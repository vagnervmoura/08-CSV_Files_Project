"""1. Get the file path from the user, load and display the data."""

# python main_CSV.py in.csv out.csv "0;0;piano" "3;1;mug" "1;2;17" "3;3;0"

import sys
import os
from functions import (
    read_csv_file,
    display_table,
    validate_field_selection,
    save_csv_file
)


def main():  
    if len(sys.argv) < 2: # To check if the user provided the arguments to run. EX.: python reader.py in.csv
        print("Please provide the file path for us to work with.")
        sys.exit

    file_path = sys.argv[1] # [1] = Is the second argument on the TERMINAL  |  python [0]reader.py [1]in.csv [2]"0;0;piano" "3;1;mug" "1;2;17" "3;3;0"
    save_file_path = sys.argv[2] # [2] = is the Third argument on the TERMINAL  |  python [0]reader.py [1]in.csv [2]out.csv [3]"0;0;piano" "3;1;mug" "1;2;17" "3;3;0"
    
    # VALIDATE SAVE_FILE_PATH
    if not save_file_path.endswith('.csv'):
        print(f"Target file path not valid: {save_file_path}")
        sys.exit()

    if not os.path.exists(file_path) or not os.path.isfile(file_path): # To check if the file that user is looking for into the folder does not exist on folder OR if it is not an file, EX.: it is an Folder.
        print(f"The path dos not lead to a file or does not exist: {file_path}") 
        print(f"Available files:") # Print available files on folder
        for fn in os.listdir(): # Para os files into folder send to FileName 'FN'
            if fn.endswith(".py") or os.path.isdir(fn): # if the FN ends with '.py' or if the file is and directory, does not show on print.
                continue
            print(f" - {fn}") # Print all the files availables on folder
    else:
        # READ
        table = read_csv_file(file_path)
        
#        # DISPLAY    
#        display_table(table, separator="=")
        
        # LOAD CHANGES
        # python reader.py in.csv "0;0;piano" "3;1;mug" "1;2;17" "3;3;0"
        #                        [1c][1r]   [4c][2r]  [2c][3r]
        changes = sys.argv[3:]
        if not changes:
            print("No changes to be made were provided, try again.")
            sys.exit()
            
        print()
        
        for chg in changes:
            # X = column  |  Y = row   |  VAL = value
            x, y, val = chg.split(';') # y = Row Index  |  x = Column Index  |  val = Value  | chg = Change
            y = int(y)
            x = int(x)          
            
            # VALIDATION OF THE INPUT DATA
            validate_field_selection(x, y, table)        
            
#            # DISPLAY THE CHANGE INFORMATION
#            value_to_be_changed = table[y][x]
#            print(f"Changing {value_to_be_changed} into {val}...")

            # DO THE CHANGE
            table[y][x] = val

        display_table(table)  
            
        # SAVE TO THE NEW FILE
        # python reader.py in.csv out.csv "0;0;piano" "3;1;mug" "1;2;17" "3;3;0"
        save_csv_file(table, save_file_path)
        
if __name__ == "__main__":
    main()