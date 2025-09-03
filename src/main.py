from textnode import TextNode, TextType
from leafnode import *
from htmlnode import *
from parentnode import *
from markdown_to_html import *
import sys
def main():
	md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
	node = markdown_to_html_node(md)
	html = node.to_html()
	print(html)
	print("<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>")
	sys.exit(0)

if __name__=="__main__":
	main()
