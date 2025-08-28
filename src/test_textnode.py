import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
	def test_eq2(self):
                node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
                node2 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
                self.assertEqual(node,node2)
	def test_repr(self):
		node = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(str(node),"TextNode(This is a text node, bold, None)")
	def test_not_eq1(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a code node", TextType.CODE)
		self.assertNotEqual(node,node2)
	def test_not_eq2(self):
                node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
                node2 = TextNode("This is a link node", TextType.LINK, "https://www.github.com")
                self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()
