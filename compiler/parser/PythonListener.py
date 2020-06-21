# Generated from Python.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#program.
    def enterProgram(self, ctx:PythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonParser#program.
    def exitProgram(self, ctx:PythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonParser#stmt.
    def enterStmt(self, ctx:PythonParser.StmtContext):
        pass

    # Exit a parse tree produced by PythonParser#stmt.
    def exitStmt(self, ctx:PythonParser.StmtContext):
        pass


    # Enter a parse tree produced by PythonParser#if.
    def enterIf(self, ctx:PythonParser.IfContext):
        pass

    # Exit a parse tree produced by PythonParser#if.
    def exitIf(self, ctx:PythonParser.IfContext):
        pass


    # Enter a parse tree produced by PythonParser#while.
    def enterWhile(self, ctx:PythonParser.WhileContext):
        pass

    # Exit a parse tree produced by PythonParser#while.
    def exitWhile(self, ctx:PythonParser.WhileContext):
        pass


    # Enter a parse tree produced by PythonParser#funcDef.
    def enterFuncDef(self, ctx:PythonParser.FuncDefContext):
        pass

    # Exit a parse tree produced by PythonParser#funcDef.
    def exitFuncDef(self, ctx:PythonParser.FuncDefContext):
        pass


    # Enter a parse tree produced by PythonParser#suiteInLine.
    def enterSuiteInLine(self, ctx:PythonParser.SuiteInLineContext):
        pass

    # Exit a parse tree produced by PythonParser#suiteInLine.
    def exitSuiteInLine(self, ctx:PythonParser.SuiteInLineContext):
        pass


    # Enter a parse tree produced by PythonParser#suiteBlock.
    def enterSuiteBlock(self, ctx:PythonParser.SuiteBlockContext):
        pass

    # Exit a parse tree produced by PythonParser#suiteBlock.
    def exitSuiteBlock(self, ctx:PythonParser.SuiteBlockContext):
        pass


    # Enter a parse tree produced by PythonParser#elif_clause.
    def enterElif_clause(self, ctx:PythonParser.Elif_clauseContext):
        pass

    # Exit a parse tree produced by PythonParser#elif_clause.
    def exitElif_clause(self, ctx:PythonParser.Elif_clauseContext):
        pass


    # Enter a parse tree produced by PythonParser#else_clause.
    def enterElse_clause(self, ctx:PythonParser.Else_clauseContext):
        pass

    # Exit a parse tree produced by PythonParser#else_clause.
    def exitElse_clause(self, ctx:PythonParser.Else_clauseContext):
        pass


    # Enter a parse tree produced by PythonParser#funcdef.
    def enterFuncdef(self, ctx:PythonParser.FuncdefContext):
        pass

    # Exit a parse tree produced by PythonParser#funcdef.
    def exitFuncdef(self, ctx:PythonParser.FuncdefContext):
        pass


    # Enter a parse tree produced by PythonParser#argsList.
    def enterArgsList(self, ctx:PythonParser.ArgsListContext):
        pass

    # Exit a parse tree produced by PythonParser#argsList.
    def exitArgsList(self, ctx:PythonParser.ArgsListContext):
        pass


    # Enter a parse tree produced by PythonParser#simple_stmt.
    def enterSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#simple_stmt.
    def exitSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#assign.
    def enterAssign(self, ctx:PythonParser.AssignContext):
        pass

    # Exit a parse tree produced by PythonParser#assign.
    def exitAssign(self, ctx:PythonParser.AssignContext):
        pass


    # Enter a parse tree produced by PythonParser#funcCall.
    def enterFuncCall(self, ctx:PythonParser.FuncCallContext):
        pass

    # Exit a parse tree produced by PythonParser#funcCall.
    def exitFuncCall(self, ctx:PythonParser.FuncCallContext):
        pass


    # Enter a parse tree produced by PythonParser#return.
    def enterReturn(self, ctx:PythonParser.ReturnContext):
        pass

    # Exit a parse tree produced by PythonParser#return.
    def exitReturn(self, ctx:PythonParser.ReturnContext):
        pass


    # Enter a parse tree produced by PythonParser#print.
    def enterPrint(self, ctx:PythonParser.PrintContext):
        pass

    # Exit a parse tree produced by PythonParser#print.
    def exitPrint(self, ctx:PythonParser.PrintContext):
        pass


    # Enter a parse tree produced by PythonParser#logicalAssign.
    def enterLogicalAssign(self, ctx:PythonParser.LogicalAssignContext):
        pass

    # Exit a parse tree produced by PythonParser#logicalAssign.
    def exitLogicalAssign(self, ctx:PythonParser.LogicalAssignContext):
        pass


    # Enter a parse tree produced by PythonParser#assignExpr.
    def enterAssignExpr(self, ctx:PythonParser.AssignExprContext):
        pass

    # Exit a parse tree produced by PythonParser#assignExpr.
    def exitAssignExpr(self, ctx:PythonParser.AssignExprContext):
        pass


    # Enter a parse tree produced by PythonParser#assignFuncCall.
    def enterAssignFuncCall(self, ctx:PythonParser.AssignFuncCallContext):
        pass

    # Exit a parse tree produced by PythonParser#assignFuncCall.
    def exitAssignFuncCall(self, ctx:PythonParser.AssignFuncCallContext):
        pass


    # Enter a parse tree produced by PythonParser#comp.
    def enterComp(self, ctx:PythonParser.CompContext):
        pass

    # Exit a parse tree produced by PythonParser#comp.
    def exitComp(self, ctx:PythonParser.CompContext):
        pass


    # Enter a parse tree produced by PythonParser#andLogical.
    def enterAndLogical(self, ctx:PythonParser.AndLogicalContext):
        pass

    # Exit a parse tree produced by PythonParser#andLogical.
    def exitAndLogical(self, ctx:PythonParser.AndLogicalContext):
        pass


    # Enter a parse tree produced by PythonParser#orLogical.
    def enterOrLogical(self, ctx:PythonParser.OrLogicalContext):
        pass

    # Exit a parse tree produced by PythonParser#orLogical.
    def exitOrLogical(self, ctx:PythonParser.OrLogicalContext):
        pass


    # Enter a parse tree produced by PythonParser#notLogical.
    def enterNotLogical(self, ctx:PythonParser.NotLogicalContext):
        pass

    # Exit a parse tree produced by PythonParser#notLogical.
    def exitNotLogical(self, ctx:PythonParser.NotLogicalContext):
        pass


    # Enter a parse tree produced by PythonParser#comparison.
    def enterComparison(self, ctx:PythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PythonParser#comparison.
    def exitComparison(self, ctx:PythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PythonParser#expr.
    def enterExpr(self, ctx:PythonParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParser#expr.
    def exitExpr(self, ctx:PythonParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParser#func_call.
    def enterFunc_call(self, ctx:PythonParser.Func_callContext):
        pass

    # Exit a parse tree produced by PythonParser#func_call.
    def exitFunc_call(self, ctx:PythonParser.Func_callContext):
        pass


