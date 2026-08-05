from dataclasses import dataclass

@dataclass
class Chunk:
	id : int
	text : str
	page_num : int
	chunk_num: int
	document : str
