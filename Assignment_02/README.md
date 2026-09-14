Siam University Vehicle Rental System
# Assignment 02 —  CampusWheels Vehicle Rental Desk

## Course Information
- **Course:** 192-201 Advanced Computer Programming with Generative AI
- **Student:** Thida Khaing 
- **Student ID**  6705140024
- **Assignment:** Assignment 02 — Vehicle Rental System


---

## 1. Project Overview

This project is a simple **campus vehicle-rental system** developed in Python for Siam University.

The program models different types of vehicles and the people who rent them. It demonstrates three important Object-Oriented Programming (OOP) concepts:

* **Classes and Objects :**  Created Vehicle, Renter, ElectricCar, and Motorbike classes.
* **Encapsulation :**Used @property and setter methods to validate name and license_no.
* **Inheritance :** ElectricCar and Motorbike inherit from the Vehicle class.
* **Polymorphism** Each vehicle type has its own __str__() method.

---

## 2. Project Structure

```text
Assignment_02/
│
├── rental.py
├── main.py
└── README.md
```

### `rental.py`

Contains all four required classes:

* `Vehicle`
* `Renter`
* `ElectricCar`
* `Motorbike`

### `main.py`

Contains a demonstration program that creates objects, tests renting and returning vehicles, checks validation, and demonstrates inheritance and polymorphism.

### `README.md`

Contains the project description, instructions for running the program, OOP concepts demonstrated, and an honest AI-use note.

---
## 3. Project Execution
Run this in the terminal:

python main.py

The program demonstrates creating vehicles and renters, renting and returning vehicles, validation, inheritance, and polymorphism.

## 4. Testing the Program

I tested the program using pytest with a separate test_rental.py file to check the required functionality, including:

Vehicle rental and return status
Renter validation
Properties and setters
Inheritance
Method overriding
Polymorphism

The test_rental.py file was used only for development testing.
---

## 5. AI Use Note
I used AI mainly to clarify encapsulation, @property and how to write the README.md file and used test_rental.py to check my program during development.


