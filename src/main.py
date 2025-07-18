from textnode import TextNode
from textnode import TextType

def main():
    node = TextNode(
        "This is some anchor text",
        text_type=TextType.PLAIN,
        url="https://www.boot.dev"
    )
    print(node)

main()