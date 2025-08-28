from textnode import TextNode, TextType
import sys
def main():
	dummy_node = TextNode("print(hello world)",TextType.CODE)
	dummy_node2 = TextNode("boot.dev",TextType.LINK,"https://www.boot.dev")
	dummy_node3 = TextNode("print(hello world)",TextType.CODE)
	print(dummy_node==dummy_node2)
	print(dummy_node==dummy_node3)
	print(dummy_node)
	print(dummy_node2)
	sys.exit(0)

if __name__=="__main__":
	main()
