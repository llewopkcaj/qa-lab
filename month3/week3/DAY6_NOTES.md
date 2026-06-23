# Month 3 · Week 3 · Day 6 — CI Artifact Verification

## What I Verified
- Modified the workflow in selenium.yml to run pytest for month3/week3 only
- GitHub Actions ran Selenium tests headlessly on ubuntu-latest.
- pytest-html report was generated and uploaded as the `selenium-report` artifact.
- I downloaded the artifact ZIP and opened the HTML report locally.
- The report shows the expected results and attatchments.

## Notes
- The artifact path issue is fixed by updating the upload-artifact path.
- The CI run now reliably produces a readable HTML report I can share as QA evidence.
