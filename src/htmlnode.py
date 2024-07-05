class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        print(f"{self.tag}: {self.value} -> {self.children}, {self.props}")

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = " "
        for key, value in self.props:
            attributes += f"{key}=\"{value}\" "
        return attributes

