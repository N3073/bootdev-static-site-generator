import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter
from leafnode import LeafNode

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

	def test_textnode_to_htmlnode_link(self):
		text_node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
		exp_leaf_node = LeafNode("a","This is a link node",{"href":"https://www.boot.dev"})
		act_leaf_node = text_node_to_html_node(text_node)
		self.assertEqual(exp_leaf_node.tag,act_leaf_node.tag)
		self.assertEqual(exp_leaf_node.value,act_leaf_node.value)
		self.assertTrue("href" in act_leaf_node.props)
		self.assertEqual(act_leaf_node.props["href"],"https://www.boot.dev")
		self.assertEqual(act_leaf_node.to_html(),exp_leaf_node.to_html())

	def test_textnode_to_htmlnode_img(self):
		text_node = TextNode("-image-", TextType.IMAGE, "image.jpg")
		exp_leaf_node = LeafNode("img","",{"src":"image.jpg","alt":"-image-"})
		act_leaf_node = text_node_to_html_node(text_node)
		self.assertEqual(exp_leaf_node.tag,act_leaf_node.tag)
		self.assertEqual(exp_leaf_node.value,act_leaf_node.value)
		self.assertTrue("src" in act_leaf_node.props)
		self.assertTrue("alt" in act_leaf_node.props)
		self.assertEqual(act_leaf_node.props["src"],"image.jpg")
		self.assertEqual(act_leaf_node.props["alt"],"-image-")
		self.assertEqual(act_leaf_node.to_html(),exp_leaf_node.to_html())

	def test_textnode_to_htmlnode_text(self):
		text_node = TextNode("Some text", TextType.TEXT)
		exp_leaf_node = LeafNode(None,"Some text")
		act_leaf_node = text_node_to_html_node(text_node)
		self.assertEqual("Some text",act_leaf_node.to_html())
		self.assertEqual(act_leaf_node.to_html(),exp_leaf_node.to_html())
		self.assertEqual(exp_leaf_node.tag,act_leaf_node.tag)

	def test_textnode_to_htmlnode_bold(self):
		text_node = TextNode("Text", TextType.BOLD)
		exp_leaf_node = LeafNode("b","Text")
		act_leaf_node = text_node_to_html_node(text_node)
		self.assertEqual("<b>Text</b>",act_leaf_node.to_html())
		self.assertEqual(act_leaf_node.to_html(),exp_leaf_node.to_html())
		self.assertEqual(exp_leaf_node.tag,act_leaf_node.tag)

	def test_textnode_split(self):
		node = TextNode("**This is text** with a `code block` _word_", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(len(new_nodes),3)
		self.assertEqual(new_nodes[0].text,"**This is text** with a ")
		self.assertEqual(new_nodes[0].node_type,TextType.TEXT)
		self.assertEqual(new_nodes[1].text,"code block")
		self.assertEqual(new_nodes[1].node_type,TextType.CODE)
		self.assertEqual(new_nodes[2].text," _word_")
		self.assertEqual(new_nodes[2].node_type,TextType.TEXT)
		new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
		self.assertEqual(len(new_nodes),4)
		self.assertEqual(new_nodes[2].text," ")
		self.assertEqual(new_nodes[2].node_type,TextType.TEXT)
		self.assertEqual(new_nodes[3].text,"word")
		self.assertEqual(new_nodes[3].node_type,TextType.ITALIC)
		new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
		self.assertEqual(len(new_nodes),5)
		self.assertEqual(new_nodes[0].text,"This is text")
		self.assertEqual(new_nodes[0].node_type,TextType.BOLD)
		self.assertEqual(new_nodes[1].text," with a ")
		self.assertEqual(new_nodes[1].node_type,TextType.TEXT)


