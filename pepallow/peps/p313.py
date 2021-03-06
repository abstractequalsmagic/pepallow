import ast
from pepallow import HandledTransformer

try:
    # Try original version first.
    from romana.romana import roman
except ImportError:
    from pepallow.romana import roman


NUMBER = 313
SUPPRESS = (NameError,)


class PEP313Transformer(HandledTransformer):
    """
    PEP313 => Adding Roman Numeral Literals to Python
    
    I => 1
    IV => 4
    M => 1000
    """

    def visit_Name(self, node):
        number = roman(node.id)
        if number:
            return ast.Num(number)
        return node
