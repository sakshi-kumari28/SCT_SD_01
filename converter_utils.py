def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    
    from_unit, to_unit = from_unit.upper(), to_unit.upper()

    if from_unit == to_unit:
        return value

    # Celsius-based conversions
    if from_unit == "C":
        if to_unit == "F":
            return celsius_to_fahrenheit(value)
        elif to_unit == "K":
            return celsius_to_kelvin(value)

    # Fahrenheit-based conversions
    elif from_unit == "F":
        if to_unit == "C":
            return fahrenheit_to_celsius(value)
        elif to_unit == "K":
            return fahrenheit_to_kelvin(value)

    # Kelvin-based conversions
    elif from_unit == "K":
        if to_unit == "C":
            return kelvin_to_celsius(value)
        elif to_unit == "F":
            return kelvin_to_fahrenheit(value)

    # Invalid unit
    raise ValueError("Invalid temperature unit. Use C, F, or K.")
