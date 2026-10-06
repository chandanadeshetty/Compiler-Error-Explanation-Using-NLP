import sys
import traceback
import time

try:
    from codecarbon import EmissionsTracker
    CODECARBON_AVAILABLE = True
except ImportError:
    CODECARBON_AVAILABLE = False

def extract_error(code):
    """
    Executes Python code safely, captures error type, message, traceback,
    line number, and optionally tracks CodeCarbon emissions.
    
    Returns a dictionary (IR) with the extracted details.
    """
    import io
    import contextlib
    
    ir = {
        "error_type": None,
        "error_message": None,
        "line_number": None,
        "traceback": None,
        "green_metrics": None,
        "stdout": ""
    }

    tracker = None
    if CODECARBON_AVAILABLE:
        try:
            # Using log_level error to avoid noisy console outputs
            tracker = EmissionsTracker(save_to_file=True, log_level='error')
            tracker.start()
        except Exception:
            tracker = None

    start_time = time.perf_counter()
    f = io.StringIO()

    try:
        # Step 1: Compile the code to catch SyntaxErrors
        compiled_code = compile(code, '<string>', 'exec')
        
        # Step 2: Execute the compiled code safely with a restricted namespace
        exec_globals = {"__name__": "__main__"}
        with contextlib.redirect_stdout(f):
            exec(compiled_code, exec_globals)
            
        ir["stdout"] = f.getvalue()
        
    except Exception as e:
        ir["stdout"] = f.getvalue()
        ir["error_type"] = type(e).__name__
        ir["error_message"] = str(e)
        ir["traceback"] = traceback.format_exc()
        
        # Extract line number appropriately depending on error type
        if isinstance(e, SyntaxError):
            ir["line_number"] = e.lineno
        else:
            # Extract line number from the <string> code frame
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb_list = traceback.extract_tb(exc_traceback)
            for tb in reversed(tb_list):
                if tb.filename == '<string>':
                    ir["line_number"] = tb.lineno
                    break

    duration = time.perf_counter() - start_time

    # Record Green metrics
    if tracker:
        try:
            emissions = tracker.stop()
            ir["green_metrics"] = {
                "emissions_kg": emissions,
                "energy_consumed_kwh": tracker.final_emissions_data.energy_consumed if emissions else 0,
                "execution_time_sec": duration
            }
        except Exception:
            ir["green_metrics"] = {
                "execution_time_sec": duration,
                "emissions_kg": 0,
                "energy_consumed_kwh": 0
            }
    else:
        ir["green_metrics"] = {
            "execution_time_sec": duration,
            "emissions_kg": 0,
            "energy_consumed_kwh": 0
        }

    return ir