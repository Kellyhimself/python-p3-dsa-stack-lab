class Stack:
    # A Stack is a data structure that follows the Last In First Out (LIFO) principle. This means that the last item added to the stack will be the first one to be removed.

    def __init__(self, items = [], limit = 100):
        # The constructor creates a new stack with the given limit.
        # The items parameter is a list of items that will be added to the stack initially.
        self.items = []
        # The items attribute is a list of the items in the stack.
        self.limit = limit
        # The limit attribute is the maximum number of items that the stack can hold.

        for item in items:
            # This loop iterates over the items in the items parameter.
            if(not self.full()):
                # If the stack is not full, the item is added to the stack.
                self.items.append(item)


    def isEmpty(self):
        # This method checks if the stack is empty.
        return self.items == []
        # The stack is empty if the list of items is empty.

    def push(self, item):
        # This method adds an item to the stack.
        if (not self.full()):
            # If the stack is not full, the item is added to the stack.
            self.items.append(item)
        else:
            # If the stack is full, the item is not added to the stack.
            return None

    def pop(self):
        # This method removes and returns the top item from the stack.
        if self.isEmpty():
            # If the stack is empty, there is no top item to return.
            return None
        # The top item is returned and removed from the stack.
        return self.items.pop()

    def peek(self):
        # This method returns the top item from the stack without removing it.
        return self.items[len(self.items)]
        # The top item is the last item in the list of items.

    def size(self):
        # This method returns the number of items in the stack.
        return len(self.items)
        # The number of items in the stack is the length of the list of items.

    def full(self):

        if (len(self.items) >= self.limit):
            # If the number of items in the stack is greater than or equal to the limit, the stack is full.
            return True
        # The stack is not full.
        return False

    def search(self, target):
        # This method searches for the target item in the stack.
        for i in reversed(range(len(self.items))):
            # The loop iterates over the items in the stack in reverse order.
            if self.items[i] == target:
                # If the current item is equal to the target item, the index of the item is returned.
                return len(self.items) -1  - i 
        # The target item is not found in the stack.
        return -1