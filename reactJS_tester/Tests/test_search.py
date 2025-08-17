# tests/test_search.py
from playwright.sync_api import expect
from reactJS_tester.pages.home_page import HomePage
from reactJS_tester.components.search_modal import SearchModal

def test_search_functionality(page):
    home = HomePage(page)
    home.open()
    page.wait_for_load_state("networkidle")

    # 1) open the searchbar
    home.search_button().click()

    modal = SearchModal(page)

    # 2) Type "custom hook"
    modal.input().fill("custom hook")

    # 3) Click on the first result and capture its text
    first = modal.first_result()
    first_result_text = first.locator("a").text_content()
    first.locator("a").click()

    # 4) reopen modal to save query
    home.search_button().click()

    # 5) click star
    star_button = modal.save_star()
    expect(star_button).to_be_visible(timeout=3000)
    star_button.click()

    # 6) escape and reopen
    page.keyboard.press("Escape")
    home.search_button().click()

    # 7) assert it was saved
    favorites = modal.favorites_items()
    favorites.wait_for()
    count = favorites.count()

    found = False
    for i in range(count):
        item = favorites.nth(i)
        text = item.locator("a").text_content()
        if text == first_result_text:
            found = True
    assert found
