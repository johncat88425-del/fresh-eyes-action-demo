# Fresh Eyes GitHub Action: real CI execution

[![Working README](https://github.com/johncat88425-del/fresh-eyes-action-demo/actions/workflows/working.yml/badge.svg)](https://github.com/johncat88425-del/fresh-eyes-action-demo/actions/workflows/working.yml)
[![Broken README — expected failure](https://github.com/johncat88425-del/fresh-eyes-action-demo/actions/workflows/broken.yml/badge.svg)](https://github.com/johncat88425-del/fresh-eyes-action-demo/actions/workflows/broken.yml)

**These are two team-written engineering fixtures, not two additional real-world AI repairs.** The runs are real; the example fault is deliberate. The red workflow is the expected result of detecting that fault, not an infrastructure outage. No model or repair runs here.

This repository shows the [Fresh Eyes](https://github.com/johncat88425-del/fresh-eyes) README check on two copies
of the same tiny CLI, `shout`, which prints a text file in capitals.

| Folder | What its README says | Expected result |
|---|---|---|
| [`good/`](good/README.md) | `pip install .` then `shout --help` | ✅ installs and starts |
| [`broken/`](broken/README.md) | `pip install -r requirements.txt` then `shout --help` | ❌ the `shout` command is never created |

The `broken/` README makes a real-world mistake: installing only the requirements file never installs the package,
so the command its next line uses doesn't exist. Fresh Eyes found exactly this in a real project's README.

Open the **Actions** tab to see each run and its plain-language summary. Every run happens in a fresh, non-root
container that can reach only PyPI; no AI model is called and no key is used. A start-up check shows that the
documented commands install and start the program, not that its output is correct.

## Use it in your own repository

```yaml
# .github/workflows/readme.yml
name: README still works
on: [push, pull_request]
jobs:
  fresh-eyes:
    runs-on: ubuntu-24.04-arm
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: johncat88425-del/fresh-eyes@dfcac778f241dc598aea1fe2597d7a254d7154ee
```

Your README needs one `pip install` command and one `--help` or `--version` command in code blocks.

The Action is pinned to commit `dfcac778f241dc598aea1fe2597d7a254d7154ee`. Its reports distinguish startup checks from functional correctness. Open either badge, then its job summary for the actual commands, exit codes and environment. The report artifact expires after 14 days; the workflow history and summaries remain the primary demo links.
