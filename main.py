cells = {}

def set_cell(address, value):
    cells[address] = value

def get_cell(address):
    return cells.get(address, "Cell not found")

def display_cells():
    if not cells:
        print("No cells set yet")
    else:
        for addr, val in sorted(cells.items()):
            print(f"{addr}: {val}")

def main():
    print("=== Spreadsheet Engine ===")
    print("Commands: SET <cell> <value>, GET <cell>, SHOW, EXIT")
    print()
    
    while True:
        user_input = input("> ").strip().upper()
        
        if not user_input:
            continue
        
        parts = user_input.split(maxsplit=2)
        command = parts[0]
        
        if command == "EXIT":
            print("Goodbye!")
            break
        elif command == "SET" and len(parts) == 3:
            address, value = parts[1], parts[2]
            set_cell(address, value)
            print(f"Set {address} = {value}")
        elif command == "GET" and len(parts) == 2:
            address = parts[1]
            print(get_cell(address))
        elif command == "SHOW":
            display_cells()
        else:
            print("Invalid command. Try: SET A1 10, GET A1, SHOW, or EXIT")

if __name__ == "__main__":
    main()
