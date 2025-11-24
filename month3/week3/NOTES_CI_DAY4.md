# Day 4 – CI Pipeline for Selenium (Month 3, Week 3)

## What I accomplished:
- Set up a GitHub Actions workflow for Selenium tests.
- Installed Chrome + Chromedriver on the GitHub Ubuntu runner.
- Ran tests headlessly in CI.
- Added markers to failing and flaky tests to make the whole CL pipeline work.
- Generated and downloaded an artifact report.

## What I learned:
- YAML provides instructions for 
- CI runs remote Linux machines, not my laptop.
- pytest-html artifacts upload only if the file exists (so use `if: always()`).
- Flaky external websites should be skipped in CI.
- Expected failures (`xfail`) and skips ('skipif') help stabilize the pipeline.

## Next steps:
- Add screenshots-on-failure to CI reports.
- Optional: Add GitHub Secrets for real login flows.
- Optional: Run the entire suite in CI once stabilized.
