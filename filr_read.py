try:
    f = open("C:/Windows/System32/cmd.exe/demofile.txt", "r")
    print(f.readline())
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("Error: 'demofile.txt' not found. Please ensure the file exists in the specified location.")
