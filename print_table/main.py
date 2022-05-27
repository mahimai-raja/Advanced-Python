from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Name', 'Department', 'Year']
table.add_row(['Mahimai', 'CSE', 'Third'])
table.add_row(['Raja', 'ECE', 'Second'])
table.add_row(['iKurious', 'AI', 'Final'])

print(table)