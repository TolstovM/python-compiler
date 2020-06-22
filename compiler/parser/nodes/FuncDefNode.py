from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class FuncDefNode(BaseNode):

    def __init__(self, argsListNode, suiteNode, funcName):
        super().__init__()
        self.argListNode = argsListNode
        self.suiteNode = suiteNode
        self.funcName = funcName
        self.children.append(argsListNode)
        self.children.append(suiteNode)

    def __str__(self):
        return "func def: " + str(self.funcName)

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitFuncDef(self)
