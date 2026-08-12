import pymupdf as pm
from app.models.document import Page,Document


def read_pdf(path:str):
	# open a pdf using PYmupdf,Read every page,Extract txt from each page
	#create a page obg for every page
	#return document object
	
	with pm.open(path) as pdf:
		pages = []
		
		for page in pdf:
			each_p = Page(page.number,page.get_text())
			pages.append(each_p)
	document = Document(path,pages)
	return document

	
		
		
		