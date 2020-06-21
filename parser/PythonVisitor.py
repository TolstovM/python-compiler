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

    # Visit a parse tree produced by PythonParser#suite.
    def visitSuite(self, ctx: PythonParser.SuiteContext):
        childrenNodes = []
        for child in ctx.children:
            childrenNodes.append(self.visit(child))
        return childrenNodes

    # Visit a parse tree produced by PythonParser#elif_clause.
    def visitElif_clause(self, ctx: PythonParser.Elif_clauseContext):
        logicalTestNode = self.visit(ctx.children[0])
        suiteNode = self.visit(ctx.children[1])
        elifNode = IfelNode(logicalTestNode, suiteNode)
        return elifNode

    # Visit a parse tree produced by PythonParser#else_clause.
    def visitElse_clause(self, ctx: PythonParser.Else_clauseContext):
        suiteNode = self.visit(ctx.children[0])
        elseNode = ElNode(suiteNode)
        return elseNode

    # Visit a parse tree produced by PythonParser#if.
    def visitIf(self, ctx: PythonParser.IfContext):
        logicalTestNode = self.visit(ctx.children[0])
        suiteNode = self.visit(ctx.children[1])
        ifNode = IfNode(logicalTestNode, suiteNode)
        for i in range(2, len(ctx.children)):
            ifNode.appendChild(self.visit(ctx.children[i]))
        return ifNode

    # Visit a parse tree produced by PythonParser#while.
    def visitWhile(self, ctx: PythonParser.WhileContext):
        logicalTestNode = self.visit(ctx.children[0])
        suiteNode = self.visit(ctx.children[1])
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
                argListNode.addChildren(self.visit(child))
        return argListNode




    # Visit a parse tree produced by PythonParser#funcDef.
    def visitFuncDef(self, ctx:PythonParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#simple_stmt.
    def visitSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assign.
    def visitAssign(self, ctx:PythonParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#return.
    def visitReturn(self, ctx:PythonParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx:PythonParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignExpr.
    def visitAssignExpr(self, ctx:PythonParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignFuncCall.
    def visitAssignFuncCall(self, ctx:PythonParser.AssignFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#comp.
    def visitComp(self, ctx:PythonParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#andLogical.
    def visitAndLogical(self, ctx:PythonParser.AndLogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#orLogical.
    def visitOrLogical(self, ctx:PythonParser.OrLogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#notLogical.
    def visitNotLogical(self, ctx:PythonParser.NotLogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#comparison.
    def visitComparison(self, ctx:PythonParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#func_call.
    def visitFunc_call(self, ctx:PythonParser.Func_callContext):
        return self.visitChildren(ctx)



del PythonParser