from .BaseNode import BaseNode
from compiler import GeneratorVisitor


class SuiteNode(BaseNode):

    def __init__(self):
        super(SuiteNode, self).__init__()

    def __str__(self):
        return 'sub_scope'

    def appendChild(self, node):
        self.children.append(node)

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitSuite(self)
