from dataclasses import dataclass

@dataclass
class BinaryTreeNodeBase:
    left: any = None
    right: any = None

class BinaryOperatorBase(BinaryTreeNodeBase):
    op = lambda self, x, y: x
    op_char = '_'
    def simplify(self):
        return self
    def exec(self):
        left = self.left.exec() if isinstance(self.left, BinaryOperatorBase) else self.left
        right = self.right.exec() if isinstance(self.right, BinaryOperatorBase) else self.right
        if isinstance(left, Const) and isinstance(right, Const):
            return Const(self.op(left.val, right.val))
        return type(self)(left, right).simplify()
    def __repr__(self):
        return f'({self.left} {self.op_char} {self.right})'

class Plus(BinaryOperatorBase):
    op = lambda self, x, y: x + y
    op_char = '+'
    def simplify(self):
        if isinstance(self.left, Const) and self.left.val == 0:
            return self.right
        elif isinstance(self.right, Const) and self.right.val == 0:
            return self.left
        return self

class Minus(BinaryOperatorBase):
    op = lambda self, x, y: x - y
    op_char = '-'
    def simplify(self):
        if isinstance(self.right, Const) and self.right.val == 0:
            return self.left
        return self

class Times(BinaryOperatorBase):
    op = lambda self, x, y: x * y
    op_char = '*'
    def simplify(self):
        if isinstance(self.left, Const):
            if self.left.val == 0:
                return Const(0)
            elif self.left.val == 1:
                return self.right
        elif isinstance(self.right, Const):
            if self.right.val == 0:
                return Const(0)
            elif self.left.val == 1:
                return self.left
        return self

class Divide(BinaryOperatorBase):
    op = lambda self, x, y: x / y
    op_char = '/'
    def simplify(self):
        if isinstance(self.left, Const) and self.left.val == 0:
            return Const(0)
        elif isinstance(self.right, Const):
            if self.right.val == 0:
                raise ZeroDivisionError('Cannot divide by zero')
            elif self.left.val == 1:
                return self.left
        return self

class Power(BinaryOperatorBase):
    op = lambda self, x, y: x ** y
    op_char = '^'
    def simplify(self):
        if isinstance(self.right, Const):
            if self.right.val == 0:
                return Const(1)
            elif self.right.val == 1:
                return self.left
        return self

@dataclass
class Const:
    val: float
    def __repr__(self):
        return str(self.val)
    def __neg__(self):
        return Const(-self.val)

@dataclass
class Var:
    name: str
    def __repr__(self):
        return self.name

if __name__ == '__main__':
    eq = Minus(Plus(Const(10), Const(5)), Times(Const(1), Var('x')))
    print(eq, ' = ', eq.exec())
    eq = Times(Minus(Const(32), Const(31)), Var('x'))
    print(eq, ' = ', eq.exec())
    eq = Power(Const(2), Const(8))
    print(eq, ' = ', eq.exec())
    eq = Power(Var('x'), Const(0))
    print(eq, ' = ', eq.exec())
