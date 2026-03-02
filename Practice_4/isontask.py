import json

def simple_json_parser():
    """
    Simple JSON parser for the specific task
    """
    try:
        with open('sample-data.json', 'r') as file:
            data = json.load(file)
        
        # Print header exactly as specified
        print("Interface Status")
        print("=" * 80)
        print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
        print("-" * 50 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6)
        
        # Parse and print each interface
        for item in data['imdata']:
            attrs = item['l1PhysIf']['attributes']
            dn = attrs['dn']
            desc = attrs.get('descr', '')
            speed = attrs.get('speed', 'inherit')
            mtu = attrs.get('mtu', '')
            
            print(f"{dn:<50} {desc:<20} {speed:<8} {mtu:<6}")
            
    except FileNotFoundError:
        print("Error: sample-data.json not found!")
        print("\nCreating sample file for you...")
        create_sample_json()
    except KeyError as e:
        print(f"Error: JSON structure doesn't match expected format. Missing key: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    simple_json_parser()