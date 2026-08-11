from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

from app.services.chunker import chunk_doc
from app.services.embedder import embed
from app.services.pdf_reader import read_pdf


client = QdrantClient(
    host="localhost",
    port=6333
)

client.recreate_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

doc = read_pdf("data/sample/dataset_1.pdf")
chunks = chunk_doc(doc)
embeddings = embed(chunks)

points = []
for chunk,embedding in zip(chunks,embeddings):
	points.append(
		PointStruct(
			id = chunk.id,
			vector = embedding.tolist(),
			payload = {
				"text" : chunk.text,
				"page" : chunk.page_num,
				"chunk" : chunk.chunk_num,
				"document": chunk.document},
		)
	)

client.upsert(
	collection_name = "documents",
	points = points)
# print(client.count("documents"))

# print(len(chunks))
# print(len(embeddings))
# print(len(embeddings[0]))