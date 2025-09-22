import os
from dotenv import load_dotenv

load_dotenv(".env")

file_count = 0
rename_count = 0
old_char = ''
new_char = ''

path = os.getenv("folder_path")

def main():
    # for accessing the global variables
    global file_count
    global rename_count
    global old_char
    global new_char

    # to what to change it to 
    old_char = ' '
    new_char = '-'

    Rename(path, old_char, new_char)

    print(f"File Count: {file_count}")
    print(f"Rename Count: {rename_count}")

# old = the character in the filename we want to replace
# new = the new character we want to replace the "old" with
def Rename(path, old, new):
    global file_count
    global rename_count

    items = os.listdir(path)

    for item in items:
        # getting the path for each item
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            # recursively calls the function until the item is not a folder
            Rename(item_path, old, new)
        else:
            new_name = ""
            file_count += 1

            # checking if the thing 
            if old in item:
                # making the desired changes 
                new_name = item.replace(old, new)   
                rename_count += 1

                # modifying the item path with the new_name
                updated_path = os.path.join(path, new_name)

                # renaming
                os.rename(item_path, updated_path)


main()