import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "This is a test case.")
        print(node)


if __name__ == "__main__":
    unittest.main()

