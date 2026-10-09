import json
import math
from pathlib import Path


INDEX_PATH = Path(__file__).resolve().parent / "vector_index.json"


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Return cosine similarity; vectors must have the same dimensions."""
    if len(a) != len(b):
        raise ValueError(
            f"Vector dimensions differ: {len(a)} != {len(b)}. "
            "Re-index if you changed embedding models or dimensions."
        )

    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(y * y for y in b))

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot / (mag_a * mag_b)


class VectorStore:
    """A small JSON-persisted vector store for learning, not production scale."""

    def __init__(self, path: Path = INDEX_PATH):
        self.path = Path(path)
        self.items = []

    def exists(self) -> bool:
        return self.path.exists()

    def add(self, document: dict, embedding: list[float]) -> None:
        self.items.append({
            "document": document,
            "embedding": embedding,
        })

    def search(self, query_embedding: list[float], top_k: int = 3) -> list[dict]:
        if top_k < 1:
            raise ValueError("top_k must be at least 1")

        results = []
        for item in self.items:
            score = cosine_similarity(query_embedding, item["embedding"])
            results.append({
                "document": item["document"],
                "score": score,
            })

        results.sort(key=lambda item: item["score"], reverse=True)
        return results[:top_k]

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(self.items, file, ensure_ascii=False)

    def load(self) -> None:
        if not self.path.exists():
            raise FileNotFoundError(f"Index not found: {self.path}")
        with self.path.open("r", encoding="utf-8") as file:
            self.items = json.load(file)
