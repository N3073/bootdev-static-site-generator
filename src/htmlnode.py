
class HTMLNode():
	def __init__(self,tag:str=None,value:str=None,children:list=None,props:dict=None):
		self.tag=tag
		self.value=value
		self.children=children
		self.props=props

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		props_string = ""
		if self.props:
			for prop in self.props:
				prop_string = f" {prop}=\"{self.props[prop]}\""
				props_string += prop_string
		return props_string

	def __repr__(self):
		repr_string = ""
		repr_string += f"Tag: {self.tag}\n"
		repr_string += f"Value: {self.value}\n"
		repr_string += f"Children: \n"
		if self.children:
			for child in self.children:
				repr_string += f"\tChild: {child.tag}-{child.value}\n"
		else:
			repr_string += f"\tNone\n"
		repr_string += f"Properties: \n"
		if self.props:
			for property in self.props:
				repr_string += f"\t{property}: {self.props[property]}\n"
		else:
			repr_string += f"\tNone\n"
		return repr_string
