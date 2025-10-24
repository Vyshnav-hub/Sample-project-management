def grade(percent):
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    elif percent >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Grade Calculator!")
    name = input("Enter student name: ")
    try:
        percent = float(input("Enter percentage (0-100): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    g = grade(percent)
    print(f"{name}: {percent}% = Grade {g}")
    with open("results.txt", "a") as f:
        f.write(f"{name},{percent},{g}\n")
      if __name__=="__main__":
        main()
print("Thank you for using the Grade Calculator!")
