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

    @classmethod # provide an alternate constructor
    def from_string(cls, input_string):
        split_input = input_string.split('-')
        new_pattern = []
        for blip in split_input:
            if blip == 'dot':
                new_pattern.append('.')
            else:
                new_pattern.append('_')
        return cls(new_pattern)



class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

my_pattern = Letter.from_string('dot-dot')
print(str(my_pattern))