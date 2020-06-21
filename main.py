from compiler.parser import *
from antlr4 import *
from utils import showAstTree
from compiler import GeneratorVisitor


def main():
    text = '''
a=3*8+(10-8/2)*3 == 42 and True
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
