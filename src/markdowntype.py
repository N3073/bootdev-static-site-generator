from enum import Enum
from leafnode import LeafNode
class BlockType(Enum):
        PARAGRAPH = "paragraph"
        HEADING = "heading"
        CODE = "code"
        QUOTE = "quote"
        UNORDERED_LIST = "unordered_list"
        ORDERED_LIST = "ordered_list"

import re
def block_to_blocktype(block:str):

  heading_pattern_matches = re.findall("^[#]+ ",block)
  if len(heading_pattern_matches)>0:
    return BlockType.HEADING

  code_pattern_matches = re.findall("^[`]{3}.*[`]{3}$",block,re.DOTALL)
  if len(code_pattern_matches)>0:
    return BlockType.CODE

  quote_matches = re.findall(">.*\n?",block)
  if len(quote_matches)>0 and len(quote_matches)==len(block.split("\n")):
    return BlockType.QUOTE

  ul_matches = re.findall("- .*\n?",block)
  if len(ul_matches)>0 and len(ul_matches)==len(block.split("\n")):
    return BlockType.UNORDERED_LIST

  ol_matches = re.findall("[1-9][0-9]*[.] .*\n?",block)
  if len(ol_matches)>0 and len(ol_matches)==len(block.split("\n")):
    i = 1
    is_ol=True
    for match in ol_matches:
      item_number = int(match.split(".")[0])
      if i!=item_number:
        is_ol=False
        break
      i += 1
    if is_ol: return BlockType.ORDERED_LIST
  return BlockType.PARAGRAPH
