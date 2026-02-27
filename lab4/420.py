def solve():
    # Read number of commands
    m = int(input().strip())
    
    # Initialize variables
    g = 0  # global variable
    n = 0  # outer function's variable
    
    # Process each command
    for _ in range(m):
        scope, value_str = input().strip().split()
        value = int(value_str)
        
        if scope == "global":
            g += value
        elif scope == "nonlocal":
            n += value
        elif scope == "local":
            # Local variable - does nothing to g or n
            # In a real implementation, this would create a local variable
            # but since we only need final g and n, we can ignore it
            pass
    
    # Output final values
    print(g, n)

# Run the solution
solve()