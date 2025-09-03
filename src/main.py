from textnode import TextNode, TextType
from leafnode import *
from htmlnode import *
from parentnode import *
from markdown_to_html import *
from generate_page import generate_page
import sys
import os
import shutil


def static_to_public(source,target):
	
	pub_path = os.path.join(".",target)
	static_path = os.path.join(".",source)
	
	if not os.path.exists(static_path):
		raise Exception(f"folder \"static\" does not exist in {source}")
	if not os.path.exists(pub_path):
		os.mkdir(pub_path)
	
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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
	source_items = os.listdir(dir_path_content)
	for item in source_items:
		source_item_path = os.path.join(dir_path_content,item)
		dest_item_path =os.path.join(dest_dir_path,item)
		if os.path.isdir(source_item_path):
			os.mkdir(dest_item_path)
			generate_pages_recursive(source_item_path, template_path, dest_item_path)
			continue
		if item[-3:]!=".md":
			continue
		generate_page(source_item_path,"./template.html",dest_item_path.replace(".md",".html"), basepath)

		

def main():
	if len(sys.argv)>1:
		basepath = sys.argv[1]
		
	else:
		basepath="/"
	print(basepath)
	static_to_public("static","docs")
	generate_pages_recursive("./content","./template.html","./docs", basepath)
	sys.exit(0)

if __name__=="__main__":
	main()


