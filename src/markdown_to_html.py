from markdowntype import *
from markdown_extraction import *
from parentnode import *
from leafnode import *
def markdown_to_html_node(markdown):
  md_blocks = markdown_to_blocks(markdown)
  root = ParentNode(tag="div",children=[])
  for block in md_blocks:
    block_type = block_to_blocktype(block)
    match block_type:
      case BlockType.PARAGRAPH:
        root.children.append(convertParagraphToHtmlNode(block))
      case BlockType.CODE:
        root.children.append(convertCodeToHtmlNode(block))
      case BlockType.HEADING:
        root.children.append(convertHeadingToHtmlNode(block))
      case BlockType.QUOTE:
        root.children.append(convertQuoteToHtmlNode(block))
      case BlockType.UNORDERED_LIST:
        root.children.append(converULToHtmlNodeNode(block))
      case BlockType.ORDERED_LIST:
        root.children.append(convertOLToHtmlNodeNode(block))
  
  return root

def convertParagraphToHtmlNode(block:str):
  text_nodes = text_to_textnodes(block.replace("\n"," ").strip())
  return ParentNode("p",[text_node_to_html_node(x) for x in text_nodes],None)

def convertCodeToHtmlNode(block:str):
  code_text = block.replace("```","").lstrip()
  return ParentNode("pre",[LeafNode("code",code_text)])

def convertHeadingToHtmlNode(block:str):
  hashes,content = block.split(" ",maxsplit=1)
  child_nodes = [text_node_to_html_node(x) for x in text_to_textnodes(content)]
  tag = f"h{min(len(hashes),6)}"
  return ParentNode(tag,child_nodes)

def convertQuoteToHtmlNode(block:str):
  text_nodes = text_to_textnodes(block.replace(">","").replace("\n"," ").strip())
  return ParentNode("blockquote",[text_node_to_html_node(x) for x in text_nodes],None)

def converULToHtmlNodeNode(block:str):
  lines = block.split("\n")
  child_nodes = []
  for line in lines:
    child_nodes.append(ParentNode("li",[text_node_to_html_node(x) for x in text_to_textnodes(line.split(" ",maxsplit=1)[1])]))
  return ParentNode("ul",child_nodes)

def convertOLToHtmlNodeNode(block:str):
  lines = block.split("\n")
  child_nodes = []
  for line in lines:
    child_nodes.append(ParentNode("li",[text_node_to_html_node(x) for x in text_to_textnodes(line.split(" ",maxsplit=1)[1])]))
  return ParentNode("ol",child_nodes)