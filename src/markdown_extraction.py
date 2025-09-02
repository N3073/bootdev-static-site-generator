import re
from textnode import *
def extract_markdown_images(text:str)->list:
  search_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  search_results = re.findall(search_pattern,text)
  #image_list = []
  #for result in search_results:
  #  print(result)
  #  image_list.append(result)
  return search_results

def extract_markdown_links(text:str)->list:
  search_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  search_results = re.findall(search_pattern,text)
  #link_list = []
  #for result in search_results:
  #  link_list.append(result)
  return search_results

def split_nodes_image(old_nodes):
  new_nodes=[]
  for old_node in old_nodes:
    if old_node.node_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    images = extract_markdown_images(old_node.text)
    if not len(images):
      new_nodes.append(old_node)
      continue
    text = old_node.text
    for alt,url in images:
      splits=text.split(f"![{alt}]({url})",maxsplit=1)
      if len(splits[0]):
        new_nodes.append(TextNode(splits[0],TextType.TEXT,None))
      new_nodes.append(TextNode(alt,TextType.IMAGE,url))
      text = splits[1]
    if len(text):
      new_nodes.append(TextNode(text,TextType.TEXT,None))
  return new_nodes



def split_nodes_link(old_nodes):
  new_nodes=[]
  for old_node in old_nodes:
    if old_node.node_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    images = extract_markdown_links(old_node.text)
    if not len(images):
      new_nodes.append(old_node)
      continue
    text = old_node.text
    for alt,url in images:
      splits=text.split(f"[{alt}]({url})",maxsplit=1)
      if len(splits[0]):
        new_nodes.append(TextNode(splits[0],TextType.TEXT,None))
      new_nodes.append(TextNode(alt,TextType.LINK,url))
      text = splits[1]
    if len(text):
      new_nodes.append(TextNode(text,TextType.TEXT,None))
  return new_nodes

def text_to_textnodes(text:str):
  old_nodes = [TextNode(text,TextType.TEXT,None)]
  old_nodes = split_nodes_link(old_nodes)
  old_nodes = split_nodes_image(old_nodes)
  old_nodes = split_nodes_delimiter(old_nodes,"_",TextType.ITALIC)
  old_nodes = split_nodes_delimiter(old_nodes,"`",TextType.CODE)
  old_nodes = split_nodes_delimiter(old_nodes,"**",TextType.BOLD)
  return old_nodes

def markdown_to_blocks(markdown):
  text_blocks = markdown.split("\n\n")
  text_blocks = filter(lambda x : x!="",text_blocks)
  text_blocks = map(lambda x : x.strip(), text_blocks)
  return list(text_blocks)
