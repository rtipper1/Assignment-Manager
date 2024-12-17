from modules.Course import Course
from modules.Category import Category
from modules.Assignment import Assignment

def main():
    course1 = Course("ECE 302", 4, [])
    print(course1.get_categories())


if __name__ == "__main__":
    main()