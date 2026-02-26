# ---------------- Base Class ----------------
class BusinessUtility:
    # Method to calculate regular profit margin
    def calculate_margin(self, revenue, cost):
        # Formula:
        # Regular Margin = ((Revenue - Cost) / Revenue) * 100

        # Check to avoid division by zero
        if revenue == 0:
            return 0.0

        # Calculate and return regular margin
        return ((revenue - cost) / revenue) * 100


# ---------------- Derived Class ----------------
# Inherits from BusinessUtility
class SeasonalBusinessUtility(BusinessUtility):

    # Overriding the calculate_margin() method
    def calculate_margin(self, revenue, cost):
        # Call the base class method to get regular margin
        regular_margin = super().calculate_margin(revenue, cost)

        # Add seasonal adjustment of 10%
        seasonal_margin = regular_margin + 10

        # Return seasonal margin
        return seasonal_margin


# ---------------- Profitability Checker Class ----------------
class ProfitabilityChecker:

    # Method to check if business is profitable
    def check_profitability(self, regular_margin):
        # Business is profitable if margin is 10% or more
        if regular_margin >= 10:
            print("Business is profitable.")
        else:
            print("Business is not profitable.")


# ---------------- Main Program ----------------

# Read revenue input from user
revenue = float(input())

# Read cost input from user
cost = float(input())

# Create objects of each class
business = BusinessUtility()                 # Base class object
seasonal_business = SeasonalBusinessUtility()  # Derived class object
checker = ProfitabilityChecker()             # Profitability checker object

# Calculate regular margin using base class
regular_margin = business.calculate_margin(revenue, cost)

# Calculate seasonal margin using derived class
seasonal_margin = seasonal_business.calculate_margin(revenue, cost)

# Display the margins formatted to 2 decimal places
print(f"Regular Margin: {regular_margin:.2f}%")
print(f"Seasonal Margin: {seasonal_margin:.2f}%")

# Check and display profitability status
checker.check_profitability(regular_margin)
