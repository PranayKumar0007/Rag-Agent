from sentence_transformers import SentenceTransformer 
from app.services.pdf_reader import read_pdf
from app.services.chunker import chunk_doc

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(chunks:list):
	texts = [chunk.text for chunk in chunks]
	embeddings = model.encode(texts)
	return embeddings
