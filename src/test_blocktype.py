import unittest
from markdowntype import *
class TestBlockType(unittest.TestCase):
  def test_code_block_detection(self):
    md = "```code block```"
    md2 = "```code block\nmore code\neven more code```" 
    md3 = "```not code block`"
    md4 = "`not code block```"
    self.assertEqual(BlockType.CODE,block_to_blocktype(md))
    self.assertEqual(BlockType.CODE,block_to_blocktype(md2))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md3))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md4))

  def test_heading_block_detection(self):
    md = "#### Heading4"
    md2 = "## HEading2"
    md3 = "m## not heading"
    md4 = "##not heading"
    self.assertEqual(BlockType.HEADING,block_to_blocktype(md))
    self.assertEqual(BlockType.HEADING,block_to_blocktype(md2))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md3))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md4))

  def test_quote_block_detection(self):
    md = ">You shall not pass!\n>Foolish puppet!\n>Holy mother!"
    md2 = ">You shall not pass!"
    md3 = ">You shall not pass!\n>Foolish puppet!\n<Holy mother!"
    md4 = "##not a quote"
    self.assertEqual(BlockType.QUOTE,block_to_blocktype(md))
    self.assertEqual(BlockType.QUOTE,block_to_blocktype(md2))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md3))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md4))

  def test_unordered_list_detection(self):
    md = "- You shall not pass!\n- Foolish puppet!\n- Holy mother!"
    md2 = "- You shall not pass!"
    md3 = "-You shall not pass!\n- Foolish puppet!\n- Holy mother!"
    md4 = "4 You shall not pass!\n3 Foolish puppet!\n1 Holy mother!"
    self.assertEqual(BlockType.UNORDERED_LIST,block_to_blocktype(md))
    self.assertEqual(BlockType.UNORDERED_LIST,block_to_blocktype(md2))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md3))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md4))
  def test_ordered_list_detection(self):
    md = "1. You shall not pass!\n2. Foolish puppet!\n3. Holy mother!"
    md2 = "1. You shall not pass!"
    md3 = "0. You shall not pass!\n1. Foolish puppet!\n2. Holy mother!"
    md4 = "2. You shall not pass!\n3. Foolish puppet!\n4. Holy mother!"
    md5 = "1 You shall not pass!\n2 Foolish puppet!\n3 Holy mother!"
    md6 = "1.You shall not pass!\n2.Foolish puppet!\n3.Holy mother!"
    self.assertEqual(BlockType.ORDERED_LIST,block_to_blocktype(md))
    self.assertEqual(BlockType.ORDERED_LIST,block_to_blocktype(md2))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md3))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md4))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md5))
    self.assertEqual(BlockType.PARAGRAPH,block_to_blocktype(md6))
