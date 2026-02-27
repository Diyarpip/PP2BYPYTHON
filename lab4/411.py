import json

def apply_patch(source, patch):
    if not isinstance(source, dict) or not isinstance(patch, dict):
        return patch
    
    for key, value in patch.items():
        if value is None:
            # Remove key if present
            if key in source:
                del source[key]
        elif key not in source:
            # Add new key
            source[key] = value
        elif isinstance(source[key], dict) and isinstance(value, dict):
            # Both objects, recurse
            apply_patch(source[key], value)
        else:
            # Replace value
            source[key] = value
    
    return source

def main():
    src_str = input().strip()
    patch_str = input().strip()
    
    source = json.loads(src_str)
    patch = json.loads(patch_str)
    
    result = apply_patch(source, patch)
    
    # Compact JSON with sorted keys
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))

if __name__ == "__main__":
    main()