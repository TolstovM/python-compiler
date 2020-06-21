class BaseNode:

    def __init__(self, value=None):
        self.children = []
        self.value = value

    def __str__(self):
        return str(self.value)
