
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.data_store import retrieve_context


class InterviewCoach:

    def __init__(self, vector_store):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is missing. Configure your API key."
            )

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            api_key=api_key
        )

        self.vector_store = vector_store
        self.parser = StrOutputParser()

    def run_agent(self, system_prompt, user_prompt, **values):

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", user_prompt)
        ])

        chain = prompt | self.llm | self.parser

        return chain.invoke(values)

    # AGENT 1: INTERVIEWER AGENT

    def ask_question(self, company, role, difficulty, history):

        context = retrieve_context(
            self.vector_store,
            company,
            role,
            "Interview questions for " + role
        )

        return self.run_agent(
            """
            You are an expert Interviewer Agent.

            Conduct a realistic company-specific mock interview.
            Ask only one question at a time.
            Adapt questions to the selected job role.
            Do not reveal the answer.
            """,

            """
            Company: {company}
            Role: {role}
            Difficulty: {difficulty}

            Retrieved Knowledge:
            {context}

            Previous Interview:
            {history}

            Ask the next interview question.
            """,

            company=company,
            role=role,
            difficulty=difficulty,
            context=context,
            history=str(history)
        )

    # AGENT 2: EVALUATOR AGENT

    def evaluate_answer(self, company, role, answer):

        context = retrieve_context(
            self.vector_store,
            company,
            role,
            answer
        )

        return self.run_agent(
            """
            You are an Interview Evaluator Agent.

            Evaluate the candidate's answer based on:
            1. Correctness
            2. Depth of knowledge
            3. Communication skills

            Give scores out of 10.
            Explain strengths and weaknesses.
            Suggest improvements.
            """,

            """
            Company: {company}
            Role: {role}
            Candidate Answer: {answer}

            Retrieved Knowledge:
            {context}

            Evaluate the answer and provide detailed feedback.
            """,

            company=company,
            role=role,
            answer=answer,
            context=context
        )

    # AGENT 3: COACH AGENT

    def get_coaching(self, company, role, concern):

        context = retrieve_context(
            self.vector_store,
            company,
            role,
            concern
        )

        return self.run_agent(
            """
            You are a Personal Interview Coach Agent.

            Give personalised interview preparation advice.
            Identify improvement areas.
            Provide practical exercises and examples.
            Be supportive and clear.
            """,

            """
            Company: {company}
            Role: {role}
            Candidate Concern: {concern}

            Retrieved Knowledge:
            {context}

            Generate personalised coaching.
            """,

            company=company,
            role=role,
            concern=concern,
            context=context
        )

    # AGENT 4: REPORT AGENT

    def generate_report(self, company, role, history):

        return self.run_agent(
            """
            You are an Interview Report Agent.

            Prepare a professional interview performance report.
            Include strengths, weaknesses, performance summary
            and a seven-day improvement plan.
            Do not invent scores.
            """,

            """
            Company: {company}
            Role: {role}

            Interview History:
            {history}

            Generate the final performance report.
            """,

            company=company,
            role=role,
            history=str(history)
        )
