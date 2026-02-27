import importlib

def classify_attribute(module_path, attr_name):
    try:
        # Try to import the module
        module = importlib.import_module(module_path)
        
        # Check if the module has the attribute
        if hasattr(module, attr_name):
            attr = getattr(module, attr_name)
            # Check if it's callable
            if callable(attr):
                return "CALLABLE"
            else:
                return "VALUE"
        else:
            return "ATTRIBUTE_NOT_FOUND"
            
    except ImportError:
        return "MODULE_NOT_FOUND"
    except Exception:
        # Catch any other unexpected errors
        return "MODULE_NOT_FOUND"

def solve():
    # Read number of queries
    n = int(input().strip())
    
    # Process each query
    for _ in range(n):
        module_path, attr_name = input().strip().split()
        result = classify_attribute(module_path, attr_name)
        print(result)

# Run the solution
solve()