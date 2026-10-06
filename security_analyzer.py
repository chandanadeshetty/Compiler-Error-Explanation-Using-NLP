import ast

class SecurityAnalyzer:
    def __init__(self):
        """
        Week 10: Security Enforcement Mechanism
        Implements static analysis using Python's AST to detect 4 major vulnerabilities:
        1. Command Injection (e.g., os.system)
        2. Arbitrary Code Execution (e.g., eval, exec)
        3. Insecure Temporary Files (e.g., tempfile.mktemp)
        4. Hardcoded Secrets (e.g., variables named 'password', 'secret', 'apikey')
        """
        pass

    def scan_code(self, code_string):
        """
        Parses the code string and returns a list of detected vulnerabilities.
        """
        vulnerabilities = []
        try:
            tree = ast.parse(code_string)
        except SyntaxError:
            # If code is too structurally broken to parse, we must skip deep analysis
            return vulnerabilities

        for node in ast.walk(tree):
            
            # Vulnerability 1: Command Injection
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'system':
                    vulnerabilities.append({
                        "type": "Command Injection",
                        "severity": "CRITICAL",
                        "message": "os.system() detected. Risk of shell command injection.",
                        "line": getattr(node, 'lineno', 'Unknown')
                    })
                    
            # Vulnerability 2: Arbitrary Code Execution
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ['eval', 'exec']:
                    vulnerabilities.append({
                        "type": "Arbitrary Code Execution",
                        "severity": "HIGH",
                        "message": f"{node.func.id}() detected. Risk of running untrusted code.",
                        "line": getattr(node, 'lineno', 'Unknown')
                    })
                    
            # Vulnerability 3: Insecure Temporary Files
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'mktemp':
                    vulnerabilities.append({
                        "type": "Insecure Temp File",
                        "severity": "MEDIUM",
                        "message": "mktemp() is insecure. Use tempfile.mkstemp() instead.",
                        "line": getattr(node, 'lineno', 'Unknown')
                    })

            # Vulnerability 4: Hardcoded Secrets
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id.lower()
                        if any(secret in var_name for secret in ['password', 'secret', 'api_key', 'token']):
                            vulnerabilities.append({
                                "type": "Hardcoded Secret",
                                "severity": "LOW",
                                "message": f"Potential hardcoded secret detected in variable '{target.id}'.",
                                "line": getattr(target, 'lineno', 'Unknown')
                            })

        return vulnerabilities
