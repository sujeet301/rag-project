import argparse
from dotenv import load_dotenv

from documents import documents
from rag import index_documents, answer_question
from vector_store import VectorStore


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Local Gemini RAG demo")
    parser.add_argument(
        "--reindex",
        action="store_true",
        help="Re-create embeddings and overwrite the saved vector index."
    )
    args = parser.parse_args()

    store = VectorStore()

    if args.reindex or not store.exists():
        print("Indexing documents with Gemini embeddings...")
        index_documents(documents, store)
        store.save()
        print(f"Indexed {len(store.items)} document chunks.")
    else:
        store.load()
        print(f"Loaded {len(store.items)} chunks from the saved index.")

    print("\nCompany Policy Assistant")
    print("Ask a question, or type 'exit' to quit.")
    print("Tip: run `python app.py --reindex` after changing documents.py.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            answer, sources = answer_question(question, store)
            print(f"\nAssistant: {answer}")
            if sources:
                print("\nSources:")
                for source in sources:
                    page = f", page {source['page']}" if source.get("page") else ""
                    print(f"- {source['source']}{page} (similarity: {source['score']:.3f})")
            print()
        except Exception as exc:
            print(f"\nAn error occurred: {exc}")
            print("Check your API key, model access, internet connection, and package versions.\n")


if __name__ == "__main__":
    main()
