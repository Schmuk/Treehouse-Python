# Top level functions, not inside class or another function

# 2 spaces b/t functions

# 4 spaces for indentation is recommended

# everything after a comma gets spaces

# spaces around operators not inside a function call

# no space b/t function name and parenthesis

# no spaces inside of parenthesis

# one import per line

# classes, no spaces, caps to separate words, RaceCar

# new line at end of file

# import this -> the Zen of Python


def foo_bar(arg1, arg2, arg3, arg4):
    return arg1, arg2, arg3, arg4


def bar(*args):
    # bad spacing
    return 2 + 2  # not inside function call


# Bad class name(fixed), bad spacing(fixed), bad indentation(fixed)
class Treehouse:
    def one(self):
        return 1

    def two(self):
        return 2


# bad identation and whitespace
alpha, beta, charlie, delta = foo_bar("a long string", "a longer string", "yet another long string",
                                      "and other crazy string")  # line args up, or give each arg its own line
# last parenthesis can either be with last arg or on its own line


# bad spacing (fixed)
one = 1
three = 3
fourteen = 14  # make fourteen equal to 12

print(alpha)
print(fourteen)

print(Treehouse().two())