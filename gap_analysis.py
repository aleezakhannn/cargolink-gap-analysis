import pandas as pd


def load_data(assets_path="assets.csv", controls_path="control_mapping.csv"):
    assets = pd.read_csv(assets_path)
    controls = pd.read_csv(controls_path)
    return assets, controls


def find_gaps(assets, controls):
    """Return controls whose status is Partial or Missing,
    joined with the asset they relate to."""
    gaps = controls[controls["Status"].isin(["Partial", "Missing"])]
    merged = gaps.merge(
        assets,
        left_on="Related Asset ID",
        right_on="Asset ID",
        how="left",
    )
    merged["Priority"] = merged.apply(rate_priority, axis=1)
    return merged


def rate_priority(row):
    """High if the asset is High sensitivity and the control is Missing."""
    if row["Sensitivity"] == "High" and row["Status"] == "Missing":
        return "High"
    if row["Sensitivity"] == "High" or row["Status"] == "Missing":
        return "Medium"
    return "Low"

def write_report(controls, gaps, path="gap_analysis_report.md"):
    implemented = controls[controls["Status"] == "Implemented"]
    lines = [
        "# CargoLink ISO 27001 Gap Analysis Report",
        "",
        "This report compares CargoLink's current controls against ISO 27001:2022 "
        "Annex A. All data comes from the local lab environment (sample data only).",
        "",
        "## Summary",
        "",
        f"- Controls reviewed: {len(controls)}",
        f"- Implemented: {len(implemented)}",
        f"- Gaps found (Partial or Missing): {len(gaps)}",
        f"- High priority gaps: {len(gaps[gaps['Priority'] == 'High'])}",
        "",
        "## Control Status",
        "",
        "| Control ID | Control Title | Status |",
        "|---|---|---|",
    ]
    for _, r in controls.iterrows():
        lines.append(f"| {r['Control ID']} | {r['Control Title']} | {r['Status']} |")

    lines += [
        "",
        "## Identified Gaps",
        "",
        "| # | Control ID | Control Title | Status | Asset | Sensitivity | Priority | Current State |",
        "|---|---|---|---|---|---|---|---|",
    ]
    ordered = gaps.sort_values(
        "Priority", key=lambda s: s.map({"High": 0, "Medium": 1, "Low": 2})
    )
    for i, (_, r) in enumerate(ordered.iterrows(), start=1):
        lines.append(
            f"| {i} | {r['Control ID']} | {r['Control Title']} | {r['Status']} | "
            f"{r['Name']} | {r['Sensitivity']} | {r['Priority']} | {r['Current State']} |"
        )

    lines += ["", "## Evidence", "", "Screenshots are in the `evidence` folder:", ""]
    lines += [
        "- `evidence/script-output.png` - script run showing gaps found",
        "- `evidence/tests-passed.png` - unit tests passing",
        "",
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def main():
    assets, controls = load_data()
    gaps = find_gaps(assets, controls)

    print(f"Total controls reviewed: {len(controls)}")
    print(f"Gaps found: {len(gaps)}\n")
    print(
        gaps[
            ["Control ID", "Control Title", "Status", "Name", "Sensitivity", "Priority"]
        ].to_string(index=False)
    )

    gaps.to_csv("gaps_output.csv", index=False)
    print("\nSaved gaps_output.csv")
    write_report(controls, gaps)
    print("Saved gap_analysis_report.md")


if __name__ == "__main__":
    main()