
while True:
    # 🖼️ Python Pattern Drawing Project

    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))
    rows = 0
    size = 0
    width = 0
    height = 0

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))
    elif choice == 8:
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        #Loop through rows and print increasing stars
        for row in range(1, rows + 1):
            print("*" * row)

    elif choice == 2:  # Square with Hollow Center
        #Create a square with a hollow center
        for line in range(1, size + 1):
            if line == 1 or line == size:
                print("*" * size)
            else:
                print("*" + " " * (size - 2) + "*")


    elif choice == 3:  # Diamond
        #Create a diamond shape using loops
        if rows % 2 != 0:
            space = rows // 2
            stars = 1
            for row in range(1, rows + 1, 2):
                print(" " * space + "*" * stars)
                space -= 1
                stars += 2
            space = 1
            stars = rows - 2
            for low_row in range(rows - 1, 0, -2):
                print(" " * space + "*" * stars)
                space += 1
                stars -= 2
        else:
            space = rows // 2
            stars = 2
            for row in range(1, rows + 1, 2):
                print(" " * space + "*" * stars)
                space -= 1
                stars += 2
            space = 1
            stars = rows
            for low_row in range(rows, 0, -2):
                print(" " * space + "*" * stars)
                space += 1
                stars -= 2

    elif choice == 4:  # Left-angled Triangle
        #Print decreasing stars for each row
        for row in range(rows, 0, -1):
            print("*" * row)



    elif choice == 5:  # Hollow Square
        #Similar to choice 2 but ensure perfect square logic
        for line in range(1, size + 1):
            if line == 1 or line == size:
                print("* " * (size - 1) + "*")
            else:
                print("*" + " " * (size * 2 - 3) + "*")

    elif choice == 6:  # Pyramid
        #Center-align stars to form a pyramid
        space = rows - 1
        stars = 1
        for row in range(1, rows * 2 + 1, 2):
            print(" " * space + "*" * stars)
            space -= 1
            stars += 2


    elif choice == 7:  # Reverse Pyramid
        #Create an upside-down pyramid
        space = 0
        stars = rows * 2 - 1
        for row in range(rows * 2 - 1, 0, -2):
            print(" " * space + "*" * stars)
            space += 1
            stars -= 2

    elif choice == 8:  # Rectangle with Hollow Center
        #Handle separate width and height inputs for rectangle
        for star in range(1, height + 1):
            if star == 1 or star == height:
                print("* " * (width - 1) + "*")
            else:
                print("*" + " " * (width * 2 - 3) + "*")

    else:
        print("❌ Invalid choice! Please restart the program.")

    # Step 5: Optional - Allow the user to restart or exit
    print("Would you like to continue? - Y/N")
    answer_y_n = input()
    if answer_y_n == "N":
        break

