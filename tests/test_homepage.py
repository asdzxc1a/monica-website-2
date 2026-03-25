from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = (ROOT / "index.html").read_text(encoding="utf-8")
STYLES_CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


class HomepageContractTests(unittest.TestCase):
    def test_primary_navigation_matches_brand_direction(self):
        for label in ("PORTFOLIO", "ABOUT", "PRESS", "CONTACT"):
            self.assertIn(label, INDEX_HTML)

    def test_featured_work_section_uses_all_compress_assets(self):
        for asset in (
            "./Compress/_P9A0019.jpg",
            "./Compress/_P9A0116.jpg",
            "./Compress/_P9A0301.jpg",
            "./Compress/_P9A0671копія.jpg",
            "./Compress/_P9A0687копія.jpg",
            "./Compress/_P9A0746копія.jpg",
            "./Compress/_P9A0852копія.jpg",
            "./Compress/_P9A0908копія.jpg",
        ):
            self.assertIn(asset, INDEX_HTML)

    def test_featured_work_section_frames_style_range(self):
        for fragment in (
            "Portfolio Study",
            "Editor's Letter",
            "Cover Presence",
            "Wardrobe Notes",
            "Look Ledger",
            "Soft Rebellion",
        ):
            self.assertIn(fragment, INDEX_HTML)

    def test_homepage_retains_supporting_editorial_sections(self):
        for fragment in ("Dior 2026", "Breakfast Stories", "About Monica", "Book A Session"):
            self.assertIn(fragment, INDEX_HTML)

    def test_finale_section_uses_separate_source_images(self):
        for asset in (
            "./finale-scream.jpg",
            "./finale-bite.jpg",
            "./finale-pearls.jpg",
            "./finale-boxing.jpg",
            "./finale-swing.jpg",
            "./finale-boxes.jpg",
            "./finale-redwall.jpg",
        ):
            self.assertIn(asset, INDEX_HTML)

        for fragment in (
            "The Final Chapter",
            "Little Icon",
            "Collection",
            "Grace",
            "with",
            "Grit",
            "View The Full Portfolio",
        ):
            self.assertIn(fragment, INDEX_HTML)

        self.assertNotIn('src="./finale-reference.png"', INDEX_HTML)

    def test_styles_define_featured_portfolio_layout(self):
        for selector in (
            ".featured-spread",
            ".featured-spread__editorial",
            ".featured-spread__hero",
            ".featured-spread__aside",
            ".featured-spread__strip",
        ):
            self.assertIn(selector, STYLES_CSS)


if __name__ == "__main__":
    unittest.main()
