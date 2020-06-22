from .commands import commands
from .parser.nodes import *


class GeneratorVisitor:

    def __init__(self):
        super(GeneratorVisitor, self).__init__()
        self.program = []
        self.funcLicks = dict()

    def visitProgram(self, node: ProgramNode):
        funcDefStmt = [i for i, child in enumerate(node.children) if isinstance(child, FuncDefNode)]
        execStmt = [i for i, child in enumerate(node.children[:-1]) if not isinstance(child, FuncDefNode)]

        for idx in funcDefStmt:
            self.visit(node.children[idx])

        self.program.append(commands['start'])
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
        if node.op:
            self.program.append(commands['push'])
            self.program.append(commands[str(node)])

    def visitIf(self, node: IfNode):
        self.visit(node.logicalTestNode)
        self.program.append(commands['jump_if'])
        jumpToBlank = len(self.program)
        self.program.append(None)

        jumpsBlank = self._visitIfChild(node)

        self.program[jumpToBlank] = len(self.program)
        self.visit(node.suiteNode)
        for idx in jumpsBlank:
            self.program[idx] = len(self.program)

    def visitWhile(self, node: WhileNode):
        suiteStartPosition = len(self.program)
        self.visit(node.logicalTestNode)
        self.program.append(commands['not'])
        self.program.append(commands['jump_if'])
        jumpToEndBlank = len(self.program)
        self.program.append(None)

        self.visit(node.suiteNode)

        self.program.append(commands['jump'])
        self.program.append(suiteStartPosition)
        self.program[jumpToEndBlank] = len(self.program)

    def visitSuite(self, node: SuiteNode):
        for child in node.children:
            self.visit(child)

    def visitPrint(self, node: PrintNode):
        if '\'' in str(node.children[0].value) or '\"' in str(node.children[0].value):
            self.program.append(commands['push'])
            self.program.append(str(node.children[0]).replace('\'', '').replace('\"', ''))
        else:
            self.visit(node.children[0])
        self.program.append(commands['func'])
        self.program.append('print')
        self.program.append(1)

    def visitFuncDef(self, node: FuncDefNode):
        self.funcLicks[str(node.funcName)] = len(self.program)
        for i in range(len(node.argListNode.children) - 1, -1, -1):
            self.program.append(commands['store'])
            self.program.append(str(node.argListNode.children[i]))
        self.visit(node.suiteNode)

    def visitArgsList(self, node: ArgListNode):
        for child in node.children:
            self.visit(child)

    def visitReturn(self, node: ReturnNode):
        self.visit(node.argsListNode)
        self.program.append(commands['return'])

    def visitFuncCall(self, node: FuncCallNode):
        self.visit(node.argsListNode)
        self.program.append(commands['call'])
        self.program.append(self.funcLicks[str(node.funcName)])

    def visit(self, node: BaseNode):
        if node:
            return node.accept(self)

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

    def _visitIfChild(self, node: IfNode):
        ifelNodes = [child for child in node.children if isinstance(child, IfelNode)]
        elseNode = [child for child in node.children if isinstance(child, ElNode)]

        jumpsToBlank = []
        for child in ifelNodes:
            self.visit(child.logicalTestNode)
            self.program.append(commands['jump_if'])
            jumpsToBlank.append(len(self.program))
            self.program.append(None)

        jumpsBlank = []
        if elseNode:
            self.visit(elseNode[0].suiteNode)
            self.program.append(commands['jump'])
            jumpsBlank.append(len(self.program))
            self.program.append(None)

        for i, child in enumerate(ifelNodes):
            self.program[jumpsToBlank[i]] = len(self.program)
            self.visit(child.suiteNode)
            self.program.append(commands['jump'])
            jumpsBlank.append(len(self.program))
            self.program.append(None)

        return jumpsBlank
