from .BaseNode import BaseNode


class ExprNode(BaseNode):

    def __init__(self, leftNode, rightNode, op):
        super(ExprNode, self).__init__()
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.op = op
        if leftNode:
            self.children.append(leftNode)
        self.children.append(rightNode)

    def __str__(self):
        return self.op
