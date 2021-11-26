def factorial(i: int) -> int:

    if i < 0:
        raise ValueError("Factorial not defined for negative values")

    if i == 0:
        return 1

    return i * factorial(i - 1)


# Success: no issues found in 1 source file
# print(factorial(3))

# Argument 1 to "factorial" has incompatible type "str"; expected "int"
# print(factorial('3'))

# Argument 1 to "factorial" has incompatible type "float"; expected "int"
print(factorial(3.01))
