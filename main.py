def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.writelines(["Hello! My Name is Gilbert", "\nI am 35 years old", "\ncurrently enjoying learning python at plp"])
    except FileNotFoundError:
        print("File not found or directory does not exist.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File creation process completed.")


def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found or directory does not exist.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File reading process completed.")


def append_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.writelines(["\nApart from coding i also love nature walks,", "\nMoney matters more in the insurance industry", "\nLastly I love cool gospel music, i am a true beliver or Jesus "])
    except FileNotFoundError:
        print("File not found or directory does not exist.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()  
