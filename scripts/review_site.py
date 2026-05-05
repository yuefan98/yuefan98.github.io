from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_FILES = [
    ROOT / "index.html",
    ROOT / "script.js",
    ROOT / "styles.css",
    ROOT / "README.md",
]

REQUIRED_TEXT = [
    "impedance.py",
    "nleis.py",
    "https://nleispy.readthedocs.io/en/latest/getting-started.html",
    "Set up the environment and install nleis.py from PyPI.",
    "Define paired EIS and NLEIS circuit models using supported element pairs.",
    "mailto:yuefan26@gmail.com",
    "https://scholar.google.com/citations?user=lsf1t2AAAAAJ&hl=en&authuser=1",
    "https://www.linkedin.com/in/yuefan-ji",
    "Publisher",
    "https://iopscience.iop.org/article/10.1149/1945-7111/ae1064",
    "https://pubs.acs.org/doi/10.1021/acs.chemmater.3c03138",
    "https://www.sciencedirect.com/science/article/pii/S0008622322010867",
]

FORBIDDEN_TEXT = [
    "you@example.com",
    "Lorem ipsum",
    "generated spectra are shown",
    "Synthetic Nyquist",
    "fake data",
    "made up",
    "impedanceCanvas",
    "Prepare Python Job",
    "load_frequency_file",
    "initial_guess=[...]",
    "from nleis import",
]


def read_site_text() -> str:
    return "\n".join(path.read_text(encoding="utf-8") for path in TEXT_FILES)


def assert_ascii(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    try:
        content.encode("ascii")
    except UnicodeEncodeError as exc:
        raise AssertionError(f"{path.relative_to(ROOT)} contains non-ASCII text: {exc}") from exc


def main() -> None:
    for path in TEXT_FILES:
        if not path.exists():
            raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
        assert_ascii(path)

    site_text = read_site_text()

    for expected in REQUIRED_TEXT:
        if expected not in site_text:
            raise AssertionError(f"Missing required API/guardrail text: {expected}")

    lowered = site_text.lower()
    for forbidden in FORBIDDEN_TEXT:
        if forbidden.lower() in lowered:
            raise AssertionError(f"Forbidden placeholder or artificial-result wording: {forbidden}")

    if "<canvas" in site_text:
        raise AssertionError("Canvas visualization should remain disabled until it is implemented correctly")

    if "<pre><code" in site_text:
        raise AssertionError("Generated code snippets should not be shown for nleis.py")

    print("Site review passed: wording, API references, and artificial-result guardrails are intact.")


if __name__ == "__main__":
    main()
