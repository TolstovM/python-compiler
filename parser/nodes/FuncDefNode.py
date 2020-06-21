from .BaseNode import BaseNode


class FuncDefNode(BaseNode):

    def __init__(self, argsListNode, suiteNode):
        super().__init__()
        self.argListNode = argsListNode
        self.suiteNode = suiteNode
        self.children.append(argsListNode)
        self.children.append(suiteNode)

    def __str__(self):
        return "func def"
