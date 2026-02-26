import xml.etree.ElementTree as ET

def get_medical_problems_sorted(xml_path):
    
    tree = ET.parse(xml_path)
    root = tree.getroot()

    medical_problems = []

    for problem in root.iter("problem"):
        if problem.text:
            medical_problems.append(problem.text.strip())

    medical_problems.sort()
    return medical_problems
