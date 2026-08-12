from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(
	host = "localhost",
	port = 6333)

model = SentenceTransformer("all-MiniLM-L6-v2")

def search(query:str):
	query_embeddings = model.encode(query)
	result = client.query_points(
				collection_name="documents",
				query=query_embeddings,
				limit = 3
			)
	retrieved_chunks = []
	for point in result.points:
		each_chunk = {"score":point.score,"text":point.payload["text"],"page":point.payload["page"],"chunk":point.payload["chunk"],"document":point.payload["document"]}
		retrieved_chunks.append(each_chunk)
	return retrieved_chunks

