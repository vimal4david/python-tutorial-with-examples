"""
Python Indentation Tutorial

Python uses indentation to define code blocks instead of curly braces or keywords.
Key rules:
- Use 4 spaces per indentation level (PEP 8 standard)
- Be consistent throughout your code
- Indentation is mandatory for code blocks (functions, loops, conditionals, etc.)
- Mixing tabs and spaces will cause errors
"""
def function_with_indentation():
        print("pass")
        pass


def function_if_two_is_greater_than_zero():
    if 2>0:
        print("2 is greater than 0")


def function_if_two_is_greater_two_statements():
    if 2>0:
        print("2 is greater than 0")
        print("This is another statement")

if __name__ == "__main__":
    function_with_indentation()
    function_if_two_is_greater_than_zero()
    function_if_two_is_greater_two_statements()

