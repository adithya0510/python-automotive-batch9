import random

managers = ['a', 'b', 'c']

employees = [f"e{i}" for i in range(1, 13)]   #list comprehension

reports = 4

# This changes the order of employees but keeps all employees unique
random.shuffle(employees)

manager_employee_report = {

    # managers[i] becomes the key (manager name)
    managers[i]: list(
        filter(
            lambda emp: True,
            employees[i * reports:(i + 1) * reports]
            # i = 0 → employees[0:4]
            # i = 1 → employees[4:8]
            # i = 2 → employees[8:12]
        )
    )

    for i in range(len(managers))
}

# Import pprint to display dictionary in a readable, multi-line format
from pprint import pprint

pprint(manager_employee_report)
