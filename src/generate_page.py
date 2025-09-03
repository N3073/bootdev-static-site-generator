from markdown_to_html import markdown_to_html_node
from parentnode import *
from htmlnode import *
from markdown_extraction import extract_title
import re

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path,"r") as f:
        md = f.read()
        f.close()

    with open(template_path,"r") as f:
        html_template = f.read()
        f.close()
    md_html = markdown_to_html_node(md)
    html_template=re.sub(r"\{\{ *Content *\}\}",md_html.to_html(),html_template)
    html_template=re.sub(r"\{\{ *Title *\}\}",extract_title(md),html_template)
    html_template = html_template.replace("href=\"/",f"href=\"{basepath}")
    html_template = html_template.replace("src=\"/",f"src=\"{basepath}")
    with open(dest_path, "w") as f:
        f.write(html_template)
        f.close()