"""
A stack machine processes instructions by pushing and popping values to an internal stack. A simple example of this is a calculator.

The argument passed to run(instructions) will always be a string containing a series of instructions. 
The instruction set of the calculator will be this:

+: Pop the last 2 values from the stack, add them, and push the result onto the stack.
-: Pop the last 2 values from the stack, subtract the lower one from the topmost one, and push the result.
*: Pop the last 2 values, multiply, and push the result.
/: Pop the last 2 values, divide the topmost one by the lower one, and push the result.
DUP: Duplicate (not double) the top value on the stack.
POP: Pop the last value from the stack and discard it.
PSH: Performed whenever a number appears as an instruction. Push the number to the stack.
Any other instruction (for example, a letter) should result in the value "Invalid instruction: [instruction]"
Examples:

"" ➞ 0

"5 6 +" ➞ 11

"3 DUP +" ➞ 6

"6 5 5 7 * - /" ➞ 5

"x y +" ➞ Invalid instruction: x
"""

# class Calculator:
#     def __init__(self, input_stack: str) -> None:
#         self.input_stack = input_stack

#     def print_stack(self):
#         print(self.input_stack)

#     def split_stack_to_list(self):
#         splited_str = self.input_stack.split(' ')
#         print(splited_str)

#     def add_two_last_values(self):


# first_stack = Calculator('2 6 +')







