from enum import Enum

class Types(Enum):
    NORMAL = " "
    BOLD = "** **"
    ITALIC = "* *"
    CODE = "` `"
    LINKS = "[ ]( )"
    IMAGES = "![ ]( )"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self):
        if