import ast

class ASTParser:
    def __init__(self):
        pass

    def parse_code(self, code_string):
        \"\"\"
        Returns the AST tree from the source code.
        If there's a syntax error, returns None.
        \"\"\"
        try:
            return ast.parse(code_string)
        except SyntaxError:
            return None

    def get_node_by_line(self, code_string, line_number):
        \"\"\"
        Finds and returns the AST node responsible for the error at the given line number. 
        Also returns the AST node type name.
        \"\"\"
        if line_number is None:
            return None, "Unknown"
            
        tree = self.parse_code(code_string)
        if not tree:
            # Fallback if AST can't even be parsed completely due to SyntaxError
            return None, "SyntaxError Node"
            
        target_node = None
        for node in ast.walk(tree):
            if hasattr(node, "lineno") and node.lineno == line_number:
                # We want the deepest matching node, keep tracking
                target_node = node
                
        if target_node:
            return target_node, type(target_node).__name__
            
        return None, "Unknown"

    def extract_related_variables(self, code_string, line_number):
        \"\"\" Extract variables involved in the error line using AST. \"\"\"
        node, _ = self.get_node_by_line(code_string, line_number)
        variables = []
        if node:
            for child in ast.walk(node):
                if isinstance(child, ast.Name):
                    variables.append(child.id)
        return list(set(variables))
