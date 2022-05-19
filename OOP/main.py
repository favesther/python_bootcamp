from prettytable import PrettyTable
table = PrettyTable()
data = {"Pokemon Name": ["Pikachu", "Squirtle", "Charmander"], "Type": ["Electric", "Water", "Fire"]}
for key in data:
    table.add_column(key, data[key])
table.align = "l"
print(table)