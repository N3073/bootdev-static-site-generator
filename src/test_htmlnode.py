import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

	def test_repr(self):
		node1 = HTMLNode(tag="h1",value="Fancy title")
		node2 = HTMLNode(tag="img",value=None,children=None,props={"src":"image.jpg", "alt":"-image-", "width":"120","height":"240"})
		node3 = HTMLNode(tag="div",children=[node1,node2])
		self.assertEqual(len(node3.children),2)

	def test_props_to_html(self):
		node2 = HTMLNode(tag="img",value=None,children=None,props={"src":"image.jpg", "alt":"-image-", "width":"120","height":"240"})
		actual = node2.props_to_html()
		expected = " src=\"image.jpg\" alt=\"-image-\" width=\"120\" height=\"240\""
		self.assertEqual(actual,expected)

	def test_repr2(self):
		node1 = HTMLNode(tag="img",value=None,children=None,props={"src":"image.jpg", "alt":"-image-", "width":"120","height":"240"})
		repr_str = str(node1)
		print(repr_str)
		self.assertTrue("Tag:" in repr_str)
		self.assertTrue("Value:" in repr_str)
		self.assertTrue("Children:" in repr_str)
		self.assertTrue("Properties:" in repr_str)

