def guard_zero(operate):
    def inner(x, y):
        if y == 0:
            print("Cannot divide by 0.")
            return
        return operate(x, y)
    return inner


## without decorators

# def divide(x, y):
#     return x / y
# divide = guard_zero(divide)
# divide(5,0)

@guard_zero
def divide(x, y):
    return x / y

divide(5,0)