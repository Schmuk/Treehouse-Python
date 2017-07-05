import copy
class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__() # ignores everything passed in ? now we have an empty list instance stored inside self

        for _ in range(count):
            self.append(copy.copy(value))
            '''append copy of value given.  If something is sent is in mutable, another list,
            each member in our filled list that was a copy of that list would be the same member
            if we weren't using copy.copy, if we changed one of them it would change all of them,
            we are just putting in references to that list. With copy.copy were not getting references, 
            we are getting brand new versions of that list'''

            '''
            >>> import filledlist
            >>> fl = filledlist.FilledList(9, 2)
            >>> len(fl)
            9
            >>> fl
            [2, 2, 2, 2, 2, 2, 2, 2, 2]
            >>> fl2 = filledlist.FilledList(2, [1, 2, 3])
            >>> fl2
            [[1, 2, 3], [1, 2, 3]]
            >>> fl2[0][1] = 5
            >>> fl2
            [[1, 5, 3], [1, 2, 3]]
            >>>           
            '''