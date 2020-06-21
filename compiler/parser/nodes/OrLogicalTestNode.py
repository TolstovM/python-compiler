from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class OrLogicalTestNode(BaseNode):

    def __init__(self, leftLogicalTestNode, rightLogicalTestNode):
        super(OrLogicalTestNode, self).__init__()
        self.leftLogicalTestNode = leftLogicalTestNode
        self.rightLogicalTestNode = rightLogicalTestNode
        self.children.append(leftLogicalTestNode)
        self.children.append(rightLogicalTestNode)

    def __str__(self):
        return "or"

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitOrLogicalTest(self)
