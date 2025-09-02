import unittest
from markdown_extraction import *
class TestImageExtraction(unittest.TestCase):
  def test_right_number_of_results(self):
    input_text = "some text some more text ![some image](src/image.jpg), some text ![some other image](app_feedback/img/image2.jpg)"
    results = extract_markdown_images(input_text)
    self.assertListEqual([("some image","src/image.jpg"),("some other image","app_feedback/img/image2.jpg")],results)
    self.assertEqual(2, len(results))

  def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
  def test_extract_empty_list(self):
    matches = extract_markdown_images(
        "This is text without any links or images."
    )
    self.assertListEqual([], matches)

class TestLinkExtraction(unittest.TestCase):
  def test_right_number_of_results(self):
    input_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    results = extract_markdown_links(input_text)
    self.assertListEqual([("to boot dev","https://www.boot.dev"),("to youtube","https://www.youtube.com/@bootdotdev")],results)
    self.assertEqual(2, len(results))

  def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with an [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    self.assertListEqual([("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

  def test_extract_empty_list(self):
    matches = extract_markdown_links(
        "This is text without any links or images."
    )
    self.assertListEqual([], matches)

class TestSplitNodesImage(unittest.TestCase):
  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ],
        new_nodes,
    )
  def test_split_on_multiple_nodes(self):
    node1 = TextNode(   
        "This is text with an image ![image1](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    node2 = TextNode("This text also has an image ![image3 is cool](src/static/img/image3.jpg). Which is cool!",TextType.TEXT,None)
    new_nodes = split_nodes_image([node1,node2])
    self.assertListEqual(
        [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode("This text also has an image ", TextType.TEXT),
            TextNode("image3 is cool", TextType.IMAGE, "src/static/img/image3.jpg"),
            TextNode(". Which is cool!", TextType.TEXT),
        ],
        new_nodes,
    )
  def test_ignore_non_text_nodes(self):
    nodes = [
      TextNode("image1",TextType.IMAGE,"src/static/img/image3.jpg"),
      TextNode("boot.dev",TextType.LINK,"https://www.boot.dev"),
      TextNode("bold text",TextType.BOLD),
      TextNode("code text",TextType.CODE),
      TextNode("italic text",TextType.ITALIC),
      TextNode("normal text",TextType.TEXT),
    ]
    new_nodes = split_nodes_image(nodes)
    self.assertListEqual(nodes,new_nodes)

  def test_on_string_with_no_images(self):

    node = TextNode("Making unit tests is useful. Although kind of boring and tedious.",TextType.TEXT,None)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [TextNode("Making unit tests is useful. Although kind of boring and tedious.",TextType.TEXT,None)],
        new_nodes,
    )

class TestSplitNodesLink(unittest.TestCase):
  def test_split_links(self):
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and another [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ],
        new_nodes,
    )

  def test_split_links2(self):
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and another [to youtube](https://www.youtube.com/@bootdotdev) but only 2.",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(" but only 2.", TextType.TEXT),
        ],
        new_nodes,
    )


  def test_split_on_multiple_nodes(self):
    node1 = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and another [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    node2 = TextNode("This text has a link to [google.com](https://www.google.com). Which is cool!",TextType.TEXT,None)
    new_nodes = split_nodes_link([node1,node2])
    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode("This text has a link to ", TextType.TEXT),
            TextNode("google.com", TextType.LINK, "https://www.google.com"),
            TextNode(". Which is cool!", TextType.TEXT),
        ],
        new_nodes,
    )

  def test_on_string_with_no_links(self):

    node = TextNode("Making unit tests is useful. Although kind of boring and tedious.",TextType.TEXT,None)
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [TextNode("Making unit tests is useful. Although kind of boring and tedious.",TextType.TEXT,None)],
        new_nodes,
    )
class TestTextToTextnodes(unittest.TestCase):
  def test_text_to_textnodes(self):
    test_string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    self.assertListEqual(
      [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ],
      text_to_textnodes(test_string)
    )

class TestMarkdownToTextBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self):
    md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )
  def test_excessive_new_line_removal(self):
    md = """




- listitem1
- listitem2
- listitem3


Normal text line.
second line of paragraph.

"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(len(blocks),2)
    self.assertListEqual(blocks,["- listitem1\n- listitem2\n- listitem3","Normal text line.\nsecond line of paragraph."])


  def test_leading_and_trailing_whitespace(self):
    md = """      Indented text\nMore text       """
    blocks = markdown_to_blocks(md)
    self.assertEqual(len(blocks),1)
    self.assertListEqual(["Indented text\nMore text"],blocks)
