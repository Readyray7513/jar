class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = capacity
        self._size = 0 # Start with 12

    def __str__(self):
        return "🍪" * self._size  # Represents the cookies visually

    def deposit(self, n):
        """Add `n` cookies to the jar."""
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in the jar!")
        self._size += n

    def withdraw(self, n):
        """Remove `n` cookies from the jar."""
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self._size - n < 0:
            raise ValueError("Not enough cookies to withdraw!")
        self._size -= n

    @property
    def size(self):
        """Returns the current number of cookies in the jar."""
        return self._size

    @property
    def capacity(self):
        """Returns the jar's total capacity."""
        return self._capacity


    
        