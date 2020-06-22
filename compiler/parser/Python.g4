grammar Python;

tokens { INDENT, DEDENT, LINE_BREAK }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from compiler.parser.PythonParser import PythonParser
}
@lexer::members {
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

}

NL: ('\r'? '\n' ' '*);

program: stmt* EOF;

stmt
    : simple_stmt
    | compound_stmt
    ;

compound_stmt
    : IF logical_test COLON suite elif_clause* else_clause?     # if
    | WHILE logical_test COLON suite                            # while
//    | FOR exprlist 'in' testlist COLON suite
    | funcdef                                                   # funcDef
    ;

suite
    : simple_stmt                           # suiteInLine
    | INDENT stmt+ DEDENT        # suiteBlock
    ;

elif_clause
    : ELIF logical_test COLON suite
    ;

else_clause
    : ELSE COLON suite
    ;

funcdef
    : DEF IDENTIFIER OPEN_PAREN argslist? CLOSE_PAREN COLON suite
    ;

argslist
    : IDENTIFIER (COMMA IDENTIFIER)+    # argsList
    ;

simple_stmt
    : small_stmt (LINE_BREAK | EOF)
    ;

small_stmt
    : IDENTIFIER op=ASSIGN assign_part                                                          # assign
    | func_call                                                                                 # funcCall
    | RETURN argslist                                                                           # return
    | PRINT OPEN_PAREN (IDENTIFIER | SHORT_STRING) CLOSE_PAREN                                  # print
    ;

assign_part
    : expr                                              # assignExpr
    | logical_test                                      # logicalAssign
    | func_call                                         # assignFuncCall
    ;



logical_test
    : comparison                        # comp
    | NOT logical_test                  # notLogical
    | logical_test AND logical_test     # andLogical
    | logical_test OR logical_test      # orLogical
    ;

comparison
    : TRUE | FALSE
    | comparison op=(LESS_THAN | GREATER_THAN | EQUALS | GT_EQ | LT_EQ | NOT_EQ_1 | NOT_EQ_2 /*| optional=NOT? IN | IS  optional=NOT?*/) comparison
    | expr
    ;

expr
    : OPEN_PAREN expr CLOSE_PAREN
    | op=(ADD | MINUS | NOT_OP) expr
    | expr op=(STAR | DIV | MOD | IDIV) expr
    | expr op=(ADD | MINUS) expr
    | expr op=AND_OP expr
    | expr op=XOR expr
    | expr op=OR_OP expr
    | NUMBER
    | IDENTIFIER
    | func_call
    ;

func_call
    : IDENTIFIER OPEN_PAREN argslist CLOSE_PAREN
    ;

DEF                : 'def';
RETURN             : 'return';
PRINT              : 'print';
IF                 : 'if';
ELIF               : 'elif';
ELSE               : 'else';
WHILE              : 'while';
FOR                : 'for';
OR                 : 'or';
AND                : 'and';
NOT                : 'not';
TRUE               : 'True';
FALSE              : 'False';

COMMA              : ',';
COLON              : ':';
SEMI_COLON         : ';';

EQUALS             : '==';
GT_EQ              : '>=';
LT_EQ              : '<=';
NOT_EQ_1           : '<>';
NOT_EQ_2           : '!=';

NOT_OP             : '~';
OR_OP              : '|';
XOR                : '^';
AND_OP             : '&';
ADD                : '+';
MINUS              : '-';
MOD                : '%';
IDIV               : '//';
DIV                : '/';
STAR               : '*';

LESS_THAN          : '<';
GREATER_THAN       : '>';
OPEN_PAREN         : '(';
CLOSE_PAREN        : ')';
OPEN_BRACE         : '{';
CLOSE_BRACE        : '}';
OPEN_BRACKET       : '[';
CLOSE_BRACKET      : ']';

ASSIGN             : '=';

IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
WHITESPACE: [ \t]+ -> skip;
COMMENT: '//' ~('\r' | '\n')* -> skip;

SHORT_STRING
    : '\'' ('\\' (RN | .) | ~[\\\r\n'])* '\''
    | '"'  ('\\' (RN | .) | ~[\\\r\n"])* '"'
    ;

fragment RN
    : '\r'? '\n'
    ;

