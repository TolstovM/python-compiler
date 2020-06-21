from .BaseNode import BaseNode


class ArgListNode(BaseNode):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'argList'

    def addChildren(self, node):
        self.children.append(node)
