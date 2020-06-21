from compiler import GeneratorVisitor


class BaseNode:

    def __init__(self, value=None):
        super(BaseNode, self).__init__()
        self.children = []
        self.value = value

    def __str__(self):
        return str(self.value)

    def accept(self, visitor: GeneratorVisitor):
        visitor.visitDefault(self)
