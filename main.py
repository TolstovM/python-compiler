from parser import *
from antlr4 import *

def main():
    text = '''
    a = 2
    b = 2
    if a == b:
        print('hello')
    else:
        max(a, b)
        print('loh')
        
    def max (x1, x2):
        return x1
    '''
    inputStream = InputStream(text)
    lexer = PythonLexer(inputStream)
    tokenStream = CommonTokenStream(lexer)
    parser = PythonParser(tokenStream)

    cst = parser.program()
    print(cst.toStringTree())
    ast = PythonVisitor().visitProgram(cst)
    print(ast.toStringTree())


if __name__ == '__main__':
    main()
