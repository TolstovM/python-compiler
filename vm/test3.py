from .machine import *

program = [
    'START',
    'PUSH', 100,
    'STORE', 'a',
    'PUSH', 30,
    'STORE', 'b',
    'LOAD', 'a',
    'LOAD', 'b',
    'ISGT',
    'JUMP_IF', 22,
    'LOAD', 'b',
    'STORE', 'c',
    'JUMP', 26,
    'LOAD', 'a',
    'STORE', 'c',
    'LOAD', 'c',
    'FUNC', 'print', 1,
    'HALT'
]
instruction_table = Machine.get_instruction_table()

machine = Machine(program, instruction_table)
machine.run()
