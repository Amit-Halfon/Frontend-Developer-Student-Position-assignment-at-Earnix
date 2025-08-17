
from playwright.sync_api import Page

class HomePage:
    URL = "https://react.dev/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def header(self):
        return self.page.locator("header")

    def footer(self):
        return self.page.locator("footer")

    #finds the theme toggle button
    def theme_toggle_button(self):
        return self.page.get_by_role("button", name="Use Dark Mode")

    #finds the html tag
    def html_root(self):
        return self.page.locator("html")

    def search_button(self):
        return self.page.get_by_role("button", name="Search")

    def translations_button(self):
        return self.page.get_by_label("Translations")
