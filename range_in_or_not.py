# Function to check if a number is in a given range
def is_in_range(n, start, end):
    return start <= n <= end

# Example usage
num = float(input("Enter a number: "))
start = float(input("Enter the start of the range: "))
end = float(input("Enter the end of the range: "))

if is_in_range(num, start, end):
    print(f"{num} is in the range between {start} and {end}.")
else:
    print(f"{num} is not in the range between {start} and {end}.")
