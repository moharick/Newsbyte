import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
    def setUp(self):
        self.source = Sources("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")

    def source_test(self):
        self.assertTrue(isinstance(self.source, Sources))


if __name__ == '__main__':
    unittest.main()