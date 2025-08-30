from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self,tag:str,value:str,props:dict=None):
		if value is None:
			raise TypeError(f"Invalid argument type of parameter \"value\": {type(value)}")
		super().__init__(tag,value,None,props)

	def to_html(self)->str:
		if self.value is None:
			raise ValueError("Value cannot be None")
		if self.tag is None:
			return self.value

		match self.tag:
			case "img":
				return f"<{self.tag}{self.props_to_html()}>"
			case _:
				return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

