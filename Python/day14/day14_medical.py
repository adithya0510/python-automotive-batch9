import xml.etree.ElementTree as ET

# -----------------------------
# XML DATA (embedded)
# -----------------------------
MEDICAL_XML = """
<medical>
    <problem>migraine</problem>
    <problem>sinus</problem>
    <problem>thyroid</problem>
</medical>
"""

# -----------------------------
# BUSINESS LOGIC
# -----------------------------
def get_medical_problems_sorted():
    """
    Parse XML data and return medical problems in alphabetical order
    """
    root = ET.fromstring(MEDICAL_XML)

    medical_problems = []

    for problem in root.iter("problem"):
        medical_problems.append(problem.text.strip())

    medical_problems.sort()
    return medical_problems


# -----------------------------
# PYTEST TEST CASE
# -----------------------------
def test_medical_problems_sorted():
    result = get_medical_problems_sorted()

    expected = [
        "migraine",
        "sinus",
        "thyroid"
    ]

    assert result == expected
