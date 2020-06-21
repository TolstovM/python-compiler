from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class ComparisonNode(BaseNode):

    def __init__(self, leftNode, op, rightNode):
        super(ComparisonNode, self).__init__()
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.op = op
        self.children.append(leftNode)
        self.children.append(rightNode)

    def __str__(self):
        return self.op.text

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitComparison(self)
