from compiler.parser.nodes import BaseNode


def showAstTree(rootNode: BaseNode):
    __visit(rootNode)


def __visit(node: BaseNode, depth=0):
    prefix = '  ' * depth
    print(prefix + str(node))
    for child in node.children:
        if child:
            __visit(child, depth + 1)
