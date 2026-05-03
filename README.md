# Yuefan Ji GitHub Pages Site

Static personal website for `yuefan98.github.io`.

## Scope

- Present Yuefan Ji's research, software, publications, and links.
- Keep the visual treatment clean and Apple-inspired.
- Keep unfinished EIS/NLEIS browser-interface and visualization concepts disabled until they are implemented correctly.
- Do not show synthetic spectra, browser-generated fits, artificial analysis results, or generated code snippets.

## Scientific Software Guardrails

The software section should point users to the official nleis.py documentation rather than presenting locally generated snippets. The current workflow reference is:

- https://nleispy.readthedocs.io/en/latest/getting-started.html

JavaScript may update navigation and page metadata. It must not calculate, display, or imply browser-side EIS/NLEIS spectra, fits, or analysis results.

## Local Checks

Run the same checks used by GitHub Actions:

```bash
node --check script.js
python3 scripts/review_site.py
```

## Deploy

Changes should be reviewed through a pull request before merging to the GitHub Pages branch.
