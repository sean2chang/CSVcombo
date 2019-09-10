# Import CSV and OS modules
import csv
import os

# User inputs
option = str(input('Would you like to select individual files to merge or use the directory path to merge files? (I for individual/D for directory)')).lower()
new_file_name = str(input('What do you want the name of the combined file to be?')) + '.csv'

# If options is i, then process individual files
if option == 'i':
    # List Variable
    file_list = []

    # User inputs
    combine_files = file_list.insert(0, str(input('What is the name of the file you want to combine? (No file extension needed)')) + '.csv')
    add_prompt = str(input('Do you want to add more files? (Y/N)')).lower()

    # Additional file inputs
    while add_prompt == 'y':
        print('Here is the current list of files you are combining:')
        print(file_list)
        combine_files = file_list.insert(0, str(input('What other files do you want to combine? (No file extension needed)')) + '.csv')
        add_prompt = str(input('Do you want to add more files? (Y/N)')).lower()

    # User continuation
    print('Here is the current list of files you are combining:')
    print(file_list)
    validate = str(input('Would you like to process these files? (Y/N)')).lower()

    # If approved by user, then process
    if validate == 'y':

        # Pull in only one file
        first_file = file_list[0]
        with open(first_file, 'r') as ff1:
            # Pull in CSV module function DictReader
            d_reader = csv.DictReader(ff1)
            # Get header row in the first file
            headers = d_reader.fieldnames
            with open(new_file_name, 'w', newline='') as ff2:
                csv_writer = csv.writer(ff2, delimiter=',')
                csv_writer.writerow(headers)

        # Read in all files and skip the header row of each file
        for file in file_list:
            with open(file, 'r') as f1:
                csv_reader = csv.reader(f1, delimiter=',')
                with open(new_file_name, 'a', newline='') as f2:
                    csv_writer = csv.writer(f2, delimiter=',')
                    # Skip the header row
                    next(csv_reader, None)
                    for row in csv_reader:
                        csv_writer.writerow(row)
    else:
        print('Please rerun Python script.')

# If options is d, then process all the files in the directory together
elif option == 'd':

    # User input
    file_directory = str(input('What is the path of the files you want to combine? (ex: /users/seanchang/documents/python/projects/combine_csv_files/combine-v2')).lower()

    # Get all files in directory and convert into list
    file_list = os.listdir(file_directory)

    # Get the name of this Python script
    script_name = os.path.basename(__file__)

    # Remove script name from list
    file_list.remove(script_name)

    # Validate list
    print(file_list)
    validate = str(input('Would you like to process these files? (Y/N)')).lower()

    if validate == 'y':
        # Pull in only one file
        first_file = file_list[0]
        with open(first_file, 'r') as ff1:
             d_reader = csv.DictReader(ff1)
             headers = d_reader.fieldnames
             with open(new_file_name, 'w', newline='') as ff2:
                csv_writer = csv.writer(ff2, delimiter=',')
                csv_writer.writerow(headers)

        # Read in all files and skip the header row of each file
        for file in file_list:
             with open(file, 'r') as f1:
                csv_reader = csv.reader(f1, delimiter=',')
                with open(new_file_name, 'a', newline='') as f2:
                    csv_writer = csv.writer(f2, delimiter=',')
                    # Skip the header row
                    next(csv_reader, None)
                    for row in csv_reader:
                        csv_writer.writerow(row)
    else:
        print('Please rerun Python script if you want merge files.')
