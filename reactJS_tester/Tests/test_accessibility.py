# using the axe-core to check accecibility but limit the run only to keyboard mobility
def test_keyboard_accessibility(page):
    page.goto("https://react.dev/")

    page.add_script_tag(url="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.0/axe.min.js")
    results = page.evaluate("""
        async () => await axe.run(document, {
            runOnly: { type: 'tag', values: ['cat.keyboard'] },
            rules: { region: { enabled: false } }
        })
    """)
    violations = results["violations"]
    assert len(violations) == 0
