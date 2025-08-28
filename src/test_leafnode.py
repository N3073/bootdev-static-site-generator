from leafnode import LeafNode

import unittest

class TestLeafNode(unittest.TestCase):

	def test_leafnode_to_html_h(self):
		leaf = LeafNode("h1","Fancy titles!")
		self.assertEqual(leaf.to_html(),"<h1>Fancy titles!</h1>")

	def test_leafnode_to_html_a(self):
		leaf = LeafNode("a","Boot.dev",{"href":"https://www.boot.dev"})
		self.assertEqual(leaf.to_html(),"<a href=\"https://www.boot.dev\">Boot.dev</a>")

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_notag(self):
		leaf=LeafNode(None, "Hello, world!",{"href":"https://www.boot.dev"})
		self.assertEqual(leaf.to_html(), "Hello, world!")


