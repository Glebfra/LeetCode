class MinStack:
    def __init__(self):
        self.min = 1 << 31
        self.min = []
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.min:
            val = min(self.min[-1], val)
        self.min.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.min.pop()

    def top(self) -> int:
        """
        >>> stack = MinStack()
        >>> stack.push(1)
        >>> stack.top()
        1
        """
        return self.data[-1]

    def getMin(self) -> int:
        """
        >>> stack = MinStack()
        >>> stack.push(1)
        >>> stack.push(-2)
        >>> stack.pop()
        >>> stack.getMin()
        1

        >>> stack = MinStack()
        >>> stack.push(1)
        >>> stack.push(-2)
        >>> stack.getMin()
        -2
        """
        return self.min[-1]
    

if __name__ == '__main__':
    from doctest import testmod

    testmod()
