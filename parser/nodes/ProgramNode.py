from .BaseNode import BaseNode


class ProgramNode(BaseNode):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Program"

    def appendChild(self, childNode):
        self.children.append(childNode)
