def read_and_write_file(input_file, output_file):
    try:
        # Opens input file in read mode
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content, convert to uppercase)
        modified_content = content.upper()

        # Open output file write mode
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_file}' has been read and modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage
input_filename = 'OneofOne.txt'   # Replace with your input file
output_filename = 'output1.txt' # Replace with your desired output file
read_and_write_file(input_filename, output_filename)


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

