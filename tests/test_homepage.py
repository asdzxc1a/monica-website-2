from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = (ROOT / "index.html").read_text(encoding="utf-8")
STYLES_CSS = (ROOT / "styles.css").read_text(encoding="utf-8")
APP_JS = (ROOT / "app.js").read_text(encoding="utf-8") if (ROOT / "app.js").exists() else ""


class HomepageContractTests(unittest.TestCase):
    def test_primary_navigation_matches_brand_direction(self):
        for label in ("PORTFOLIO", "PRESS", "CONTACT"):
            self.assertIn(label, INDEX_HTML)

        self.assertNotIn(">ABOUT<", INDEX_HTML)
        self.assertNotIn('<button class="menu-button" type="button" aria-label="Open menu">\n            <span></span>', INDEX_HTML)
        self.assertNotIn(".menu-button span", STYLES_CSS)

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

    def test_featured_work_mobile_reduces_copy_density(self):
        for fragment in (
            "A darker editorial study of Monica in motion, poise, and transformation.",
            "Denim",
            "Tulle",
            "Tailoring",
            "Couture",
        ):
            self.assertIn(fragment, INDEX_HTML)

        for selector in (
            ".featured-spread__tags",
            ".featured-spread__tag",
        ):
            self.assertIn(selector, STYLES_CSS)

        for fragment in ("Read Editor's Letter", "View Wardrobe Notes"):
            self.assertNotIn(fragment, INDEX_HTML)

        for selector in (".featured-spread__details", ".featured-spread__detail"):
            self.assertNotIn(selector, STYLES_CSS)

    def test_homepage_retains_supporting_editorial_sections(self):
        for fragment in ("Dior 2026", "Breakfast Stories", "Book A Session"):
            self.assertIn(fragment, INDEX_HTML)

        self.assertNotIn("About Monica", INDEX_HTML)

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
            "Contact &amp; Bookings",
            "Get In",
            "Touch",
            "With Me",
            "Get In Touch With Me",
            "hello@monicastudio.art",
            "+377 6 43 91 37 95",
            "https://www.instagram.com/monicastyle.mc/",
            "Follow Monica on Instagram",
            "Instagram",
            "Monaco",
        ):
            self.assertIn(fragment, INDEX_HTML)

        self.assertNotIn('src="./finale-reference.png"', INDEX_HTML)
        self.assertNotIn('src="./finale-crown.jpg"', INDEX_HTML)

    def test_styles_define_featured_portfolio_layout(self):
        for selector in (
            ".featured-spread",
            ".featured-spread__editorial",
            ".featured-spread__hero",
            ".featured-spread__aside",
            ".featured-spread__strip",
        ):
            self.assertIn(selector, STYLES_CSS)

    def test_desktop_featured_aside_reads_as_editorial_story(self):
        for fragment in (
            "Look Study 01",
            "Soft Rebellion",
            "Lavender texture, dark lens, colder posture.",
            "Blue Room Couture",
        ):
            self.assertIn(fragment, INDEX_HTML)

        for selector in (
            ".featured-spread__aside-editorial",
            ".featured-spread__aside-heading",
            ".featured-spread__aside-note",
            ".featured-spread__aside-stage",
            ".featured-spread__aside-inset",
            "\"lead hero aside\"",
        ):
            self.assertIn(selector, STYLES_CSS)

    def test_finale_section_has_couture_motion_hooks(self):
        self.assertIn("./app.js", INDEX_HTML)

        for selector in (
            ".motion-ready .finale-chapter__hero-image",
            ".finale-chapter--active .finale-chapter__hero-image",
            ".finale-chapter__title-script::after",
            "@keyframes couture-shimmer",
        ):
            self.assertIn(selector, STYLES_CSS)

        for fragment in (
            "IntersectionObserver",
            "finale-chapter--active",
            "--finale-shift",
            "--finale-tilt",
        ):
            self.assertIn(fragment, APP_JS)

    def test_finale_section_has_mobile_editorial_rules(self):
        for fragment in (
            "scroll-snap-type: x mandatory",
            "grid-template-areas:",
            "\"copy copy\"",
            "grid-auto-columns: 82vw",
            "scroll-snap-align: center",
            ".finale-chapter__ghost {\n    display: none;",
            "grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);",
            "min-height: min(38rem, calc(100svh - 1.25rem));",
            ".finale-chapter__redwall {\n    display: block;",
            ".finale-chapter__redwall img {\n    width: 100%;",
        ):
            self.assertIn(fragment, STYLES_CSS)


if __name__ == "__main__":
    unittest.main()
