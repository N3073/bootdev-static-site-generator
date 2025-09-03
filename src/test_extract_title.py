import unittest
from markdown_extraction import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title_extraction(self):
        md = "\n# Fancy title\n\n# Other title\n\n"

        title = extract_title(md)
        self.assertEqual(title,"Fancy title")

    def test_leading_space_removal(self):
        md = "\n#   Fancy title\n\n# Other title\n\n"

        title = extract_title(md)
        self.assertEqual(title,"Fancy title")
    def test_trailing_space_removal(self):
        md = "\n# Fancy title  \n\n# Other title\n\n"

        title = extract_title(md)
        self.assertEqual(title,"Fancy title")

    def test_something_else_in_front(self):
        md = "normal text \n\n# Fancy title\n\n# Other title\n\n"

        title = extract_title(md)
        self.assertEqual(title,"Fancy title")

    def test_header2_in_front(self):
        md = "##header2 \n\n# Fancy title\n\n# Other title\n\n"

        title = extract_title(md)
        self.assertEqual(title,"Fancy title")