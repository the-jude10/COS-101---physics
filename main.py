import math

first_name = input('Please enter your first name: ')

def calculate_volume_sphere():
    radius = float(input('Please enter the radius of the sphere: '))
    volume = (4/3) * math.pi * radius ** 3
    print(f'The volume of the sphere is {volume}')

def calculate_triangle_area():
    base = float(input('Please enter the base of the triangle: '))
    height = float(input('Please enter the height of the triangle: '))
    area = 0.5 * base * height
    print(f'The area of the triangle is {area}')

def calculate_median():
    numbers = input('Enter numbers separated by commas: ')
    nums_list = sorted([float(num) for num in numbers.split(',')])
    n = len(nums_list)
    if n % 2 == 1:
        median = nums_list[n // 2]
    else:
        median = (nums_list[n // 2 - 1] + nums_list[n // 2]) / 2
    print(f'The median of the numbers is {median}')

def calculate_compound_interest():
    principal = float(input('Please enter the principal amount: '))
    rate = float(input('Please enter the annual interest rate (as a percentage): '))
    time = float(input('Please enter the time (in years): '))
    n = int(input('Please enter the number of times interest is compounded per year: '))
    compound_interest = principal * (1 + rate / (100 * n)) ** (n * time) - principal
    print(f'The compound interest is {compound_interest}')

def calculate_acceleration():
    initial_velocity = float(input('Please enter the initial velocity (in m/s): '))
    final_velocity = float(input('Please enter the final velocity (in m/s): '))
    time = float(input('Please enter the time (in seconds): '))
    acceleration = (final_velocity - initial_velocity) / time
    print(f'The acceleration is {acceleration} m/s²')

def main_menu():
    print("\nChoose an option from the following:")
    print("a) Calculate the Volume of a Sphere")
    print("b) Calculate the Area of a Triangle")
    print("c) Calculate the Median of Numbers")
    print("d) Calculate Compound Interest")
    print("e) Calculate Acceleration")

    choice = input("Enter your choice (a, b, c, d, e): ").lower()

    if choice == 'a':
        calculate_volume_sphere()
    elif choice == 'b':
        calculate_triangle_area()
    elif choice == 'c':
        calculate_median()
    elif choice == 'd':
        calculate_compound_interest()
    elif choice == 'e':
        calculate_acceleration()
    else:
        print("Invalid choice. Please select a valid option.")

main_menu()

print(f'Thank you {first_name} for using my App')
