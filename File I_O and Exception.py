
def read_items(file_name):
    try:
        with open(file_name, 'r') as file:
            items = file.read().splitlines()
            return items
    except FileNotFoundError:
        print("File doesn't exist")
        return[]
    except Exception as e:
        print(f"Error occurred by {str(e)}")
        return[]
    
def save_items(file_name, items):
    try:
        with open(file_name, 'w') as file:
            file.write('\n'.join(items))
            print("Items saved")
    except Exception as e:
        print(f"Error occurred by {str(e)}")

def main():
    file_name = 'items.txt'
    items = read_items(file_name)

    print("Items loaded:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    new_item = input("Enter a new item: ")
    items.append(new_item)

    save_items(file_name, items)

    print("\nUpdated List:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

if __name__ == "__main__":
    main()
