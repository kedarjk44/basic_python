from Stack import Stack


class StackInheritance(Stack.Stack):
    class_var = 1

    def __init__(self):
        super(StackInheritance, self).__init__()
        self.sum = 0

    def push(self, elm):
        self.sum += elm
        Stack.Stack.push(self, elm)

    def pop(self):
        elm = Stack.Stack.pop(self)
        self.sum -= elm
        return elm

    def get_sum(self):
        return self.sum


new_stack = StackInheritance()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
print(new_stack.get_sum())
new_stack.pop()
new_stack.pop()
print(new_stack.get_sum())

print(issubclass(StackInheritance, Stack.Stack))
print(issubclass(StackInheritance, StackInheritance))

print(hasattr(new_stack, 'sum'))
print(hasattr(new_stack, 'class_var'))
print(hasattr(StackInheritance, 'sum'))
print(hasattr(StackInheritance, 'class_var'))