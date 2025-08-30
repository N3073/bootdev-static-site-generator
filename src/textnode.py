from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
	CODE = "code"
	BOLD = "bold"
	ITALIC = "italic"
	LINK = "link"
	IMAGE = "image"
	TEXT = "text"

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

def text_node_to_html_node(text_node:TextNode):
	if not text_node:
		raise ValueError("text_node cannot be None")
	if not isinstance(text_node, TextNode):
		raise ValueError("text_node must be of type TextNode")

	match text_node.node_type:
		case TextType.CODE:
			return LeafNode("code",text_node.text)
		case TextType.BOLD:
			return LeafNode("b",text_node.text)
		case TextType.ITALIC:
			return LeafNode("i",text_node.text)
		case TextType.LINK:
			return LeafNode("a",text_node.text,{"href":text_node.url})
		case TextType.IMAGE:
			return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
		case TextType.TEXT:
			return LeafNode(None,text_node.text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	#delimiters = {"`":TextType.CODE,"_":TextType.ITALIC,"**":TextType.BOLD}
	#new_text_type = delimiters[delimiter]
	new_nodes = []
	for old_node in old_nodes:
		if old_node.node_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		splits = old_node.text.split(delimiter)
		if not len(splits)%2:
			raise Exception("Invalid markdown syntax")
		if len(splits)==1:
			new_nodes.append(old_node)
			continue
		for i in range(len(splits)):
			if splits[i]=='':
				continue
			if i%2:
				new_nodes.append(TextNode(splits[i],text_type))
			else:
				new_nodes.append(TextNode(splits[i],TextType.TEXT))
	return new_nodes
