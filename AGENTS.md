# fare-calc

Computes transit fares from zones crossed, rider category and time of day.

This repository has adopted the tradecraft practice. Its work configuration is `.tradecraft/work.json`.

## Code Review Rules

Review pull requests only when they are marked ready; skip drafts. Post only P0/P1 findings a consumer would act on wrongly. Name the wrong action, not the wording. Where this repository's own convention contradicts a general rule, the convention wins and the comment says so. A deletion is as good a finding as an addition.

## Checks

Run `python -m unittest discover -s tests -v` before pushing.
