class Character:
    def __init__(self, name='', **kwargs): # made name keyword arg and provided default value
        if not name:
            raise ValueError("'name' is required")
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self): # use magic methods on base class
        return '{}: {}'.format(self.__class__.__name__, self.name)