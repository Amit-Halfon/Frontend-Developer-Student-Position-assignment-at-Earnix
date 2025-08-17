# pages/adding_interactivity_page.py
import re
from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PWTimeoutError

class AddingInteractivityPage:
    URL = "https://react.dev/learn/adding-interactivity#responding-to-events"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def wait_preview_loaded(self):
        # your exact spinner selector and behavior
        preview = self.page.locator(".sp-loading").first
        try:
            preview.wait_for(state="visible", timeout=2000)
        except PWTimeoutError:
            pass
        expect(preview).to_be_hidden(timeout=5000)

    def expand_show_more_if_visible(self):
        show_more = self.page.locator("span", has_text="Show more").first
        if show_more.is_visible():
            show_more.click()

    def editor(self):
        return self.page.locator(".cm-editor").first

    def line_play_movie(self):
        return self.editor().locator(".cm-line", has_text="Play Movie").first

    def replace_line_with_pause_movie(self):
        line = self.line_play_movie()
        line.scroll_into_view_if_needed()
        line.click()
        # keep your exact call:
        line.fill("Pause Movie")

    def preview_frame(self):
        # keep your exact iframe title contains "Sandbox Preview"
        return self.page.frame_locator("iframe[title*='Sandbox Preview']").first

    def first_preview_button_text(self) -> str:
        btn = self.preview_frame().get_by_role("button").first
        return btn.inner_text().strip()
