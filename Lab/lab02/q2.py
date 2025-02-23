# A Python program to calculate the area of simple shapes.

# initiate the variable area
area = 0 

def get_rectangle_area(length, width):
    # calculate the area of a rectangle
    global area
    area = length * width
    return area

def get_triangle_area(base, height):
    # calculate the area of a triangle
    global area
    area = 0.5 * base * height
    return area

def get_circle_area(radius):
    # calculate the area of a circle
    global area
    area = 3.14 * radius ** 2
    return area

def main():
    # print the program title
    print("Area calculator of simple shapes")
    shape = str(input("Enter the shape desired: "))
    
    if shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        get_rectangle_area(length, width)
    
    elif shape == "right triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        get_triangle_area(base, height)  
    
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        get_circle_area(radius)
    
    print("The area is: ", area, sep = "")

if __name__ == "__main__":
    main()      