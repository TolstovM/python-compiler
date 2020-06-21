from .BaseNode import BaseNode


class ComparisonNode(BaseNode):

    def __init__(self, leftNode, op, rightNode):
        super(ComparisonNode, self).__init__()
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.op = op
        self.children.append(leftNode)
        self.children.append(rightNode)

    def __str__(self):
        return self.op
