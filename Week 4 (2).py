def ask_for_filename():
    filename = input("enter the filename to read: ")

    try:
        # Attempt to open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


ask_for_filename()