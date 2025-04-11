def main():
    # Read file "informacion.txt"
    with open("./informacion.txt", "r") as file:
        info_file = file.read()

    # Print the information
    print(info_file)

if __name__ == "__main__":
    main()