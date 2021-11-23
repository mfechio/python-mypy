"""
 - dynamic typing
 - type hints
 - python 3.5
 - static type checker (check code) - try to check violation on type hints or not
 - error better than when we use debugger - see list example
 - a way to document our code
 - ignored by interpreter
 - debug process
"""


def factorial(i):
    """
    3! == 3 x 2 x 1 = 6
    2! == 2 x 1 = 2
    1! == 1 == 1
    0! == 1 (by convention)
    < 0 == None
    """

    if i < 0:
        raise ValueError("Factorial not defined for negative values")

    if i == 0:
        return 1

    return i * factorial(i - 1)


# Success
print(factorial(3))

# TypeError: '<' not supported between instances of 'str' and 'int'
# print(factorial('3'))

# TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
# print(factorial(3.01))
