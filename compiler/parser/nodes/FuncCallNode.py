from .BaseNode import BaseNode


class FuncCallNode(BaseNode):

    def __init__(self, funcName, argsListNode):
        super(FuncCallNode, self).__init__()
        self.funcName = funcName
        self.argsListNode = argsListNode
        self.children.append(argsListNode)

    def __str__(self):
        return 'func: ' + str(self.funcName)
