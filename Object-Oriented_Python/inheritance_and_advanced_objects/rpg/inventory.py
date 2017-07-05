class Inventory(list):
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item): # item is the thing we're looking for (coin)
        return item in self.slots # True of False
    # coin in backpack

    def __iter__(self): # makes object iterable? can iterate through it in a for loop
        yield from self.slots # read up on yield

    '''for item in self.slots:
        yield item
        
    this is what yield from does'''

