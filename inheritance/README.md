# Inheritance

This directory contains Python scripts that demonstrate various concepts related to inheritance in object-oriented programming. Inheritance allows classes to inherit attributes and methods from other classes, promoting code reuse and establishing relationships between classes.

## Table of Contents
- [Files and Descriptions](#files-and-descriptions)
  - [method_override.py](#method_overridepy)
  - [practical_task_1.py](#practical_task_1py)
- [Concepts Demonstrated](#concepts-demonstrated)
- [Importance of Learning These Concepts](#importance-of-learning-these-concepts)
- [Usage](#usage)
- [Credits](#credits)

## Files and Descriptions

### method_override.py
**Description**: This script demonstrates method overriding, where a child class provides a specific implementation of a method that is already defined in its parent class. This is crucial for polymorphism in object-oriented programming.

### practical_task_1.py
**Description**: This script shows the basic mechanics of inheritance by creating a parent class and a child class that inherits attributes and methods from the parent.

## Concepts Demonstrated

### method_override.py
- **Method Overriding**: This script illustrates how a child class can override a method from its parent class to provide a specific implementation.
- **Why It's Important**: Method overriding is essential for polymorphism, allowing different classes to be treated as instances of the same class through a common interface, leading to more flexible and maintainable code.

### practical_task_1.py
- **Basic Inheritance**: This script demonstrates the fundamental concept of inheritance, where a child class inherits attributes and methods from a parent class.
- **Why It's Important**: Understanding basic inheritance is crucial for code reuse and establishing hierarchical relationships between classes, making code more modular and easier to manage.

## Importance of Learning These Concepts

Learning inheritance is vital for mastering object-oriented programming, which is a dominant paradigm in software development. Inheritance allows for the creation of more complex and structured code by promoting reuse and reducing redundancy. It enables developers to build on existing code, creating new functionality with minimal changes. This leads to more maintainable and scalable codebases, which is essential for large and long-term projects.

## Usage

To use any of the scripts, navigate to this directory and run the script using Python. For example:

    cd inheritance
    python method_override.py

This script demonstrates method overriding through a practical example involving an `Adult` class (parent) and a `Child` class (child). The script takes user input for a person's age and decides whether the person object will be an instance of the `Adult` class or the `Child` class. It then uses the `person_can_drive()` method to determine and print whether the person is old enough to drive, based on their class instance.

![override](https://github.com/javerria/codingTasks/assets/163902258/e472e4e4-2bb6-44aa-adda-855dd92f3641)


## Credits

Authored by [Javeria](https://www.linkedin.com/javerria).
