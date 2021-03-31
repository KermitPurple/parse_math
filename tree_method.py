from dataclasses import dataclass

@dataclass
class BinaryTreeNodeBase:
    left: any = None
    right: any = None

class BinaryOperatorBase(BinaryTreeNodeBase):
    op = lambda self, x, y: x
    op_char = '_'
    def exec(self, env: dict = None):
        return self.op(self.left.exec(env), self.right.exec(env))
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
    def __neg__(self):
        return Const(-self.val)
    def exec(self, _env: dict = None):
        return self.val

@dataclass
class Var:
    name: str
    def __repr__(self):
        return self.name
    def exec(self, env: dict = None):
        if env is None or self.name not in env:
            raise KeyError(f'{self.name} is not defined')
        return env[self.name]

if __name__ == '__main__':
    eq = Times(Plus(Const(3), Const(2)), Power(Const(2), Const(8)))
    print(eq, '=', eq.exec())
