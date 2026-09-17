
def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def main():
    first = float(input("First number: "))
    second = float(input("Second number: "))

    result = add(first, second)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
