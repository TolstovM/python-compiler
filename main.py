from compiler.parser import *
from antlr4 import *
from utils import showAstTree
from compiler import GeneratorVisitor


def main():
    text = '''
res = pow(2, 8)
print(res)

def pow(a, b):
    result = 1
    i = 0
    while b > i:
        result = result * a
        i = i + 1
    return result
    '''
    inputStream = InputStream(text)
    lexer = PythonLexer(inputStream)
    tokenStream = CommonTokenStream(lexer)
    parser = PythonParser(tokenStream)

    cst = parser.program()
    print(cst.toStringTree())
    ast = PythonVisitor().visitProgram(cst)
    showAstTree(ast)
    generatorVisitor = GeneratorVisitor()
    generatorVisitor.visitProgram(ast)
    print(generatorVisitor.program)


if __name__ == '__main__':
    main()
