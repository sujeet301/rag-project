import os
from dotenv import load_dotenv
from google.genai import types

from embeddings import client, create_embedding, GENERATION_MODEL
from vector_store import VectorStore

load_dotenv()

TOP_K = int(os.getenv("RAG_TOP_K", "3"))


def index_documents(documents: list[dict], store: VectorStore) -> None:
    """
    Create an embedding for each supplied chunk and add it to the store.
    This is the indexing phase; run it when the knowledge base changes.
    """
    store.items = []

    for number, document in enumerate(documents, start=1):
        text = document.get("text", "").strip()
        if not text:
            print(f"Skipping empty document chunk #{number}")
            continue

        print(f"Embedding chunk {number}/{len(documents)}: {document.get('source', 'unknown source')}")
        vector = create_embedding(text)
        store.add(document, vector)


def answer_question(question: str, store: VectorStore) -> tuple[str, list[dict]]:
    """
    Embed the user's question, retrieve the top matching chunks,
    and ask Gemini to answer from those chunks.
    """
    if not store.items:
        raise RuntimeError("The vector store is empty. Run indexing first.")

    query_vector = create_embedding(question)
    matches = store.search(query_vector, top_k=TOP_K)

    # Avoid sending very weak matches to Gemini.
    # Tune this threshold with a real evaluation set; it is only a starter default.
    min_score = float(os.getenv("RAG_MIN_SIMILARITY", "-1"))
    matches = [match for match in matches if match["score"] >= min_score]

    if not matches:
        return (
            "I couldn't find relevant information in the available documents.",
            [],
        )

    context_parts = []
    sources = []

    for match in matches:
        doc = match["document"]
        source = doc.get("source", "unknown source")
        page = doc.get("page")
        citation = f"{source}" + (f", page {page}" if page else "")
        context_parts.append(f"[Source: {citation}]\n{doc['text']}")
        sources.append({
            "source": source,
            "page": page,
            "score": match["score"],
        })

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""
You are a careful company-policy assistant.

Answer the user's question using only the evidence in CONTEXT.
Do not invent policy details or use outside knowledge to fill gaps.
If the context does not answer the question, clearly say that the
available documents do not contain enough information.
If sources conflict, mention the conflict instead of guessing.
Be concise and include source names in the answer when useful.

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.2),
    )

    answer = response.text or "The model did not return a text answer."
    return answer, sources
