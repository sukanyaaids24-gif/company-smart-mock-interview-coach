# Company-Smart Mock Interview Coach

## 1. Project Overview

The Company-Smart Mock Interview Coach is an AI-powered interview preparation system designed to help candidates prepare for company-specific job interviews.

The application uses Agentic AI, Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG) to conduct mock interviews, evaluate candidate answers, provide personalised coaching, and generate interview performance reports.

## 2. Problem Statement

Candidates often face difficulties preparing for company-specific interviews because they lack personalised guidance, realistic interview practice, and detailed feedback on their answers.

Traditional interview preparation methods do not always provide interactive learning or adaptive feedback.

This project aims to develop an intelligent interview preparation assistant that provides an interactive and personalised interview experience.

## 3. Project Objectives

- Conduct company-specific mock interviews.
- Generate relevant interview questions based on job roles.
- Evaluate candidate answers using AI.
- Identify strengths and weaknesses.
- Provide personalised interview coaching.
- Generate interview performance reports.
- Retrieve relevant information using a vector database.

## 4. Proposed Solution

The proposed system uses multiple specialised AI agents that collaborate to provide an intelligent interview preparation experience.

The system consists of four major agents:

### 1. Interviewer Agent
- Generates company-specific interview questions.
- Adapts questions according to job roles.
- Conducts interactive mock interviews.

### 2. Evaluator Agent
- Evaluates candidate responses.
- Analyses correctness and relevance.
- Provides scores and improvement suggestions.

### 3. Coach Agent
- Identifies candidate improvement areas.
- Provides personalised preparation strategies.
- Suggests practical learning activities.

### 4. Report Agent
- Analyses interview performance.
- Summarises strengths and weaknesses.
- Generates a personalised improvement plan.

## 5. System Architecture

The system follows an agent-based architecture integrated with Retrieval-Augmented Generation (RAG).

Workflow:

1. User selects the target company and job role.
2. The system identifies the requested activity.
3. The appropriate AI agent processes the request.
4. Relevant interview knowledge is retrieved from ChromaDB.
5. The LLM generates a contextual response.
6. The application displays feedback, coaching or interview questions.

## 6. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | User interface |
| LangChain | LLM application framework |
| LCEL | Chain composition |
| Groq | LLM inference |
| ChromaDB | Vector database |
| HuggingFace | Text embeddings |
| RAG | Context retrieval |

## 7. Retrieval-Augmented Generation (RAG)

The system uses RAG to retrieve relevant interview information from a sample interview knowledge base.

The documents are converted into vector embeddings using a HuggingFace embedding model and stored in ChromaDB.

When a candidate submits a query, the system retrieves relevant documents using similarity search.

The retrieved information is provided to the LLM to generate contextual responses.

## 8. Project Structure

```text
company-smart-mock-interview-coach/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── agents.py
│   └── data_store.py
│
└── data/
    └── sample_interview_bank.csv
```

## 9. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/company-smart-mock-interview-coach.git
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key

Create a `.env` file and add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key
```

Never upload your actual API key to GitHub.

### Step 4: Run the Application

```bash
streamlit run app.py
```

## 10. Expected Outcomes

- Interactive company-specific mock interviews.
- AI-powered answer evaluation.
- Personalised interview coaching.
- Automated interview performance reports.
- Context-aware responses using RAG.

## 11. Future Enhancements

- Voice-based mock interviews.
- Resume-based interview preparation.
- Real-time interview feedback.
- Expanded company-specific knowledge bases.
- Interview performance analytics.

## 12. Conclusion

The Company-Smart Mock Interview Coach demonstrates how Agentic AI, LLMs, and Retrieval-Augmented Generation can be integrated to create an intelligent interview preparation assistant.

The project aims to improve interview readiness through personalised learning, interactive practice, and AI-driven feedback.

---

**Project:** Company-Smart Mock Interview Coach  
**Domain:** Agentic Artificial Intelligence  
**Language:** Python
