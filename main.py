import unittest
from selenium import webdriver
import page


class BcitCaSearch(unittest.TestCase):
    """A test class for the BCIT search feature."""

    def setUp(self):
        """Set up our driver"""
        self.driver = webdriver.Chrome(
            "C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.bcit.ca/")

    def test_title(self):
        """Tests if the text 'BCIT' is in the page title"""
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches(),
                        "bcit.ca title doesn't match.")

    def test_search_in_bcit_ca(self):
        """Tests bcit.ca search feature. Searches the text 'Computer Information Technology' 
        and verifies that results were found. This test does not specifically check what results are found, 
        only if results were found."""

        # Load the home page
        main_page = page.MainPage(self.driver)
        
        # Sets the text of search textbox to "Computer Information Technology"
        main_page.search_text_element = "Computer Information Technology"
        main_page.click_search_button()
        
        # Check if the search results page title is contains 'Search'
        search_results_page = page.SearchResultsPage(self.driver)
        self.assertTrue(search_results_page.is_title_matches(), "bcit.ca results page title doesn't match.")
        
        # Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(),
                        "No results found.")

    def tearDown(self):
        """Teardown after every test"""
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
