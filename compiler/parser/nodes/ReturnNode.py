from .BaseNode import BaseNode


class ReturnNode(BaseNode):

    def __init__(self, argsListNode):
        super(ReturnNode, self).__init__()
        self.argsListNode = argsListNode
        self.children.append(argsListNode)

    def __str__(self):
        return 'return'
