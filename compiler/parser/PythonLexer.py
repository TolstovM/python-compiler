# Generated from Python.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from compiler.parser.PythonParser import PythonParser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u0124\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\5\2c\n\2\3\2\3\2\7\2g\n\2\f\2")
        buf.write("\16\2j\13\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\7+\u00e8\n+\f+\16+\u00eb\13+\3,\6,\u00ee\n,\r,\16,\u00ef")
        buf.write("\3-\6-\u00f3\n-\r-\16-\u00f4\3-\3-\3.\3.\3.\3.\7.\u00fd")
        buf.write("\n.\f.\16.\u0100\13.\3.\3.\3/\3/\3/\3/\5/\u0108\n/\3/")
        buf.write("\7/\u010b\n/\f/\16/\u010e\13/\3/\3/\3/\3/\3/\5/\u0115")
        buf.write("\n/\3/\7/\u0118\n/\f/\16/\u011b\13/\3/\5/\u011e\n/\3\60")
        buf.write("\5\60\u0121\n\60\3\60\3\60\2\2\61\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2\3")
        buf.write("\2\t\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\4\2\13\13\"\"\4\2")
        buf.write("\f\f\17\17\6\2\f\f\17\17))^^\6\2\f\f\17\17$$^^\2\u0130")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\3b\3\2\2\2\5k\3\2\2\2\7o\3\2\2\2\tv\3\2\2\2\13|\3")
        buf.write("\2\2\2\r\177\3\2\2\2\17\u0084\3\2\2\2\21\u0089\3\2\2\2")
        buf.write("\23\u008f\3\2\2\2\25\u0093\3\2\2\2\27\u0096\3\2\2\2\31")
        buf.write("\u009a\3\2\2\2\33\u009e\3\2\2\2\35\u00a3\3\2\2\2\37\u00a9")
        buf.write("\3\2\2\2!\u00ab\3\2\2\2#\u00ad\3\2\2\2%\u00af\3\2\2\2")
        buf.write("\'\u00b2\3\2\2\2)\u00b5\3\2\2\2+\u00b8\3\2\2\2-\u00bb")
        buf.write("\3\2\2\2/\u00be\3\2\2\2\61\u00c0\3\2\2\2\63\u00c2\3\2")
        buf.write("\2\2\65\u00c4\3\2\2\2\67\u00c6\3\2\2\29\u00c8\3\2\2\2")
        buf.write(";\u00ca\3\2\2\2=\u00cc\3\2\2\2?\u00cf\3\2\2\2A\u00d1\3")
        buf.write("\2\2\2C\u00d3\3\2\2\2E\u00d5\3\2\2\2G\u00d7\3\2\2\2I\u00d9")
        buf.write("\3\2\2\2K\u00db\3\2\2\2M\u00dd\3\2\2\2O\u00df\3\2\2\2")
        buf.write("Q\u00e1\3\2\2\2S\u00e3\3\2\2\2U\u00e5\3\2\2\2W\u00ed\3")
        buf.write("\2\2\2Y\u00f2\3\2\2\2[\u00f8\3\2\2\2]\u011d\3\2\2\2_\u0120")
        buf.write("\3\2\2\2ac\7\17\2\2ba\3\2\2\2bc\3\2\2\2cd\3\2\2\2dh\7")
        buf.write("\f\2\2eg\7\"\2\2fe\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2")
        buf.write("\2i\4\3\2\2\2jh\3\2\2\2kl\7f\2\2lm\7g\2\2mn\7h\2\2n\6")
        buf.write("\3\2\2\2op\7t\2\2pq\7g\2\2qr\7v\2\2rs\7w\2\2st\7t\2\2")
        buf.write("tu\7p\2\2u\b\3\2\2\2vw\7r\2\2wx\7t\2\2xy\7k\2\2yz\7p\2")
        buf.write("\2z{\7v\2\2{\n\3\2\2\2|}\7k\2\2}~\7h\2\2~\f\3\2\2\2\177")
        buf.write("\u0080\7g\2\2\u0080\u0081\7n\2\2\u0081\u0082\7k\2\2\u0082")
        buf.write("\u0083\7h\2\2\u0083\16\3\2\2\2\u0084\u0085\7g\2\2\u0085")
        buf.write("\u0086\7n\2\2\u0086\u0087\7u\2\2\u0087\u0088\7g\2\2\u0088")
        buf.write("\20\3\2\2\2\u0089\u008a\7y\2\2\u008a\u008b\7j\2\2\u008b")
        buf.write("\u008c\7k\2\2\u008c\u008d\7n\2\2\u008d\u008e\7g\2\2\u008e")
        buf.write("\22\3\2\2\2\u008f\u0090\7h\2\2\u0090\u0091\7q\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\24\3\2\2\2\u0093\u0094\7q\2\2\u0094")
        buf.write("\u0095\7t\2\2\u0095\26\3\2\2\2\u0096\u0097\7c\2\2\u0097")
        buf.write("\u0098\7p\2\2\u0098\u0099\7f\2\2\u0099\30\3\2\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7q\2\2\u009c\u009d\7v\2\2\u009d")
        buf.write("\32\3\2\2\2\u009e\u009f\7V\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\u00a1\7w\2\2\u00a1\u00a2\7g\2\2\u00a2\34\3\2\2\2\u00a3")
        buf.write("\u00a4\7H\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7n\2\2\u00a6")
        buf.write("\u00a7\7u\2\2\u00a7\u00a8\7g\2\2\u00a8\36\3\2\2\2\u00a9")
        buf.write("\u00aa\7.\2\2\u00aa \3\2\2\2\u00ab\u00ac\7<\2\2\u00ac")
        buf.write("\"\3\2\2\2\u00ad\u00ae\7=\2\2\u00ae$\3\2\2\2\u00af\u00b0")
        buf.write("\7?\2\2\u00b0\u00b1\7?\2\2\u00b1&\3\2\2\2\u00b2\u00b3")
        buf.write("\7@\2\2\u00b3\u00b4\7?\2\2\u00b4(\3\2\2\2\u00b5\u00b6")
        buf.write("\7>\2\2\u00b6\u00b7\7?\2\2\u00b7*\3\2\2\2\u00b8\u00b9")
        buf.write("\7>\2\2\u00b9\u00ba\7@\2\2\u00ba,\3\2\2\2\u00bb\u00bc")
        buf.write("\7#\2\2\u00bc\u00bd\7?\2\2\u00bd.\3\2\2\2\u00be\u00bf")
        buf.write("\7\u0080\2\2\u00bf\60\3\2\2\2\u00c0\u00c1\7~\2\2\u00c1")
        buf.write("\62\3\2\2\2\u00c2\u00c3\7`\2\2\u00c3\64\3\2\2\2\u00c4")
        buf.write("\u00c5\7(\2\2\u00c5\66\3\2\2\2\u00c6\u00c7\7-\2\2\u00c7")
        buf.write("8\3\2\2\2\u00c8\u00c9\7/\2\2\u00c9:\3\2\2\2\u00ca\u00cb")
        buf.write("\7\'\2\2\u00cb<\3\2\2\2\u00cc\u00cd\7\61\2\2\u00cd\u00ce")
        buf.write("\7\61\2\2\u00ce>\3\2\2\2\u00cf\u00d0\7\61\2\2\u00d0@\3")
        buf.write("\2\2\2\u00d1\u00d2\7,\2\2\u00d2B\3\2\2\2\u00d3\u00d4\7")
        buf.write(">\2\2\u00d4D\3\2\2\2\u00d5\u00d6\7@\2\2\u00d6F\3\2\2\2")
        buf.write("\u00d7\u00d8\7*\2\2\u00d8H\3\2\2\2\u00d9\u00da\7+\2\2")
        buf.write("\u00daJ\3\2\2\2\u00db\u00dc\7}\2\2\u00dcL\3\2\2\2\u00dd")
        buf.write("\u00de\7\177\2\2\u00deN\3\2\2\2\u00df\u00e0\7]\2\2\u00e0")
        buf.write("P\3\2\2\2\u00e1\u00e2\7_\2\2\u00e2R\3\2\2\2\u00e3\u00e4")
        buf.write("\7?\2\2\u00e4T\3\2\2\2\u00e5\u00e9\t\2\2\2\u00e6\u00e8")
        buf.write("\t\3\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00eaV\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ee\t\4\2\2\u00ed\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3")
        buf.write("\2\2\2\u00f0X\3\2\2\2\u00f1\u00f3\t\5\2\2\u00f2\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\b-\2\2")
        buf.write("\u00f7Z\3\2\2\2\u00f8\u00f9\7\61\2\2\u00f9\u00fa\7\61")
        buf.write("\2\2\u00fa\u00fe\3\2\2\2\u00fb\u00fd\n\6\2\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0101\u0102\b.\2\2\u0102\\\3\2\2\2\u0103\u010c\7)\2\2")
        buf.write("\u0104\u0107\7^\2\2\u0105\u0108\5_\60\2\u0106\u0108\13")
        buf.write("\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108\u010b")
        buf.write("\3\2\2\2\u0109\u010b\n\7\2\2\u010a\u0104\3\2\2\2\u010a")
        buf.write("\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010d\u010f\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010f\u011e\7)\2\2\u0110\u0119\7$\2\2\u0111\u0114")
        buf.write("\7^\2\2\u0112\u0115\5_\60\2\u0113\u0115\13\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115\u0118\3\2\2\2")
        buf.write("\u0116\u0118\n\b\2\2\u0117\u0111\3\2\2\2\u0117\u0116\3")
        buf.write("\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c")
        buf.write("\u011e\7$\2\2\u011d\u0103\3\2\2\2\u011d\u0110\3\2\2\2")
        buf.write("\u011e^\3\2\2\2\u011f\u0121\7\17\2\2\u0120\u011f\3\2\2")
        buf.write("\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123")
        buf.write("\7\f\2\2\u0123`\3\2\2\2\21\2bh\u00e9\u00ef\u00f4\u00fe")
        buf.write("\u0107\u010a\u010c\u0114\u0117\u0119\u011d\u0120\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class PythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NL = 1
    DEF = 2
    RETURN = 3
    PRINT = 4
    IF = 5
    ELIF = 6
    ELSE = 7
    WHILE = 8
    FOR = 9
    OR = 10
    AND = 11
    NOT = 12
    TRUE = 13
    FALSE = 14
    COMMA = 15
    COLON = 16
    SEMI_COLON = 17
    EQUALS = 18
    GT_EQ = 19
    LT_EQ = 20
    NOT_EQ_1 = 21
    NOT_EQ_2 = 22
    NOT_OP = 23
    OR_OP = 24
    XOR = 25
    AND_OP = 26
    ADD = 27
    MINUS = 28
    MOD = 29
    IDIV = 30
    DIV = 31
    STAR = 32
    LESS_THAN = 33
    GREATER_THAN = 34
    OPEN_PAREN = 35
    CLOSE_PAREN = 36
    OPEN_BRACE = 37
    CLOSE_BRACE = 38
    OPEN_BRACKET = 39
    CLOSE_BRACKET = 40
    ASSIGN = 41
    IDENTIFIER = 42
    NUMBER = 43
    WHITESPACE = 44
    COMMENT = 45
    SHORT_STRING = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'print'", "'if'", "'elif'", "'else'", 
            "'while'", "'for'", "'or'", "'and'", "'not'", "'True'", "'False'", 
            "','", "':'", "';'", "'=='", "'>='", "'<='", "'<>'", "'!='", 
            "'~'", "'|'", "'^'", "'&'", "'+'", "'-'", "'%'", "'//'", "'/'", 
            "'*'", "'<'", "'>'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "NL", "DEF", "RETURN", "PRINT", "IF", "ELIF", "ELSE", "WHILE", 
            "FOR", "OR", "AND", "NOT", "TRUE", "FALSE", "COMMA", "COLON", 
            "SEMI_COLON", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", 
            "NOT_OP", "OR_OP", "XOR", "AND_OP", "ADD", "MINUS", "MOD", "IDIV", 
            "DIV", "STAR", "LESS_THAN", "GREATER_THAN", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
            "ASSIGN", "IDENTIFIER", "NUMBER", "WHITESPACE", "COMMENT", "SHORT_STRING" ]

    ruleNames = [ "NL", "DEF", "RETURN", "PRINT", "IF", "ELIF", "ELSE", 
                  "WHILE", "FOR", "OR", "AND", "NOT", "TRUE", "FALSE", "COMMA", 
                  "COLON", "SEMI_COLON", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", 
                  "NOT_EQ_2", "NOT_OP", "OR_OP", "XOR", "AND_OP", "ADD", 
                  "MINUS", "MOD", "IDIV", "DIV", "STAR", "LESS_THAN", "GREATER_THAN", 
                  "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", 
                  "OPEN_BRACKET", "CLOSE_BRACKET", "ASSIGN", "IDENTIFIER", 
                  "NUMBER", "WHITESPACE", "COMMENT", "SHORT_STRING", "RN" ]

    grammarFileName = "Python.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: PythonLexer = lexer

        def pull_token(self):
            return super(PythonLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NL, PythonParser.INDENT, PythonParser.DEDENT, True)
        return self.denter.next_token()



