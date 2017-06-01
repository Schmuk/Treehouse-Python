class Double(int):
    def __new__(*args, **kwargs): # creates new instance from whatever is passed in
        self = int.__new__(*args, **kwargs)
        return self * 2