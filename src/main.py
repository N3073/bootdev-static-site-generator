from textnode import TextNode, TextType
from leafnode import *
from htmlnode import *
from parentnode import *
from markdown_to_html import *
from generate_page import generate_page
import sys
import os
import shutil


def static_to_public(root):
	
	pub_path = os.path.join(root,"public")
	static_path = os.path.join(root,"static")
	
	if not os.path.exists(static_path):
		raise Exception(f"folder \"static\" does not exist in {root}")
	if not os.path.exists(pub_path):
		raise Exception(f"folder \"public\" does not exist in {root}")
	
	for item in os.listdir(pub_path):
		item_path = os.path.join(pub_path,item)
		if os.path.isdir(item_path):
			shutil.rmtree(item_path)
		else:
			os.remove(item_path)
	
	recursive_copy(static_path,pub_path)

def recursive_copy(source,target):
	source_items = os.listdir(source)
	for item in source_items:
		item_source_path = os.path.join(source,item)
		item_target_path = os.path.join(target,item)
		if os.path.isdir(item_source_path):
			print(f"mkdir: {item_target_path}")
			os.mkdir(item_target_path)
			recursive_copy(item_source_path,item_target_path)
		else:
			print(f"copy: {item_source_path} --> {item_target_path}")
			shutil.copy(item_source_path,item_target_path)


def main():
	static_to_public(".")
	generate_page("./content/index.md","./template.html","./public/index.html")
	sys.exit(0)

if __name__=="__main__":
	main()


