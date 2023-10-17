import csv
import sys

def read_csv_file(file_path):
    table = []
    with open(file_path, "r") as file: # If the file that user is looking for into the folder, exists, shows the file.
        reader = csv.reader(file)
        for row in reader:
            table.append(row) # To add data from the file to the TABLE list.
    return table
 
 
def display_table(table, separator="-"):
    print_tpl = "| {:<10.10s} | {:<10.10s} | {:<10.10s} | {:<10.10s} |" # To create an Template to print the file. {:<10.10s} especify the size of each colums.
#    print(53 * separator)
#    for row in reader:
#    print(print_tpl.format(table[0][0], table[0][1], table[0][2], table[0][3])) # Here will print table where [0][1] [0]-Is the line and [1]-Is the first, second and third element from the line.
#            break
    print("┌" + 12 * separator + "┬" + 12 * separator + "┬" + 12 * separator + "┬" + 12 * separator + "┐")
    tab_len = len(table)
    for row in table:
        tab_len -= 1
        print(print_tpl.format(row[0], row[1], row[2], row[3]))
        if tab_len > 0:
            print("├" + 12 * separator + "┼" + 12 * separator + "┼" + 12 * separator + "┼" + 12 * separator + "┤")  
        else:
            print("└" + 12 * separator + "┴" + 12 * separator + "┴" + 12 * separator + "┴" + 12 * separator + "┘")
 
def validate_field_selection(x, y, table):
    if len(table) < y:
        print(f"Not enough rows. Asked for: {y}, available: {len(table)}")
        sys.exit()
    if len(table[y]) < x:
        print(f"Not enough columns. Asked for: {x}, available: {len(table[y])}")
        sys.exit()
          
        
def save_csv_file(table, save_file_path):
    with open(save_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(table)