from compiler.parser import *
from antlr4 import *
from utils import showAstTree
from compiler import GeneratorVisitor
from vm.machine import *


def main():
    text = '''
def max(x1, x2):
    if x1 > x2:
        return x1
    else:
        return x2

pow2 = pow(2, 8)
pow3 = pow(3, 7)
maxVal = max(pow2, pow3)
print('2 в 8 степени:')
print(pow2)
print('3 в 7 степени:')
print(pow3)
print('Наибольшее:')
print(maxVal)


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
    ast = PythonVisitor().visitProgram(cst)
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    print('------------------------AST tree------------------------')
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    showAstTree(ast)
    generatorVisitor = GeneratorVisitor()
    generatorVisitor.visitProgram(ast)
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    print('--------------------------Code--------------------------')
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    print(generatorVisitor.program)

    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    print('-----------------------Execution------------------------')
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    instruction_table = Machine.get_instruction_table()
    machine_obj = Machine(generatorVisitor.program, instruction_table)
    machine_obj.run()


if __name__ == '__main__':
    main()
