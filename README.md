# # Cookie Jar Class

## Overview
This Python class `Jar` simulates a cookie jar that can store cookies up to a specified capacity. It allows adding and removing cookies while ensuring the jar does not exceed its limits.

## Features
- Set a maximum capacity for cookies.
- Add (`deposit`) and remove (`withdraw`) cookies with proper error handling.
- Display the current cookies in the jar using emoji representation.
- Prevents invalid operations like withdrawing more cookies than available or exceeding capacity.

## Usage

### Creating a Jar
jar = Jar(10)  # Creates a jar with a capacity of 10 cookies
If no capacity is specified, it defaults to 12.

### Adding Cookies
jar.deposit(5)  # Adds 5 cookies to the jar
Raises an error if the total exceeds capacity.

### Removing Cookies
jar.withdraw(3)  # Removes 3 cookies from the jar
Raises an error if there aren’t enough cookies.

### Checking Current Status
print(jar)       # Displays cookies visually, e.g., "🍪🍪🍪🍪🍪"
print(jar.size)  # Returns the number of cookies in the jar
print(jar.capacity)  # Returns the jar's total capacity

## Error Handling
- `ValueError` is raised for:
  - Negative deposits or withdrawals.
  - Depositing beyond the jar's capacity.
  - Withdrawing more cookies than available.

## Example
jar = Jar(5)
jar.deposit(3)
print(jar)  # 🍪🍪🍪
jar.withdraw(1)
print(jar)  # 🍪🍪

## License
This script is open-source and free to use or modify.
