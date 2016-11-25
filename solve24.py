class Problem:
    def __init__(self, numbers = [], allowed_operations = 'asmd', goal_number = 24, operations=[]):
        '''A 24 problem'''
        self.numbers = numbers
        self.allowed_operations = allowed_operations
        self.goal_number = 24
        self.operations = operations
        
    def __repr__(self):
        rep = ''
        rep += 'Problem ('
        for i, n in enumerate(self.numbers):
            if i != 0:
                rep += ' '
            rep += str(n)
        return rep + ') -> ' + str(self.goal_number) + ' using ' + self.allowed_operations
    
    def possible_actions(self):
        actions = []
        for x, n1 in enumerate(self.numbers):
            for y, n2 in enumerate(self.numbers):
                if x != y:
                    sub = Operation(n1, 's', n2)
                    if (sub.compute() > 0): actions.append(sub)
                    
                    div = Operation(n1, 'd', n2)
                    actions.append(div)
                    if y < x:
                        add = Operation(n1, 'a', n2)
                        actions.append(add)
                        
                        mul = Operation(n1, 'm', n2)
                        actions.append(mul)
        return actions
        
    def apply_operation(self, op):
        '''Returns a new problem, which results from applying the operation to the current instance'''
        new_numbers = list(self.numbers)
        new_numbers.remove(op.operator)
        new_numbers.remove(op.operand)
        new_num = op.compute()
        new_operations = list(self.operations)
        new_operations.append(op)
        if new_num != 0:
            new_numbers.append(new_num)
        return Problem( numbers=new_numbers, allowed_operations=self.allowed_operations, goal_number=self.goal_number, operations=new_operations )
    
    def is_goal(self):
        return self.goal_number in self.numbers
    
    def is_terminal(self):
        return len(self.numbers) == 1
        
class Operation:
    def __init__(self, operand, operation, operator):
        self.operand = operand
        self.operation = operation
        self.operator = operator
        
    def __repr__(self):
        return str(self.operand) + ' ' + self.operation_char() + ' ' + str(self.operator) + ' = ' + str(self.compute())
    
    def compute(self):
        if self.operation == 'a': return self.operand + self.operator
        elif self.operation == 's': return self.operand - self.operator
        elif self.operation == 'm': return self.operand * self.operator
        elif self.operation == 'd': return self.operand / self.operator
        return None
        
    def operation_char(self):
        if self.operation == 'a': return '+'
        elif self.operation == 's': return '-'
        elif self.operation == 'm': return '*'
        elif self.operation == 'd': return '/'
        return '?'
    
    
def solveProblem(p):
    if p.is_goal():
        for op in p.operations:
            print(op)
    if p.is_terminal():
        return False
    for act in p.possible_actions():
        if solveProblem(p.apply_operation(act)):
            return True
        
p = Problem( numbers = [5,6,7,8] )
print(p)
solveProblem(p)