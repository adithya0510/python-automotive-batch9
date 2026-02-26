from day14_medical_problems import get_medical_problems_sorted

def test_medical_problems_sorted():
    xml_path = r"C:\Users\BOBBY\Documents\GitHub\python-automotive-batch9\Python\day14\day14_medical.xml"

    result = get_medical_problems_sorted(xml_path)

    expected = [
        "Allergy",
        "Fracture",
        "Migraine",
        "Sinus",
        "Thyroid"
    ]

    assert result == expected
 