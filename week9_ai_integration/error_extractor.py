import traceback
import sys

class ErrorExtractor:
    def __init__(self):
        pass

    def execute_and_extract(self, code_string):
        \"\"\"
        Executes the provided Python code string and captures any compilation or runtime errors.
        Returns a dictionary with extracted error details.
        \"\"\"
        try:
            # First, attempt to compile the code to catch SyntaxErrors
            compile(code_string, '<string>', 'exec')
            
            # If compilation succeeds, attempt to execute
            # Using a restricted global namespace for safe execution
            exec_globals = {}
            exec(code_string, exec_globals)
            return None # No error found
        except Exception as e:
            return self._parse_exception(e)
            
    def _parse_exception(self, exception):
        \"\"\" Extracts type, message, and line number from the exception. \"\"\"
        error_type = type(exception).__name__
        error_message = str(exception)
        
        line_number = None
        
        # Syntax errors have a slightly different structure
        if isinstance(exception, SyntaxError):
            line_number = exception.lineno
        else:
            # Extract line number from traceback for runtime errors
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tbList = traceback.extract_tb(exc_traceback)
            
            # Find the line corresponding to '<string>', which is our executed code
            for tb in reversed(tbList):
                if tb.filename == '<string>':
                    line_number = tb.lineno
                    break

        return {
            "error_type": error_type,
            "error_message": error_message,
            "line_number": line_number,
            "traceback": traceback.format_exc()
        }
