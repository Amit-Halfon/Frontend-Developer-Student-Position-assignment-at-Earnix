# tests/test_navbar.py
import re
import pytest
from playwright.sync_api import expect
from reactJS_tester.pages.home_page import HomePage
from reactJS_tester.components.header import Header

NAV_LINKS = [
    ("Learn",      re.compile(r"^https://react\.dev/learn/?$")),
    ("Reference",  re.compile(r"^https://react\.dev/reference/react/?$")),
    ("Community",  re.compile(r"^https://react\.dev/community/?$")),
    ("Blog",       re.compile(r"^https://react\.dev/blog/?$")),
]

@pytest.mark.parametrize("text, url_regex", NAV_LINKS, ids=[n for n, _ in NAV_LINKS])
#clicking on each link in the navBar and checking that we got the expected link
def test_nav_links(page, text, url_regex):
    home = HomePage(page)
    home.open()

    header = Header(page)
    header.click_nav_text(text)

    expect(page).to_have_url(url_regex)
