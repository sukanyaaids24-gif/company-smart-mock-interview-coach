
import csv
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = ROOT / "data" / "sample_interview_bank.csv"

DB_DIR = ROOT / "chroma_db"


def load_sample_documents():

    documents = []

    with open(DATA_FILE, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            content = f"""
            Company: {row['company']}
            Role: {row['role']}
            Question: {row['question']}
            Expected Points: {row['expected_points']}
            Feedback Pattern: {row['feedback_pattern']}
            """

            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "company": row["company"],
                        "role": row["role"]
                    }
                )
            )

    return documents


def initialize_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        collection_name="company_interview_knowledge",
        embedding_function=embeddings,
        persist_directory=str(DB_DIR)
    )

    if vector_store._collection.count() == 0:
        vector_store.add_documents(load_sample_documents())

    return vector_store


def retrieve_context(vector_store, company, role, query):

    search_query = (
        f"Company: {company}. "
        f"Role: {role}. "
        f"{query}"
    )

    results = vector_store.similarity_search(
        search_query,
        k=4
    )

    if not results:
        return "No relevant interview information found."

    return "\n\n".join(
        document.page_content
        for document in results
    )
