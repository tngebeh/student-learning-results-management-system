Student Learning and Results Management System

1. Project Overview

The Student Learning and Results Management System is a Python-based console application developed for the education domain as part of the Object-Oriented Programming (OOP) course at Limkokwing University of Creative Technology Sierra Leone.

The purpose of this project is to demonstrate how object-oriented programming can be used to manage student information, courses, enrollments, and academic results. The system allows users to register students, create courses, enroll students in courses, record marks, calculate letter grades, search for student records, and display system statistics.

The application is designed as an educational prototype to demonstrate fundamental programming concepts, data management, input validation, and software development practices.

2. Project Objectives

The main objectives of this project are to:

1. Apply classes and objects to solve a practical problem in the education sector.
2. Demonstrate attributes, constructors, and instance methods.
3. Implement class methods and static methods.
4. Use dictionaries as the only collection data structure for managing records.
5. Demonstrate interaction between Student, Course, and Enrollment objects.
6. Implement student registration, course enrollment, result recording, and record searching.
7. Apply input validation to reduce invalid data entry.
8. Demonstrate relevant Digital Public Goods (DPG) principles, including accessibility, privacy awareness, and open-source readiness.

3. Technologies Used

- Programming language: Python
- Programming paradigm: Object-Oriented Programming
- Data structure: Dictionaries
- User interface: Command-line menu
- Development environment: [Enter your Python editor, e.g., IDLE or Visual Studio Code]
- Version control and collaboration: GitHub

The program uses Python's standard features and does not require third-party packages.

4. System Features

The system provides the following features:

- Course management: Create courses with unique course codes and course names.
- Student registration: Register students with a student ID, name, and academic level.
- Course enrollment: Enroll students in available courses while preventing duplicate enrollment in the same course.
- Result recording: Enter marks between 0 and 100 for students enrolled in a course.
- Grade calculation: Convert numerical marks into letter grades using the illustrative grading scale in the program.
- Student search: Search for a student using their student ID.
- Record display: Display individual student records and all registered students.
- System statistics: Display counts of student, course, and enrollment objects.

5. Object-Oriented Programming Implementation

The project contains four main classes.

5.1 Course Class

The "Course" class represents an academic course. It stores the course code and course name and provides a method for displaying course information. Its class method returns the number of course objects created.

5.2 Student Class

The "Student" class represents a registered student. It stores the student's ID, name, and academic level. Its methods support course enrollment and the display of student records. It also includes a class method for counting student objects.

5.3 Enrollment Class

The "Enrollment" class connects a student object to a course object. It stores the enrollment ID and mark, validates assessment marks, and calculates a letter grade. The class demonstrates interaction between objects, an instance method, and a static method.

5.4 StudentLearningSystem Class

The "StudentLearningSystem" class manages the application's student and course records. It supports adding students, searching for students, adding courses, displaying records, and showing system statistics.

6. Data Structure Used

The project uses dictionaries only as its collection data structure.

- The student dictionary stores Student objects using student IDs as keys.
- The course dictionary stores Course objects using course codes as keys.
- Each Student object maintains an enrollment dictionary using course codes as keys.

Dictionaries make it possible to retrieve records efficiently using unique identifiers. The project does not use lists as a collection data structure.

7. Input Validation and Privacy

The application validates required fields to prevent empty student IDs, names, academic levels, course codes, and course names. It also prevents duplicate student IDs and course codes, checks that students are enrolled before marks are recorded, and ensures that marks fall between 0 and 100.

The demonstration uses fictional student records. Real student information should not be uploaded to a public GitHub repository. The program is an educational prototype and does not include authentication, authorization, database persistence, or production-level security controls.

8. Digital Public Goods (DPG) Considerations

The project demonstrates practices relevant to Digital Public Goods:

- Open-source readiness: The source code can be shared publicly with an appropriate open-source licence.
- Accessibility: The text-based interface can run on computers capable of running Python and does not require a graphical interface.
- Privacy awareness: The application uses fictional demonstration data and encourages responsible handling of student information.
- Reusability: The classes and methods are separated into manageable components that can be adapted for other educational projects.
- Transparency: The source code and program logic can be reviewed and improved by other developers.

These features demonstrate alignment with selected DPG principles; they do not by themselves establish formal DPG recognition or certification.

9. Installation and Execution

Requirements

- Python 3 installed on the computer.
- The "student_learning_results.py" source file.
- A Python editor or terminal.

Steps to Run

1. Download or clone the project repository from GitHub.
2. Open the project folder in a Python editor or terminal.
3. Run the following command:

python student_learning_results.py

4. Select an option from the displayed menu.
5. Follow the prompts to manage courses, students, enrollments, and results.
6. Select "0" to exit the application.

The program loads fictional demonstration records at startup to help users test the features.

10. Limitations and Future Improvements

The current version stores records in memory, so data entered during a session is lost when the program closes. The grading scale is illustrative and should be replaced with institution-approved grading rules before any real academic use.

Future improvements could include:

- Database integration for permanent storage.
- Secure user authentication and role-based access.
- Editing and deleting records with appropriate permissions.
- Academic transcripts and GPA calculations based on approved institutional rules.
- A graphical user interface or web-based interface.
- Automated testing and improved error reporting.

11. Conclusion

The Student Learning and Results Management System demonstrates how object-oriented programming can be applied to a practical education-related problem. It combines classes, objects, methods, dictionaries, input validation, and object interaction to support basic student and course management.

The project provides a foundation for further development into a more complete academic information system while highlighting the importance of accessibility, privacy, documentation, and responsible software sharing.

12. Project Information

- Project title: Student Learning and Results Management System
- Student name: Abdul Tom Ngebeh
- Student ID: 905005676
- Programme: BBIT1101
- Faculty: Faculty of ICT
- Course: Object-Oriented Programming
- Lecturer: [Enter your lecturer's name]
- GitHub repository: [Paste your repository URL]
- Submission date: [Enter your submission date]
