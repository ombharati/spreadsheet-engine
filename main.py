cells = {}

def set_cell(address, value):
    cells[address] = value

def get_cell(address):
    return cells[address]

set_cell("A1", 10)
set_cell("B1", 20)

print(get_cell("A1"))
print(get_cell("B1"))
