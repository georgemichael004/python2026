# Task: Return a function result from another function.
def make_multiplier(x):
    """Outer function that takes a factor'x'"""

    def multiplier(n):
        """Inner funtion that performs the multiplication using 'x'."""
        return n * x
    return multiplier

# Create new specific functions
double = make_multiplier(2)
triple = make_multiplier(3)

# Test
print(f"5 doubled is: {double(5)}")
print(f"5 tripled is: {triple(5)}")
