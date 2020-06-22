from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class ReturnNode(BaseNode):

    def __init__(self, argsListNode):
        super(ReturnNode, self).__init__()
        self.argsListNode = argsListNode
        self.children.append(argsListNode)

    def __str__(self):
        return 'return'

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitReturn(self)
