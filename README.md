# Gemini RAG Project (Learning Version)

A small command-line RAG assistant using Gemini embeddings, cosine similarity,
and a JSON-persisted local vector store. It intentionally avoids RAG frameworks
so you can see each step.

## 1. Requirements
- Python 3.10+
- A Gemini API key with access to the selected models
- Internet connection for Gemini API calls

## 2. Setup (Windows PowerShell / CMD)

```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and replace `replace_with_your_own_key` with your own Gemini API key.
Do not share or commit `.env`.

## 3. Run

```bash
python app.py
```

The first run creates embeddings and saves them to `vector_index.json`.
Later runs load the saved index and only embed the user's question.

To rebuild the index after editing `documents.py`:

```bash
python app.py --reindex
```

Type `exit` to quit.

## 4. How it works

Indexing:
1. Read the chunks from `documents.py`.
2. Create a Gemini embedding for each chunk.
3. Save text, source metadata, and vectors to `vector_index.json`.

Querying:
1. Create an embedding for the user's question.
2. Compare it with stored vectors using cosine similarity.
3. Retrieve the top-k chunks.
4. Send the question and retrieved context to Gemini.
5. Print the answer and source references.

## 5. Important limitations

- This is a learning/demo vector store: it scans every vector linearly and keeps
  the index in one JSON file. It is not suitable for large production datasets.
- `documents.py` contains pre-written text chunks, not a PDF ingestion pipeline.
  Add PDF/text extraction and chunking before using real files.
- The similarity threshold is a tunable starting setting, not a universal value.
- RAG reduces but does not eliminate hallucinations. Validate important answers.
- Check the official Gemini docs if model availability or SDK behavior changes.
