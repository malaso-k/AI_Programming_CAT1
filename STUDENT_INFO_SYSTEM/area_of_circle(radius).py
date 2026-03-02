# functions_task.py
from math import pi

def area_of_circle(radius, verbose=False):
    """Return area rounded to 2 decimals. If verbose, print calculation steps."""
    if radius <= 0:
        raise ValueError("Radius must be greater than 0.")
    raw_area = pi * radius ** 2
    rounded_area = round(raw_area, 2)
    if verbose:
        print(f"Formula: area = pi * radius^2")
        print(f"Substitute: area = {pi} * {radius}^2")
        print(f"Raw area: {raw_area}")
        print(f"Rounded area (2 decimals): {rounded_area}")
    return rounded_area

if __name__ == "__main__":
    try:
        r_input = input("Enter the radius: ").strip()
        radius = float(r_input)
    except ValueError:
        print("Invalid input - please enter a numeric value for radius.")
    else:
        try:
            area = area_of_circle(radius, verbose=True)
        except ValueError as exc:
            print(exc)
        else:
            print(f"\nFinal result: Area for radius {radius} is {area}")
