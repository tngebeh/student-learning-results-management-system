"""
STUDENT LEARNING AND RESULTS MANAGEMENT SYSTEM
Domain: Education
Course: Object-Oriented Programming

Assignment requirements:
1. Classes, attributes, objects, and object interaction.
2. Instance methods, class methods, and a static method.
3. Dictionaries as the only collection data structure.
4. Student registration, course enrollment, and result recording.
5. Input validation and privacy-conscious design.
6. Digital Public Goods (DPG) principles.

Note:
Sample records are fictional.
Grade boundaries are illustrative, not official university policy.
Records are stored in memory and disappear when the program closes.
"""


# =====================================================
# CLASS 1: COURSE
# =====================================================

class Course:
    """Represent a course offered by an educational institution."""

    total_courses = 0

    def __init__(self, course_code, course_name):
        course_code = course_code.strip().upper()
        course_name = course_name.strip()

        if not course_code or not course_name:
            raise ValueError(
                "Course code and course name cannot be empty."
            )

        self.course_code = course_code
        self.course_name = course_name

        Course.total_courses += 1

    def display_course(self):
        """Return the course details."""
        return f"{self.course_code} - {self.course_name}"

    @classmethod
    def get_total_courses(cls):
        """Return the number of Course objects created."""
        return cls.total_courses


# =====================================================
# CLASS 2: STUDENT
# =====================================================

class Student:
    """Represent a student registered on the learning system."""

    total_students = 0

    def __init__(self, student_id, name, level):
        student_id = student_id.strip().upper()
        name = name.strip()
        level = level.strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        if not name:
            raise ValueError("Student name cannot be empty.")

        if not level:
            raise ValueError("Student level cannot be empty.")

        self.student_id = student_id
        self.name = name
        self.level = level

        # Dictionary: course code -> Enrollment object
        self.enrollments = {}

        Student.total_students += 1

    def enroll(self, course):
        """Enroll the student in a Course object."""
        if not isinstance(course, Course):
            raise TypeError(
                "Enrollment requires a valid Course object."
            )

        if course.course_code in self.enrollments:
            print("Student is already enrolled in this course.")
            return False

        enrollment = Enrollment(self, course)
        self.enrollments[course.course_code] = enrollment

        print(
            f"{self.name} enrolled in {course.course_name}."
        )
        return True

    def display_record(self):
        """Display the student's profile and course results."""
        print("\n" + "-" * 55)
        print("STUDENT RECORD")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print("Course Results:")

        if not self.enrollments:
            print("No courses registered.")

        for enrollment in self.enrollments.values():
            enrollment.display_result_line()

        print("-" * 55)

    @classmethod
    def get_total_students(cls):
        """Return the number of Student objects created."""
        return cls.total_students


# =====================================================
# CLASS 3: ENROLLMENT
# =====================================================

class Enrollment:
    """Connect a student to a course and store assessment results."""

    total_enrollments = 0

    def __init__(self, student, course):
        self.enrollment_id = (
            f"ENR{Enrollment.total_enrollments + 1:04d}"
        )

        self.student = student
        self.course = course
        self.mark = None

        Enrollment.total_enrollments += 1

    def record_mark(self, mark):
        """Validate and record a mark from 0 to 100."""
        if (
            not isinstance(mark, (int, float))
            or isinstance(mark, bool)
        ):
            raise ValueError("Mark must be a number.")

        if not 0 <= mark <= 100:
            raise ValueError(
                "Mark must be between 0 and 100."
            )

        self.mark = float(mark)

    @staticmethod
    def calculate_grade(mark):
        """Calculate a letter grade from a numerical mark."""
        if (
            not isinstance(mark, (int, float))
            or isinstance(mark, bool)
        ):
            raise ValueError("Mark must be numeric.")

        if not 0 <= mark <= 100:
            raise ValueError(
                "Mark must be between 0 and 100."
            )

        if mark >= 80:
            return "A"
        elif mark >= 70:
            return "B"
        elif mark >= 60:
            return "C"
        elif mark >= 50:
            return "D"
        else:
            return "F"

    def display_result_line(self):
        """Display the result for one course."""
        if self.mark is None:
            print(
                f"{self.course.display_course()}: "
                "Not yet graded"
            )
        else:
            grade = self.calculate_grade(self.mark)

            print(
                f"{self.course.display_course()}: "
                f"{self.mark:g}/100 | Grade: {grade}"
            )

    def display_result(self):
        """Display detailed enrollment and result information."""
        print("\nENROLLMENT RESULT")
        print(f"Enrollment ID: {self.enrollment_id}")
        print(
            f"Student: {self.student.name} "
            f"({self.student.student_id})"
        )
        print(f"Course: {self.course.display_course()}")

        if self.mark is None:
            print("Mark: Not yet graded")
            print("Grade: Pending")
        else:
            print(f"Mark: {self.mark:g}/100")
            print(
                f"Grade: {self.calculate_grade(self.mark)}"
            )


# =====================================================
# CLASS 4: STUDENT LEARNING SYSTEM
# =====================================================

class StudentLearningSystem:
    """Manage students and courses using dictionaries only."""

    def __init__(self, system_name):
        self.system_name = system_name

        # Dictionary: student ID -> Student object
        self.students = {}

        # Dictionary: course code -> Course object
        self.courses = {}

    def add_student(self, student):
        """Register a student and prevent duplicate IDs."""
        if not isinstance(student, Student):
            raise TypeError(
                "Only Student objects can be registered."
            )

        if student.student_id in self.students:
            print("This student ID already exists.")
            return False

        self.students[student.student_id] = student

        print("Student record added successfully.")
        return True

    def find_student(self, student_id):
        """Search for a student using their ID."""
        return self.students.get(
            student_id.strip().upper()
        )

    def add_course(self, course):
        """Add a course and prevent duplicate course codes."""
        if not isinstance(course, Course):
            raise TypeError(
                "Only Course objects can be added."
            )

        if course.course_code in self.courses:
            print("This course code already exists.")
            return False

        self.courses[course.course_code] = course

        print("Course created successfully.")
        return True

    def display_courses(self):
        """Display all available courses."""
        print("\nAVAILABLE COURSES")

        if not self.courses:
            print("No courses are available.")
            return

        for course in self.courses.values():
            print(course.display_course())

    def display_all_students(self):
        """Display every registered student."""
        if not self.students:
            print("No student records are available.")
            return

        for student in self.students.values():
            student.display_record()

    def display_statistics(self):
        """Display system statistics."""
        print("\nSYSTEM STATISTICS")
        print(f"System: {self.system_name}")
        print(
            f"Registered students: {len(self.students)}"
        )
        print(
            f"Available courses: {len(self.courses)}"
        )
        print(
            f"Student objects created: "
            f"{Student.get_total_students()}"
        )
        print(
            f"Course objects created: "
            f"{Course.get_total_courses()}"
        )
        print(
            f"Enrollment objects created: "
            f"{Enrollment.total_enrollments}"
        )


# =====================================================
# INPUT VALIDATION
# =====================================================

def get_non_empty_input(prompt):
    """Keep asking until the user enters a value."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


# =====================================================
# COURSE MANAGEMENT
# =====================================================

def add_course_action(system):
    """Collect information and create a course."""
    code = get_non_empty_input(
        "Enter course code: "
    ).upper()

    if code in system.courses:
        print("This course code already exists.")
        return

    name = get_non_empty_input(
        "Enter course name: "
    )

    try:
        course = Course(code, name)
        system.add_course(course)

    except ValueError as error:
        print(f"Error: {error}")


# =====================================================
# STUDENT REGISTRATION
# =====================================================

def register_student_action(system):
    """Register a new student and optionally enroll them."""
    student_id = get_non_empty_input(
        "Enter student ID: "
    ).upper()

    if system.find_student(student_id):
        print("This student ID already exists.")
        return

    name = get_non_empty_input(
        "Enter student name: "
    )

    level = get_non_empty_input(
        "Enter student level: "
    )

    try:
        student = Student(student_id, name, level)
        system.add_student(student)

    except ValueError as error:
        print(f"Error: {error}")
        return

    system.display_courses()

    if not system.courses:
        return

    course_code = input(
        "Enter course code to enroll "
        "(or press Enter to skip): "
    ).strip().upper()

    if course_code:
        course = system.courses.get(course_code)

        if course is None:
            print(
                "Course not found. "
                "Student remains registered."
            )
        else:
            student.enroll(course)


# =====================================================
# ENROLLMENT MANAGEMENT
# =====================================================

def enroll_student_action(system):
    """Enroll an existing student in a course."""
    student = system.find_student(
        input("Enter student ID: ")
    )

    if student is None:
        print("Student not found.")
        return

    system.display_courses()

    course_code = input(
        "Enter course code: "
    ).strip().upper()

    course = system.courses.get(course_code)

    if course is None:
        print("Course not found.")
        return

    student.enroll(course)


# =====================================================
# RESULT MANAGEMENT
# =====================================================

def record_result_action(system):
    """Record a mark for an enrolled student."""
    student = system.find_student(
        input("Enter student ID: ")
    )

    if student is None:
        print("Student not found.")
        return

    if not student.enrollments:
        print(
            "This student is not enrolled in any course."
        )
        return

    print("\nENROLLED COURSES")

    for code, enrollment in student.enrollments.items():
        print(
            f"{code} - {enrollment.course.course_name}"
        )

    course_code = input(
        "Enter course code: "
    ).strip().upper()

    enrollment = student.enrollments.get(course_code)

    if enrollment is None:
        print(
            "The student is not enrolled in that course."
        )
        return

    try:
        mark = float(
            input("Enter mark (0-100): ")
        )

        enrollment.record_mark(mark)
        print("Result recorded successfully.")

    except ValueError as error:
        print(f"Error: {error}")


# =====================================================
# STUDENT SEARCH
# =====================================================

def display_student_action(system):
    """Search for and display one student."""
    student = system.find_student(
        input("Enter student ID: ")
    )

    if student is None:
        print("Student not found.")
    else:
        student.display_record()


# =====================================================
# MENU
# =====================================================

def show_menu():
    """Display the main program menu."""
    print("\n" + "=" * 55)
    print("STUDENT LEARNING AND RESULTS MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add a course")
    print("2. Register a student")
    print("3. Enroll a student in a course")
    print("4. Record a result")
    print("5. Display all students")
    print("6. Search for a student")
    print("7. Display system statistics")
    print("0. Exit")


# =====================================================
# SAMPLE DATA
# =====================================================

def load_demo_data(system):
    """Load fictional records for program demonstration."""
    programming = Course(
        "OOP101",
        "Object-Oriented Programming"
    )

    database = Course(
        "DBS101",
        "Database Systems"
    )

    system.add_course(programming)
    system.add_course(database)

    student_one = Student(
        "ST001",
        "Musa Kamara (fictional)",
        "Year 2"
    )

    student_two = Student(
        "ST002",
        "Fatmata Sesay (fictional)",
        "Year 2"
    )

    system.add_student(student_one)
    system.add_student(student_two)

    student_one.enroll(programming)
    student_one.enroll(database)
    student_two.enroll(programming)

    student_one.enrollments["OOP101"].record_mark(85)
    student_one.enrollments["DBS101"].record_mark(74)
    student_two.enrollments["OOP101"].record_mark(68)


# =====================================================
# MAIN PROGRAM
# =====================================================

def main():
    """Run the application."""
    system = StudentLearningSystem(
        "Student Learning and Results Management System"
    )

    load_demo_data(system)

    while True:
        show_menu()

        choice = input(
            "Select an option: "
        ).strip()

        if choice == "1":
            add_course_action(system)

        elif choice == "2":
            register_student_action(system)

        elif choice == "3":
            enroll_student_action(system)

        elif choice == "4":
            record_result_action(system)

        elif choice == "5":
            system.display_all_students()

        elif choice == "6":
            display_student_action(system)

        elif choice == "7":
            system.display_statistics()

        elif choice == "0":
            print(
                "Thank you for using the system."
            )
            break

        else:
            print(
                "Invalid choice. Please select a listed option."
            )


if __name__ == "__main__":
    main()