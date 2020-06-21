from .BaseNode import BaseNode


class ElNode(BaseNode):

    def __init__(self, suiteNode):
        super().__init__()
        self.suiteNode = suiteNode
        self.children.append(suiteNode)

    def __str__(self):
        return 'el'
