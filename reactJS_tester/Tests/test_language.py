
import re
from playwright.sync_api import expect
from reactJS_tester.pages.home_page import HomePage
from reactJS_tester.components.header import Header

def test_spanish_page(page):
    #open home page
    home = HomePage(page)
    home.open()

    #clicking the translate button
    header = Header(page)
    header.open_translations()
    
    #clicking the spanish link and catch the popup
    spanish_link = page.get_by_text("Spanish (Español)")
    with page.expect_popup() as pop:
        spanish_link.click()
    spanish_page = pop.value

    #checking the URL is valid
    spanish_page.wait_for_load_state("domcontentloaded")
    expect(spanish_page).to_have_url(re.compile(r"^https://es\.react\.dev/"))
    
    #cheking there is a text saying learn react in spanish 
    main = spanish_page.get_by_role("main")
    expect(main).to_contain_text("Aprende React")

    spanish_page.close()
