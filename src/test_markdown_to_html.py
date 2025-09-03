import unittest
from markdown_to_html import *

class TestMarkdownToHtml(unittest.TestCase):
  def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

  def test_heading(self):
    md = """
### Heading3

###### Heading6

####### Heading6

"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><h3>Heading3</h3><h6>Heading6</h6><h6>Heading6</h6></div>"
    )

  def test_ul(self):
    md="""
- List item1
- List item2
- List item3

- List item4
- List item5
- List item6
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><ul><li>List item1</li><li>List item2</li><li>List item3</li></ul><ul><li>List item4</li><li>List item5</li><li>List item6</li></ul></div>"
    )

  def test_ol(self):
    md="""
1. List item1
2. List item2
3. List item3

1. List item4
2. List item5
3. List item6
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><ol><li>List item1</li><li>List item2</li><li>List item3</li></ol><ol><li>List item4</li><li>List item5</li><li>List item6</li></ol></div>"
    ) 

  def test_quote(self):
    md="""
>You shall not pass!
>Foolish puppet!
>
>I made it up!
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><blockquote>You shall not pass! Foolish puppet!  I made it up!</blockquote></div>"
    ) 

  def test_paragraph_with_image(self):
    md="""
Paragraph with an image: [to boot.dev](https://www.boot.dev)
Foolish puppet!
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><p>Paragraph with an image: <a href=\"https://www.boot.dev\">to boot.dev</a> Foolish puppet!></p></div>"
    ) 

  def test_paragraph_with_image(self):
    md="""
Paragraph with an image: ![-image-](src/image.jpg)
Foolish puppet!
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><p>Paragraph with an image: <img src=\"src/image.jpg\" alt=\"-image-\"> Foolish puppet!</p></div>"
    ) 
