from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    URL = "url"
    IMG = "img"

class TextNode(object):
    def __init__(self, text, text_type=TextType.PLAIN, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        url = None if url is None else url
    
    def __eq__(self, value):
        if isinstance(value, TextNode):
            return True if self.text == value.text and self.text_type == value.text_type and self.url == value.url else False
        else:
            return False
    
    def __repr__(self):
        return f"TextNode(text={self.text!r}, text_type={self.text_type!r}, url={self.url!r})"