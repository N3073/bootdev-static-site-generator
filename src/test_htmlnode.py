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
