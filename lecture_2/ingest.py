from src.loader import load_and_split
from src.embeddings import ingest_documents
def ingest_documents_from_pdf(path: str):
    try:
        documents = load_and_split(path)
        print(f"Ingesting {len(documents)} documents from {path}")
        ingest_documents(documents=documents)
        print(f"Ingested {len(documents)} documents from {path}")
    except Exception as e:
        print(f"Error ingesting documents from {path}: {e}")
        raise e
if __name__ == "__main__":
    ingest_documents_from_pdf("lecture_2/data/jobs.pdf")