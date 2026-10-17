class DynamicArray:
    
    def __init__(self, capacity: int):
        self.values = [None] * capacity

    def get(self, i: int) -> int:
        return self.values[i]

    def set(self, i: int, n: int) -> None:
        self.values[i] = n

    def pushback(self, n: int) -> None:
        currSize = self.getSize()
        if currSize == self.getCapacity():
            self.resize()
        
        self.values[currSize] = n

    def popback(self) -> int:
        currSize = self.getSize()

        # we predict this if statement to be run
        # many times in real test cases.
        # therefore we pre-calculate the current size.
        if currSize == 0:
            return None

        back = self.values[currSize - 1]
        self.values[currSize - 1] = None
        return back

    def resize(self) -> None:
        self.values = self.values + [None] * self.getCapacity()

    def getSize(self) -> int:
        cap = self.getCapacity()

        # loop backward from end of the array
        # until we meet a non-null element.
        for i in range(-1, -cap-1, -1):
            if self.values[i] != None:
                return (cap + i) + 1
        
        # if there is not any non-null element,
        # then the current size of the array is 0.
        return 0
    
    def getCapacity(self) -> int:
        return len(self.values)