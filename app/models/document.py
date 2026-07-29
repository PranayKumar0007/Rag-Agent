from dataclasses import dataclass

@dataclass
class Page:
	page_num : int
	text : str
@dataclass
class Document:
	filename :str
	pages : list[Page]
	