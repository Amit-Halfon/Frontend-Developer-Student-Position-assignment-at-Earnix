
from playwright.sync_api import expect
from reactJS_tester.pages.adding_interactivity_page import AddingInteractivityPage

def test_code_editor_updates_preview(page):
    page.set_viewport_size({"width": 1280, "height": 900})
    adding = AddingInteractivityPage(page)
 
    #opening the page , wait fot the buttons in the iframe to be loaded, expand the Code Mirror
    adding.open()
    adding.wait_preview_loaded()
    adding.expand_show_more_if_visible()

    #locate the code editor
    editor = adding.editor()
    expect(editor).to_be_visible()

    # change the line Play Movie to Pause Movie and wait a fewe seconds so the buttons will load again
    adding.replace_line_with_pause_movie()
    expect(editor.locator(".cm-line", has_text="Pause Movie").first).to_be_visible()
    page.wait_for_timeout(4000)

    # check if the text of the first button was changed to Pause Movie 
    text = adding.first_preview_button_text()
    assert text == "Pause Movie"
