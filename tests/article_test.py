import unittest

from app.models import Articles


class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.article = Articles()

    def test_articles(self):
        self.assertTrue(isinstance(self.article, Articles))


if __name__ == '__main__':
    unittest.main()