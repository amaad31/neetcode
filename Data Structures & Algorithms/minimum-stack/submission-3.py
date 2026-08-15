class MinStack:

    def __init__(self):
        self.min_num = float('inf')
        self.num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.num_stack.append(val)
        if val <= self.min_num:
            self.min_num = val
            self.min_stack.append(val)

    def pop(self) -> None:
        popped_num = self.num_stack.pop()
        if popped_num == self.min_stack[-1]:
            self.min_stack.pop()
            self.min_num = self.min_stack[-1] if len(self.min_stack) != 0 else float('inf')

    def top(self) -> int:
        return self.num_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
