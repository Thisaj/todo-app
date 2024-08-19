while True:
    try:
        width = float(input("Enter rectangle width: "))
        height = float(input("Enter rectangle height: "))
        area = width * height
        if width == height:
            exit("error width and height are equal")
        print("The area of the rectangle is", area)
        break;
    except ValueError:
        print("Please enter a number")
