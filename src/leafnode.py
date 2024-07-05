from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</self.tag>"
        render = f"<{self.tag}"
        for key, value in self.props:
            render += f" {key}=\"{value}\""
        render += f">{self.value}</{self.tag}>"
        return render
