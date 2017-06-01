class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse_list_words = []
        for item in self.pattern:
            if item == '.':
                morse_list_words.append('dot')
            else:
                morse_list_words.append('dash')
        return '-'.join(morse_list_words)

    def __iter__(self):
        yield from self.pattern # similar to self.slots from inventory


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

my_pattern = Letter(['.', '_', '.'])
print(str(my_pattern))