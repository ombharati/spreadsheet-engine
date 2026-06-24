import re

cells = {}

def set_cell(address, value):
    """Set a cell to a value or formula"""
    cells[address] = value

def get_cell(address):
    """Get cell value, evaluating formulas if needed"""
    if address not in cells:
        return "Cell not found"
    
    value = cells[address]
    
    # Check if it's a formula
    if isinstance(value, str) and value.startswith("="):
        return evaluate_formula(value)
    
    return value

def evaluate_formula(formula):
    """Evaluate a formula string"""
    # Remove the "=" prefix
    expr = formula[1:].strip()
    
    # Support SUM(A1:A5), AVERAGE(A1:A5), etc.
    expr = expr.upper()
    
    try:
        # Replace cell references with their values
        expr = replace_cell_references(expr)
        
        # Handle SUM function
        expr = re.sub(r'SUM\((.*?)\)', lambda m: str(sum_range(m.group(1))), expr)
        
        # Handle AVERAGE function
        expr = re.sub(r'AVERAGE\((.*?)\)', lambda m: str(average_range(m.group(1))), expr)
        
        # Handle MIN function
        expr = re.sub(r'MIN\((.*?)\)', lambda m: str(min_range(m.group(1))), expr)
        
        # Handle MAX function
        expr = re.sub(r'MAX\((.*?)\)', lambda m: str(max_range(m.group(1))), expr)
        
        # Evaluate the expression
        result = eval(expr)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def replace_cell_references(expr):
    """Replace cell references like A1, B2 with their values"""
    def replace_ref(match):
        cell_ref = match.group(0).upper()
        value = cells.get(cell_ref, 0)
        # Try to convert to number
        try:
            return str(float(value) if isinstance(value, str) else value)
        except:
            return "0"
    
    return re.sub(r'[A-Z]\d+', replace_ref, expr)

def parse_range(range_str):
    """Parse range like A1:A5 into list of cell addresses"""
    range_str = range_str.strip().upper()
    if ':' not in range_str:
        return [range_str]
    
    start, end = range_str.split(':')
    start_col = start[0]
    start_row = int(start[1:])
    end_col = end[0]
    end_row = int(end[1:])
    
    cells_in_range = []
    for row in range(start_row, end_row + 1):
        cells_in_range.append(f"{start_col}{row}")
    
    return cells_in_range

def sum_range(range_str):
    """Calculate SUM of a range"""
    cell_list = parse_range(range_str)
    total = 0
    for cell_addr in cell_list:
        try:
            val = cells.get(cell_addr, 0)
            total += float(val) if isinstance(val, str) else val
        except:
            pass
    return total

def average_range(range_str):
    """Calculate AVERAGE of a range"""
    cell_list = parse_range(range_str)
    values = []
    for cell_addr in cell_list:
        try:
            val = cells.get(cell_addr, 0)
            values.append(float(val) if isinstance(val, str) else val)
        except:
            pass
    return sum(values) / len(values) if values else 0

def min_range(range_str):
    """Calculate MIN of a range"""
    cell_list = parse_range(range_str)
    values = []
    for cell_addr in cell_list:
        try:
            val = cells.get(cell_addr, 0)
            values.append(float(val) if isinstance(val, str) else val)
        except:
            pass
    return min(values) if values else 0

def max_range(range_str):
    """Calculate MAX of a range"""
    cell_list = parse_range(range_str)
    values = []
    for cell_addr in cell_list:
        try:
            val = cells.get(cell_addr, 0)
            values.append(float(val) if isinstance(val, str) else val)
        except:
            pass
    return max(values) if values else 0

def display_cells():
    """Display all cells and their values"""
    if not cells:
        print("No cells set yet")
    else:
        for addr in sorted(cells.keys()):
            value = cells[addr]
            display_value = get_cell(addr)
            if isinstance(value, str) and value.startswith("="):
                print(f"{addr}: {value} = {display_value}")
            else:
                print(f"{addr}: {value}")

def help_menu():
    """Display available commands"""
    print("\n=== Available Commands ===")
    print("SET <cell> <value>     - Set cell to a value (e.g., SET A1 10)")
    print("SET <cell> =<formula>  - Set cell to a formula (e.g., SET C1 =A1+B1)")
    print("GET <cell>             - Get cell value (e.g., GET A1)")
    print("SHOW                   - Display all cells")
    print("HELP                   - Show this menu")
    print("EXIT                   - Quit")
    print("\n=== Supported Functions ===")
    print("SUM(A1:A5)      - Sum a range")
    print("AVERAGE(A1:A5)  - Average of a range")
    print("MIN(A1:A5)      - Minimum value in range")
    print("MAX(A1:A5)      - Maximum value in range")
    print("Basic math: +, -, *, /, ** (power)")
    print()

def main():
    print("=== Spreadsheet Engine ===")
    print("Type HELP for available commands\n")
    
    while True:
        user_input = input("> ").strip()
        
        if not user_input:
            continue
        
        parts = user_input.split(maxsplit=2)
        command = parts[0].upper()
        
        if command == "EXIT":
            print("Goodbye!")
            break
        elif command == "HELP":
            help_menu()
        elif command == "SET" and len(parts) == 3:
            address, value = parts[1].upper(), parts[2]
            set_cell(address, value)
            print(f"Set {address} = {value}")
        elif command == "GET" and len(parts) == 2:
            address = parts[1].upper()
            result = get_cell(address)
            print(f"{address} = {result}")
        elif command == "SHOW":
            display_cells()
        else:
            print("Invalid command. Type HELP for available commands.")

if __name__ == "__main__":
    main()
