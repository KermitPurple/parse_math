from dataclasses import dataclass

@dataclass
class BinaryTreeNodeBase:
    left: any = None
    right: any = None

class BinaryOperatorBase(BinaryTreeNodeBase):
    op = lambda self, x, y: x
    op_char = '_'
    def exec(self):
        if isinstance(self.left, BinaryOperatorBase):
            self.left = self.left.exec()
        if isinstance(self.right, BinaryOperatorBase):
            self.right = self.right.exec()
        if isinstance(self.left, Const) and isinstance(self.right, Const):
            return Const(self.op(self.left.val, self.right.val))
        return self
    def __repr__(self):
        return f'({self.left} {self.op_char} {self.right})'

class Plus(BinaryOperatorBase):
    op = lambda self, x, y: x + y
    op_char = '+'

class Minus(BinaryOperatorBase):
    op = lambda self, x, y: x - y
    op_char = '-'

class Times(BinaryOperatorBase):
    op = lambda self, x, y: x * y
    op_char = '*'

class Divide(BinaryOperatorBase):
    op = lambda self, x, y: x / y
    op_char = '/'

class Power(BinaryOperatorBase):
    op = lambda self, x, y: x ** y
    op_char = '^'

@dataclass
class Const:
    val: float
    def __repr__(self):
        return str(self.val)

@dataclass
class Var:
    name: str
    def __repr__(self):
        return self.name

if __name__ == '__main__':
    eq = Minus(Plus(Const(10), Const(5)), Times(Minus(Const(32), Const(31)), Var('x')))
    print(eq)
    print(eq.exec())
