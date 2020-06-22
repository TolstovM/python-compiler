from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class IfNode(BaseNode):

    def __init__(self, logicalTestNode, suiteNode):
        super().__init__()
        self.logicalTestNode = logicalTestNode
        self.suiteNode = suiteNode
        self.children.append(logicalTestNode)
        self.children.append(suiteNode)

    def __str__(self):
        return 'if'

    def appendChild(self, node):
        self.children.append(node)

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitIf(self)
