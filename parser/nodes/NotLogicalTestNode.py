from .BaseNode import BaseNode


class NotLogicalTestNode(BaseNode):

    def __init__(self, logicalTestNode):
        super(NotLogicalTestNode, self).__init__()
        self.logicalTestNode = logicalTestNode
        self.children.append(logicalTestNode)

    def __str__(self):
        return "not"
