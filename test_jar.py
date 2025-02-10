import pytest
from jar import Jar

def test_init():
    """Test that an invalid capacity raises a ValueError."""
    with pytest.raises(ValueError):
        Jar(-1)  # Capacity cannot be negative

def test_str():
    """Test the string representation of the jar."""
    jar = Jar()
    assert str(jar) == ""  # Empty jar should return an empty string

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # Max capacity

def test_deposit():
    """Test adding cookies to the jar."""
    jar = Jar(5)  # Jar with a capacity of 5

    jar.deposit(3)
    assert jar.size == 3  # Check if 3 cookies were added

    jar.deposit(2)
    assert jar.size == 5  # Should be full now

    with pytest.raises(ValueError):  # Should raise an error for overfilling
        jar.deposit(1)

def test_withdraw():
    """Test removing cookies from the jar."""
    jar = Jar(5)
    jar.deposit(5)  # Fill jar

    jar.withdraw(2)
    assert jar.size == 3  # Should have 3 cookies left

    jar.withdraw(3)
    assert jar.size == 0  # Should be empty

    with pytest.raises(ValueError):  # Can't withdraw from empty jar
        jar.withdraw(1)
