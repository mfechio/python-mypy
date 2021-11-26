def factorial(i: int) -> int:

    if i < 0:
        raise ValueError("Factorial not defined for negative values")

    if i == 0:
        return 1

    return i * factorial(i - 1)


# Success: no issues found in 1 source file
print(factorial(3.01))

# factorial_typed.py:4: error: Incompatible return value type (got "None", expected "int")
# factorial_typed.py:17: error:
# Argument 1 to "factorial" has incompatible type "str"; expected "int"
# Found 2 errors in 1 file (checked 1 source file)
# print(factorial('3'))

# factorial_typed.py:4: error: Incompatible return value type (got "None", expected "int")
# factorial_typed.py:22: error: A
# rgument 1 to "factorial" has incompatible type "float"; expected "int"
# Found 2 errors in 1 file (checked 1 source file)
# print(factorial(3.01))
