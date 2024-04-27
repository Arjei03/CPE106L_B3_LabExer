"""
CPE106L - B3
    GROUP1:
        BRIOL
        CACANANTA
        GUTIERREZ
"""
fileName = input('Enter file name: ')
lines = []
try:
    with open(fileName, 'r') as f:
        for line in f:
            lines.append(line.strip())
        print("The file has", len(lines), "lines.")
        while True:
            lineNumber = int(input("Enter a line number [0 to quit]: "))
            if lineNumber == 0:
                break
            elif lineNumber < 0 or lineNumber > len(lines):
                print("ERROR: line number must be between 1 and", len(lines))
            else:
                print("Line", lineNumber, ": ", lines[lineNumber - 1])
except FileNotFoundError:
    print("File not found. Please make sure the file exists and try again.")
except ValueError:
    print("Invalid input. Please enter a valid line number.")
