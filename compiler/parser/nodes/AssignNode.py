from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class AssignNode(BaseNode):

    def __init__(self, identifierNode, assignPartNode):
        super().__init__()
        self.identifierNode = identifierNode
        self.assignPartNode = assignPartNode
        self.children.append(identifierNode)
        self.children.append(assignPartNode)

    def __str__(self):
        return "assign"

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitAssign(self)
