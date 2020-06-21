from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class LogicalTestNode(BaseNode):

    def __init__(self, comparisonNode):
        super(LogicalTestNode, self).__init__()
        self.comparison = comparisonNode
        self.children.append(comparisonNode)

    def __str__(self):
        return 'logical_node'

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitLogicalTest(self)
