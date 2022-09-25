from unittest import TestCase

from words import word_finder


class PageFinderTest(TestCase):
    def setUp(self):
        self.page_map = word_finder.PageMap()

    def test_that_few_is_on_page_207(self):
        "Because festoon last on 206 and fieldfare last on 207"
        page_range = self.page_map.page_range("few")
        self.assertEqual((207, 207), page_range)
