from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class NotLogicalTestNode(BaseNode):

    def __init__(self, logicalTestNode):
        super(NotLogicalTestNode, self).__init__()
        self.logicalTestNode = logicalTestNode
        self.children.append(logicalTestNode)

    def __str__(self):
        return "not"

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitNotLogicalTest(self)
