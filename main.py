import math

first_name = input('Please enter your first name: ')

def calculate_area_circle():
    radius = float(input('Please enter the radius of the circle: '))
    area = math.pi * radius ** 2
    print(f'The area of the circle is {area}')

def calculate_rectangle_perimeter():
    length = float(input('Please enter the length of the rectangle: '))
    width = float(input('Please enter the width of the rectangle: '))
    perimeter = 2 * (length + width)
    print(f'The perimeter of the rectangle is {perimeter}')

def calculate_average():
    numbers = input('Enter numbers separated by commas: ')
    nums_list = [float(num) for num in numbers.split(',')]
    average = sum(nums_list) / len(nums_list)
    print(f'The average of the numbers is {average}')

def calculate_simple_interest():
    principal = float(input('Please enter the principal amount: '))
    rate = float(input('Please enter the annual interest rate (as a percentage): '))
    time = float(input('Please enter the time (in years): '))
    interest = (principal * rate * time) / 100
    print(f'The simple interest is {interest}')

def calculate_speed():
    distance = float(input('Please enter the distance (in meters): '))
    time = float(input('Please enter the time (in seconds): '))
    speed = distance / time
    print(f'The speed is {speed} m/s')

def main_menu():
    print("\nChoose an option from the following:")
    print("a) Calculate the Area of a Circle")
    print("b) Calculate the Perimeter of a Rectangle")
    print("c) Calculate the Average of Numbers")
    print("d) Calculate Simple Interest")
    print("e) Calculate Speed")

    choice = input("Enter your choice (a, b, c, d, e): ").lower()

    if choice == 'a':
        calculate_area_circle()
    elif choice == 'b':
        calculate_rectangle_perimeter()
    elif choice == 'c':
        calculate_average()
    elif choice == 'd':
        calculate_simple_interest()
    elif choice == 'e':
        calculate_speed()
    else:
        print("Invalid choice. Please select a valid option.")

main_menu()

print(f'Thank you {first_name} for using my App')
