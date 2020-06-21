from .BaseNode import BaseNode


class WhileNode(BaseNode):

    def __init__(self, logicalTestNode, suiteNode):
        super().__init__()
        self.logicalTestNode = logicalTestNode
        self.suiteNode = suiteNode
        self.children.append(logicalTestNode)
        self.children.append(suiteNode)

    def __str__(self):
        return 'while'
