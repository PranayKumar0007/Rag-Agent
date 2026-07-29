import pymupdf as pm
from app.models.document import Page,Document

def read_pdf(path:str):
	# open a pdf using PYmupdf,Read every page,Extract txt from each page
	#create a page obg for every page
	#return document object
	with pm.open(path) as doc:
		doc = []
		for page in doc:
			each_p = Page(page.number,page.get_text)
			doc.append(each_p)
	Document(path,doc)
	return doc
	


	
		
		
		