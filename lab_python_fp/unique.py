class Unique:
    def __init__(self, items, ignore_case = False):
        self.items = []
        if ignore_case:                 #items = [item.lower() if type(item) == str else item for item in items]
            arr = []
            for item in items:
                if (type(item) == str and item.lower() not in arr):
                    self.items.append(item)
                    arr.append(item.lower())
                elif (type(item) != str and item not in self.items):
                    self.items.append(item)
        else:
            for item in items: 
                if (item not in self.items): self.items.append(item)
    
    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            self.items.remove(item)
            return item
        raise StopIteration

if __name__ == "__main__":
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    data = ["A", "A", 2, 455,"a", "a"]
    for item in Unique(data):
        print(item)
    data = [1, 1, 2, 2, 3, 3]
    for item in Unique(data):
        print(item)

