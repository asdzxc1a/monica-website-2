from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = (ROOT / "index.html").read_text(encoding="utf-8")
STYLES_CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


class HomepageContractTests(unittest.TestCase):
    def test_primary_navigation_matches_brand_direction(self):
        for label in ("PORTFOLIO", "ABOUT", "PRESS", "CONTACT"):
            self.assertIn(label, INDEX_HTML)

    def test_homepage_has_fullscreen_landing_hero(self):
        self.assertIn('class="landing-hero"', INDEX_HTML)
        self.assertIn("MONICA", INDEX_HTML)
        self.assertIn("hero-stage__image", INDEX_HTML)

    def test_homepage_has_editorial_support_sections(self):
        for fragment in ("Selected Stories", "About Monica", "Press Notes"):
            self.assertIn(fragment, INDEX_HTML)

    def test_styles_define_new_homepage_layout(self):
        for selector in (".landing-hero", ".hero-stage", ".story-strip", ".press-list"):
            self.assertIn(selector, STYLES_CSS)


if __name__ == "__main__":
    unittest.main()
