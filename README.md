# Beauty Store RAG System

A Retrieval-Augmented Generation service that answers questions over beauty-retail documents and order data, exposed as a Flask API.

> [!IMPORTANT]
> **This repository is currently incomplete.** `main.py` imports `src.flask_api_rag_setup`, but the `src/` package is not committed, so the application will fail at import. The data files and entry point are present; the retrieval and API layer still needs to be pushed.

## Architecture

```
main.py  ──►  initialize_rag_system()   # build/load the vector index
         └──►  Flask app on 0.0.0.0:5000 # query endpoint
```

`main.py` loads configuration from a `.env` file, disables ChromaDB's anonymised telemetry, initialises the retrieval system, then serves the Flask app.

## Intended stack

| Component | Role |
|---|---|
| **OpenAI** | Embeddings and answer generation |
| **LlamaIndex** | Document loading, chunking, retrieval orchestration |
| **ChromaDB** | Vector store for embedded document chunks |
| **Flask** | HTTP API surface |

## Data

| File | Contents |
|---|---|
| `Nykaa_Beauty_Summit_Report_2024-v5.pdf` | Unstructured industry report — the document corpus |
| `Beauty-Store-Orders-YTD-2024.csv` | Year-to-date order records — structured sales data |

Pairing an unstructured report with structured order data is what makes RAG useful here: the model can ground qualitative answers about market trends in actual transaction figures rather than relying on pretrained knowledge.

## Configuration

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=sk-...
```

`ANONYMIZED_TELEMETRY` is set to `False` in code, so Chroma will not phone home.

## Running it

```bash
pip install flask python-dotenv llama-index chromadb openai
python main.py
```

The server listens on port 5000 and binds `0.0.0.0`, so it is reachable from outside the container when port-mapped.

## Notes

- `debug=False` is set explicitly, which is correct for anything exposed beyond localhost — Flask's debugger allows arbitrary code execution.
- Binding `0.0.0.0` exposes the service on all interfaces; put it behind a reverse proxy or restrict the port before deploying.
- Never commit the `.env` file — the API key must stay out of version control.
