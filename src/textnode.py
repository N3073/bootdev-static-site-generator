from enum import Enum

class TextType(Enum):
	CODE = "code"
	BOLD = "bold"
	ITALIC = "italic"
	LINK = "link"
	IMAGE = "image"

class TextNode():
	def __init__(self, text, node_type, url=None):
		self.text = text
		self.node_type = node_type
		self.url = url

	def __eq__(self,other)->bool:
		text_equal = self.text == other.text
		type_equal = self.node_type==other.node_type
		url_equal = self.url==other.url
		return text_equal and type_equal and url_equal

	def __repr__(self):
		return f"TextNode({self.text}, {self.node_type.value}, {self.url})"
