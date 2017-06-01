class ReversedStr(str):
    def __new__(*args, **kwargs): # creates the object?
        self = str.__new__(*args, **kwargs) # self is just a variable name here
        self = self[::-1]
        return self # new has a return statement

# new does not take self and is a class method (method that operates on a class not instance)