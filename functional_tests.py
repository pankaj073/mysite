from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http://localhost:8000");

        self.assertIn("Polls", self.browser.title);
        self.fail("Finish the test!");

if __name__ == "__main__":
    unittest.main(warnings="ignore")