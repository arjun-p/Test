import unittest
from Test import TextBlock


class TestTextBlock(unittest.TestCase):
    """Tests for TextBlock.py"""

    def test_textBlocker_upperCaseCheck_negative(self):
        self.assertRaises(ValueError, TextBlock.text_blocker(['AaZ']))
        self.assertRaises(ValueError, TextBlock.text_blocker(['a']))
        self.assertRaises(ValueError, TextBlock.text_blocker(['AAAAAAAAaAAAA']))
        self.assertRaises(ValueError, TextBlock.text_blocker(['ABC', 'BCD', 'CaB']))

    def test_textBlocker_upperCaseCheck_positive(self):
        self.assertEquals(TextBlock.text_blocker(['ABC', 'XYZ']), ['AX', 'BY', 'CZ'])

    def test_textBlocker_characterLimitCheck_negative(self):
        self.assertRaises(ValueError, TextBlock.text_blocker(['A'*51]))
        self.assertRaises(ValueError, TextBlock.text_blocker(['ABC', '', 'DEF']))
        self.assertRaises(ValueError, TextBlock.text_blocker(['ABC', ['A'*51]]))

    def test_textBlocker_characterLimitCheck_positive(self):
        self.assertEquals(TextBlock.text_blocker(['A'*50]), ['A']*50)

    def test_textBlocker_listCountCheck_negative(self):
        self.assertRaises(ValueError, TextBlock.text_blocker([]))
        self.assertRaises(ValueError, TextBlock.text_blocker(['A']*51))

    def test_textBlocker_listCountCheck_positive(self):
        self.assertEquals(TextBlock.text_blocker(['A']*50), ['A'*50])
