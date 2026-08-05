from app.models.chunk import Chunk
from app.services import pdf_reader as pr
import os

def chunk_doc(document):
	pages = document.pages
	doc_name = os.path.basename(document.filename)
	chunks = []
	chunk_num = 0
	for page_num,page in enumerate(pages):
		start = 0
		while start<len(page.text):
			end = start+300
			text = page.text[start:end]
			chunks.append(Chunk(chunk_num,text,page_num,chunk_num,doc_name))
			start += 250
			chunk_num +=1
	return chunks

doc = pr.read_pdf("data/sample/ACSE04.pdf")
chunks = chunk_doc(doc)
print(len(chunks))
print(chunks[0:4])


