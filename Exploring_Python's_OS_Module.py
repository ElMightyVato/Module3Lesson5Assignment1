import os

def list_directory_contents(path):
    try:
        # Get the list of files and directories in the specified path
        entries = os.listdir(path) #Retrieves a list of the entries (files and directories)
        
        if not entries:
            print("The directory is empty.")
        else:
            print(f"Contents of '{path}':")
            for entry in entries:
                full_path = os.path.join(path, entry)
                if os.path.isdir(full_path):
                    print(f"[DIR]  {entry}")
                else:
                    print(f"[FILE] {entry}")
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied: '{path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Prompt the user for the directory path
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)

if __name__ == "__main__":
    main()
