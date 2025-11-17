class Employee:
    def __init__(self, name: str, salary: float):
        # Using protected attributes (single underscore) for encapsulation
        self._name = name
        self._salary = salary

    def increase_salary(self, percentage: float):
        if percentage < 0:
            print("Error: Salary increase percentage must be non-negative.")
            return
        raise_amount = self._salary * (percentage / 100.0)
        self._salary += raise_amount
        print(f"{self._name}'s salary increased by {percentage:.2f}% (+\${raise_amount:,.2f}).")

    def display_info(self):
        print("-" * 30)
        print(f"Employee: {self._name}")
        print(f"Salary:   \${self._salary:,.2f}") # Formatted with comma separators
        print("-" * 30)
    # Optional: Getter methods for controlled access to protected attributes
    def get_name(self) -> str:
        """Returns the employee's name."""
        return self._name
    def get_salary(self) -> float:
        """Returns the employee's current salary."""
        return self._salary
# --- Example Usage ---
# 1. Create an employee object
employee1 = Employee(name="Alice Johnson", salary=60000.00)

# 2. Display initial information
print("--- Initial State ---")
employee1.display_info()

# 3. Apply a salary increase
print("\n--- Applying a Raise ---")
employee1.increase_salary(percentage=7.5)

# 4. Display updated information
print("\n--- Updated State ---")
employee1.display_info()
# 5. Accessing information using getters
print(f"\nAccessing Name via Getter: {employee1.get_name()}")
