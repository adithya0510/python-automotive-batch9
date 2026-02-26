from si import simple_interest

P = int(input("Enter Principal amount: "))
R = int(input("Enter Rate of interest: "))
T = int(input("Enter Time: "))

final_result = simple_interest(P, R, T)

print("Simple Interest is:", final_result)