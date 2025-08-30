from htmlnode import HTMLNode

class ParentNode(HTMLNode):

	def __init__(self, tag:str,children:list,props:dict=None):
		super().__init__(tag,None,children,props)

	def to_html(self):
		if not self.tag:
			raise ValueError("Tag is None!")
		if not self.children or len(self.children)==0:
			raise ValueError("A parent node must have children!")
		html_string=""
		html_string += f"<{self.tag}{self.props_to_html()}>"
		for child in self.children:
			html_string += f"{child.to_html()}"
		html_string += f"</{self.tag}>"
		return html_string

