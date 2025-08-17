# components/search_modal.py
from playwright.sync_api import Page

class SearchModal:
    def __init__(self, page: Page):
        self.page = page

    def input(self):
        return self.page.locator("#docsearch-input")

    def results_list(self):
        return self.page.locator("#docsearch-list")

    def first_result(self):
        results = self.results_list()
        return results.locator("li").first

    def save_star(self):
        return self.page.get_by_title("Save this search").first

    def favorites_items(self):
        return self.page.locator("ul#docsearch-list li")
