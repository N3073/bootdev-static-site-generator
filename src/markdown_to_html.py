from blocktype import *
from markdown_extraction import *

def markdown_to_html_node(markdown):
  md_blocks = markdown_to_blocks(markdown)
  html_string = "<div>"
  for block in md_block:
    block_type = markdown_to_blocktype(block)
    match block_type:
      case BlockType.PARAGRAPH:
      case BlockType.CODE:
      case BlockType.HEADING:
      case BlockType.QUOTE:
      case BlockType.UNORDERED_LIST:
      case BlockType.ORDERED_LIST:
