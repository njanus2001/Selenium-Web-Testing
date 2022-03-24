from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    locator = 'query'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here"""

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "BCIT" appears in page title"""

        return "BCIT" in self.driver.title

    def click_search_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        """Varifies that search results were found"""
        return "No results found." not in self.driver.page_source
    
    def is_title_matches(self):
        """Verifies that the text "Search" appears in page title"""

        return "Search" in self.driver.title
