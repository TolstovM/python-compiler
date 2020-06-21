from .BaseNode import BaseNode


class LogicalTestNode(BaseNode):

    def __init__(self, comparisonNode):
        super(LogicalTestNode, self).__init__()
        self.comparison = comparisonNode
        self.children.append(comparisonNode)

    def __str__(self):
        return 'logical_node'
