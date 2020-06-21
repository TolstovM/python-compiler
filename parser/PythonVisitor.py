# Generated from Python.g4 by ANTLR 4.7.2
from antlr4 import *
from .nodes import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#program.
    def visitProgram(self, ctx: PythonParser.ProgramContext):
        programNode = ProgramNode()
        for child in ctx.children:
            programNode.appendChild(self.visit(child))
        return programNode

    # Visit a parse tree produced by PythonParser#stmt.
    def visitStmt(self, ctx: PythonParser.StmtContext):
        return self.visit(ctx.children[0])

    # Visit a parse tree produced by PythonParser#suiteInLine.
    def visitSuiteInLine(self, ctx: PythonParser.SuiteInLineContext):
        suiteNode = SuiteNode()
        suiteNode.appendChild(self.visit(ctx.simple_stmt()))
        return suiteNode

    # Visit a parse tree produced by PythonParser#suiteBlock.
    def visitSuiteBlock(self, ctx: PythonParser.SuiteBlockContext):
        suiteNode = SuiteNode()
        i = 0
        while ctx.stmt(i):
            suiteNode.appendChild(self.visit(ctx.stmt(i)))
        return suiteNode

    # Visit a parse tree produced by PythonParser#elif_clause.
    def visitElif_clause(self, ctx: PythonParser.Elif_clauseContext):
        logicalTestNode = self.visit(ctx.logical_test())
        suiteNode = self.visit(ctx.suite())
        elifNode = IfelNode(logicalTestNode, suiteNode)
        return elifNode

    # Visit a parse tree produced by PythonParser#else_clause.
    def visitElse_clause(self, ctx: PythonParser.Else_clauseContext):
        suiteNode = self.visit(ctx.suite())
        elseNode = ElNode(suiteNode)
        return elseNode

    # Visit a parse tree produced by PythonParser#if.
    def visitIf(self, ctx: PythonParser.IfContext):
        logicalTestNode = self.visit(ctx.logical_test())
        suiteNode = self.visit(ctx.suite())
        ifNode = IfNode(logicalTestNode, suiteNode)

        i = 0
        while ctx.elif_clause(0):
            ifNode.appendChild(self.visit(ctx.elif_clause(0)))
            i += 1

        if ctx.else_clause():
            ifNode.appendChild(self.visit(ctx.else_clause()))
        return ifNode

    # Visit a parse tree produced by PythonParser#while.
    def visitWhile(self, ctx: PythonParser.WhileContext):
        logicalTestNode = self.visit(ctx.logical_test())
        suiteNode = self.visit(ctx.suite())
        whileNode = WhileNode(logicalTestNode, suiteNode)
        return whileNode

    # Visit a parse tree produced by PythonParser#funcdef.
    def visitFuncdef(self, ctx:PythonParser.FuncdefContext):
        argListNode = self.visit(ctx.argslist())
        suiteNode = self.visit(ctx.suite())
        funcDefNode = FuncDefNode(argListNode, suiteNode)
        return funcDefNode

    # Visit a parse tree produced by PythonParser#argslist.
    def visitArgsList(self, ctx: PythonParser.ArgslistContext):
        argListNode = ArgListNode()
        for child in ctx.children:
            if child.symbol.text != ',':
                argListNode.addChildren(BaseNode(child))
        return argListNode

    # Visit a parse tree produced by PythonParser#funcDef.
    def visitFuncDef(self, ctx: PythonParser.FuncDefContext):
        return self.visit(ctx.funcdef()) #!!

    # Visit a parse tree produced by PythonParser#simple_stmt.
    def visitSimple_stmt(self, ctx: PythonParser.Simple_stmtContext):
        return self.visit(ctx.small_stmt())

    # Visit a parse tree produced by PythonParser#assign.
    def visitAssign(self, ctx: PythonParser.AssignContext):
        identifierNode = BaseNode(ctx.IDENTIFIER())
        assignPartNode = self.visit(ctx.assign_part())
        assignNode = AssignNode(identifierNode, assignPartNode)
        return assignNode

    # Visit a parse tree produced by PythonParser#funcCall.
    def visitFuncCall(self, ctx: PythonParser.FuncCallContext):
        return self.visit(ctx.func_call())

    # Visit a parse tree produced by PythonParser#return.
    def visitReturn(self, ctx: PythonParser.ReturnContext):
        argsListNode = self.visit(ctx.argslist())
        returnNode = ReturnNode(argsListNode)
        return returnNode

    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx: PythonParser.PrintContext):
        paramNode = None
        if ctx.IDENTIFIER():
            paramNode = BaseNode(ctx.IDENTIFIER())
        elif ctx.SHORT_STRING():
            paramNode = BaseNode(ctx.SHORT_STRING())
        printNode = PrintNode(paramNode)
        return printNode

    # Visit a parse tree produced by PythonParser#assignExpr.
    def visitAssignExpr(self, ctx: PythonParser.AssignExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by PythonParser#assignFuncCall.
    def visitAssignFuncCall(self, ctx: PythonParser.AssignFuncCallContext):
        return self.visit(ctx.func_call())

    # Visit a parse tree produced by PythonParser#comp.
    def visitComp(self, ctx: PythonParser.CompContext):
        comparisonNode = self.visit(ctx.comparison())
        logicalTestNode = LogicalTestNode(comparisonNode)
        return logicalTestNode

    # Visit a parse tree produced by PythonParser#andLogical.
    def visitAndLogical(self, ctx: PythonParser.AndLogicalContext):
        leftLogicalTestNode = self.visit(ctx.logical_test(0))
        rightLogicalTestNode = self.visit(ctx.logical_test(1))
        andLogicalTestNode = AndLogicalTestNode(leftLogicalTestNode, rightLogicalTestNode)
        return andLogicalTestNode

    # Visit a parse tree produced by PythonParser#orLogical.
    def visitOrLogical(self, ctx: PythonParser.OrLogicalContext):
        leftLogicalTestNode = self.visit(ctx.logical_test(0))
        rightLogicalTestNode = self.visit(ctx.logical_test(1))
        orLogicalTestNode = OrLogicalTestNode(leftLogicalTestNode, rightLogicalTestNode)
        return orLogicalTestNode

    # Visit a parse tree produced by PythonParser#notLogical.
    def visitNotLogical(self, ctx:PythonParser.NotLogicalContext):
        localLogicalTestNode = self.visit(ctx.logical_test())
        logicalTestNode = LogicalTestNode(localLogicalTestNode)
        return logicalTestNode

    # Visit a parse tree produced by PythonParser#comparison.
    def visitComparison(self, ctx: PythonParser.ComparisonContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        else:
            leftNode = self.visit(ctx.comparison(0))
            rightNode = self.visit(ctx.comparison(1))
            comparisionNode = ComparisonNode(leftNode, ctx.op, rightNode)
            return comparisionNode

    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx: PythonParser.ExprContext):
        exprNode = None
        if not ctx.expr(1) and ctx.op:
            innerNode = self.visit(ctx.expr(0))
            exprNode = ExprNode(None, innerNode, ctx.op)
        elif ctx.expr(1):
            leftNode = self.visit(ctx.expr(0))
            rightNode = self.visit(ctx.expr(1))
            exprNode = ExprNode(leftNode, rightNode, ctx.op)
        elif ctx.IDENTIFIER():
            exprNode = BaseNode(ctx.IDENTIFIER())
        elif ctx.NUMBER():
            exprNode = BaseNode(ctx.NUMBER())
        elif ctx.func_call():
            exprNode = self.visit(ctx.func_call())
        return exprNode

    # Visit a parse tree produced by PythonParser#func_call.
    def visitFunc_call(self, ctx: PythonParser.Func_callContext):
        argsListNode = self.visit(ctx.argslist())
        funcCallNode = FuncCallNode(ctx.IDENTIFIER(), argsListNode)
        return funcCallNode



del PythonParser