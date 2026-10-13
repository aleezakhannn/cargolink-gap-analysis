import pandas as pd
from gap_analysis import find_gaps, rate_priority


def make_assets():
    return pd.DataFrame(
        {
            "Asset ID": ["AST-001", "AST-002"],
            "Name": ["Terminal", "Server"],
            "Sensitivity": ["Low", "High"],
        }
    )


def make_controls():
    return pd.DataFrame(
        {
            "Control ID": ["A.1", "A.2", "A.3"],
            "Control Title": ["One", "Two", "Three"],
            "Status": ["Implemented", "Partial", "Missing"],
            "Related Asset ID": ["AST-001", "AST-001", "AST-002"],
        }
    )


def test_implemented_controls_are_not_gaps():
    gaps = find_gaps(make_assets(), make_controls())
    assert "A.1" not in gaps["Control ID"].values


def test_partial_and_missing_are_gaps():
    gaps = find_gaps(make_assets(), make_controls())
    assert len(gaps) == 2
    assert set(gaps["Control ID"]) == {"A.2", "A.3"}


def test_gap_is_joined_to_asset():
    gaps = find_gaps(make_assets(), make_controls())
    row = gaps[gaps["Control ID"] == "A.3"].iloc[0]
    assert row["Name"] == "Server"


def test_priority_high_for_missing_on_high_sensitivity():
    row = {"Sensitivity": "High", "Status": "Missing"}
    assert rate_priority(row) == "High"


def test_priority_medium_for_partial_on_high_sensitivity():
    row = {"Sensitivity": "High", "Status": "Partial"}
    assert rate_priority(row) == "Medium"


def test_priority_low_for_partial_on_low_sensitivity():
    row = {"Sensitivity": "Low", "Status": "Partial"}
    assert rate_priority(row) == "Low"