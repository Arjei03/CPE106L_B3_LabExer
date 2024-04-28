def main():
    fileName = input("Enter filename: ")
    try:
        with open(fileName, 'r') as file:
            print("File Contents:")
            for line in file:
                print(line.strip())
            
            print("End of file.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
