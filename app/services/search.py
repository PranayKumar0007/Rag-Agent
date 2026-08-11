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
	return result

result = search("Describe leadership and its commitments?")

	
print(result)