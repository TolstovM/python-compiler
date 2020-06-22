from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class PrintNode(BaseNode):

    def __init__(self, parmNode):
        super(PrintNode, self).__init__()
        self.paramNode = parmNode
        self.children.append(parmNode)

    def __str__(self):
        return 'print'

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitPrint(self)
