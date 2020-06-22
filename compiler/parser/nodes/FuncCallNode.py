from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class FuncCallNode(BaseNode):

    def __init__(self, funcName, argsListNode):
        super(FuncCallNode, self).__init__()
        self.funcName = funcName
        self.argsListNode = argsListNode
        self.children.append(argsListNode)

    def __str__(self):
        return 'func: ' + str(self.funcName)

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitFuncCall(self)
