from .commands import commands
from .parser.nodes import *


class GeneratorVisitor:

    def __init__(self):
        super(GeneratorVisitor, self).__init__()
        self.program = []

    def visitProgram(self, node: ProgramNode):
        funcDefStmt = [i for i, child in enumerate(node.children) if child is FuncDefNode]
        execStmt = [i for i, child in enumerate(node.children[:-1]) if child is not FuncDefNode]

        for idx in execStmt:
            self.visit(node.children[idx])
        self.program.append(commands['halt'])

    def visitAssign(self, node: AssignNode):
        self.visit(node.assignPartNode)
        self.program.append(commands['store'])
        self.program.append(str(node.identifierNode))

    def visitExprNode(self, node: ExprNode):
        if node.op:
            self.visit(node.leftNode)
            self.visit(node.rightNode)
            if node.op != '()':
                self.program.append(commands[str(node)])
        else:
            self.visit(node.rightNode)

    def visitNotLogicalTest(self, node: NotLogicalTestNode):
        self.visit(node.logicalTestNode)
        self.program.append(commands['not'])

    def visitAndLogicalTest(self, node: AndLogicalTestNode):
        self.visit(node.leftLogicalTestNode)
        self.visit(node.rightLogicalTestNode)
        self.program.append(commands['and'])

    def visitOrLogicalTest(self, node: OrLogicalTestNode):
        self.visit(node.leftLogicalTestNode)
        self.visit(node.rightLogicalTestNode)
        self.program.append(commands['or'])

    def visitLogicalTest(self, node: LogicalTestNode):
        self.visit(node.comparison)

    def visitComparison(self, node: ComparisonNode):
        self.visit(node.leftNode)
        self.visit(node.rightNode)
        if node.value:
            self.program.append(commands['push'])
            self.program.append(commands[str(node)])

    def visit(self, node: BaseNode):
        if node:
            node.accept(self)

    def visitDefault(self, node):
        if not node:
            pass
        if str(node).isnumeric():
            self.program.append(commands['push'])
            self.program.append(float(str(node)))
        elif str(node) == 'True' or str(node) == 'False':
            self.program.append(commands['push'])
            self.program.append(commands[str(node)])
        else:
            self.program.append(commands['load'])
            self.program.append(str(node))
