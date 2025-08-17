# components/header.py
from playwright.sync_api import Page

class Header:
    def __init__(self, page: Page):
        self.page = page

    def nav(self):
        return self.page.locator("nav").first

    def click_nav_text(self, text: str):
        # keep your exact strategy:
        self.nav().get_by_text(text).click()

    def open_search(self):
        self.page.get_by_role("button", name="Search").click()

    def open_translations(self):
        self.page.get_by_label("Translations").click()
