# tests/test_layout_and_theme.py
from playwright.sync_api import expect
from reactJS_tester.pages.home_page import HomePage

def test_has_header(page):
    home = HomePage(page)
    home.open()
    expect(home.header()).to_have_count(1, timeout=1000)

def test_has_footer(page):
    home = HomePage(page)
    home.open()
    expect(home.footer()).to_have_count(1)

def test_theme_button(page):
    home = HomePage(page)
    home.open()

    toggle_button = home.theme_toggle_button()
    html = home.html_root()
    initial_class = html.get_attribute("class")

    toggle_button.click()
    #checking if the class that should be changed has been changed 
    expect(html).not_to_have_class(initial_class)
