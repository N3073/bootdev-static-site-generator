import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
			)
	def test_to_html_with_grandchildren_with_props(self):
		grandchild_node1 = LeafNode("b", "Grandchildren")
		grandchild_node2 = LeafNode(None, " are stupid!")
		child_node = ParentNode("p", [grandchild_node1,grandchild_node2],props={"class":"text"})
		parent_node = ParentNode("div", [child_node],props={"class":"container"})
		self.assertEqual(
			parent_node.to_html(),
			"<div class=\"container\"><p class=\"text\"><b>Grandchildren</b> are stupid!</p></div>",
			)

