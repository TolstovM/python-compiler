from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class ExprNode(BaseNode):

    def __init__(self, leftNode, rightNode, op):
        super(ExprNode, self).__init__()
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.op = op
        if leftNode:
            self.children.append(leftNode)
        self.children.append(rightNode)

    def __str__(self):
        if self.op == '()':
            return self.op
        return str(self.op.text)

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitExprNode(self)
