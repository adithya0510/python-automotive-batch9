# Dictionary to store student roll number as key and full name as value
students = {
    1: "Praveen Kumar",
    2: "Pavan Adithya",
    3: "Sai Snigdha",
    4: "Abhinav Singh",
    5: "Utkarsh Mishra",
    6: "Chava Kethan",
    7: "Praveen Yadav",
    8: "Sai Urla",
    9: "Pavan Reddy",
    10: "Abhinav Verma",
    11: "Rohit Sharma",
    12: "Rahul Kumar",
    13: "Neha Singh",
    14: "Ankit Mishra",
    15: "Aman Gupta",
    16: "Sneha Patel",
    17: "Kunal Mehta",
    18: "Vikas Yadav",
    19: "Suresh Kumar",
    20: "Ravi Verma"
}

# Empty Dictionary to store first names
fn_count = {}    #first name count

# Extract and count first names
for name in students.values():
    first_name = name.split()[0]   # Get first name after splitting the full name
    if first_name in fn_count:
        fn_count[first_name] += 1
    else:
        fn_count[first_name] = 1

# Display students with same first name 
print("Students having same first name:")

for first_name, count in fn_count.items():
    if count > 1:
        print(first_name)