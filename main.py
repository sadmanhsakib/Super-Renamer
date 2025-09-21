import os
from dotenv import load_dotenv

load_dotenv(".env")

counter = 0
path = os.getenv("folder_path")

def main():
    rename_counter = Rename(path)
    print(f"File Renamed: {rename_counter}")


def Rename(path):
    global counter
    items = os.listdir(path)

    for item in items:
        # getting the path for each item
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            # recursively calls the function until the item is not a folder
            Rename(item_path)
        else:
            counter += 1

            # making the desired changes 
            new_name = item.replace("!", "")
            new_name = new_name.lower()

            # modifying the item path with the new_name
            updated_path = os.path.join(path, new_name)

            # renaming
            os.rename(item_path, updated_path)
    return counter


main()