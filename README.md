# CargoLink ISO 27001 Gap Analysis

A small Python project that compares CargoLink's current security controls against ISO 27001:2022 Annex A and produces a gap analysis report. It uses sample lab data only. Nothing here touches real systems.

## What's Inside

- `assets.csv` - sample CargoLink IT assets (from the Docker lab)
- `control_mapping.csv` - 15 Annex A controls with status (Implemented, Partial, Missing)
- `gap_analysis.py` - reads both CSVs, finds the gaps, rates their priority and writes the report
- `test_gap_analysis.py` - unit tests for the script
- `gap_analysis_report.md` - the generated report (12 gaps)
- `gaps_output.csv` - the gaps as a CSV
- `evidence/` - screenshots of the script run and the passing tests

## How to Run

Install the dependencies:

```
pip install pandas pytest
```

Run the analysis:

```
python gap_analysis.py
```

Run the tests:

```
python -m pytest -v
```

## How Gaps Are Found

A control counts as a gap if its status is Partial or Missing. Each gap is joined to its related asset and given a priority:

- High: the asset is High sensitivity and the control is Missing
- Medium: the asset is High sensitivity, or the control is Missing
- Low: everything else

## Assumptions

The "Current State" notes in `control_mapping.csv` are sample assumptions about CargoLink, written for this lab exercise.

## Results

- 15 controls reviewed, 3 implemented, 12 gaps found
- Full details are in [gap_analysis_report.md](./gap_analysis_report.md)
- Screenshots of the script run and passing tests are in the [evidence](./evidence) folder

## Limitations

- The control statuses are sample assumptions, not a real audit of CargoLink
- Only 15 of the 93 Annex A controls are covered
