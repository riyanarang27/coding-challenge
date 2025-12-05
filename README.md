Coding Challenge Assignments :

This folder contains all the assignments for the coding challenge.Each assignment has its own folder inside this project.
This README explains:
- How to set up the project
- How to run the code
- What Assignment 1 is about
- What Assignment 2 is about
- What output you should see
- What you need to submit

The structure of this project is:
coding-challenge/
  README.md
  assignment1/
    producer_consumer.py
    test_producer_consumer.py
  assignment2/
    sales.csv
    sales.py
    test_sales.py
  venv/

What each folder means:

- README.md → This main file. It explains Assignment 1 and Assignment 2.
- assignment1/ → Contains all code, and test for Assignment 1.
- assignment2/ → Contains all code, and test for Assignment 2.
- venv/ → Virtual environment folder.

How to activate virtual enviroment:

Mac/Linux:
   python3 -m venv venv
source venv/bin/activate

Windows:
   python -m venv venv
venv\Scripts\activate

Assignment 1 — Producer & Consumer Program
Assignment 1 demonstrates how two threads (a Producer and a Consumer) communicate using a shared queue.

What Assignment 1 does:
Producer thread creates numbers
Consumer thread retrieves numbers
Queue capacity is small → producer/consumer wait when full/empty
Shows:
Thread synchronization
Blocking queues
Wait/notify mechanism

Files for Assignment 1:
assignment1/producer_consumer.py
assignment1/test_producer_consumer.py

For testing the Assignment 1:
1. cd assignment1
2. Run the program: python3 producer_consumer.py
    Expected Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
3. Run the Test: python3 -m unittest test_producer_consumer.py
    Expected Test Result: 
......
----------------------------------------------------------------------
Ran 6 tests in 0.xx s

OK

Assignment 2 — CSV Sales Data Analysis
Assignment 2 reads data from a CSV file and performs several data analysis operations using functional programming, lambda expressions, and stream-style processing.

What Assignment 2 does:
Loads data from sales.csv
Cleans invalid / missing rows
Computes:
Total revenue
Revenue by region
Revenue by product
Average (weighted) price per product
Top-selling products by revenue
Monthly revenue totals

Uses:
Functional programming
Lambda expressions
Data aggregation
Lightweight streaming operations

Files for Assignment 2:
sales.csv → Sales dataset
sales.py → Analysis functions + main program output
test_sales.py → Complete test suite covering:
Valid data
Empty data
Incorrect CSV rows
All analysis functions

For testing Assignment 2:
1. cd Assignment2
2. Run the Program: python3 sales.py
     Expected Output: 
rows: 10
tot_rev: 343.0
reg_rev: {'NA': 169.5, 'EU': 96.0, 'APAC': 77.5}
prod_rev: {'Widget': 97.0, 'Gadget': 104.5, 'Thing': 51.5, 'Gizmo': 90.0}
avg_price: {'Widget': 10.78, 'Gadget': 8.71, 'Thing': 5.15, 'Gizmo': 15.0}
top_prod: ['Gadget', 'Widget', 'Gizmo']
mon_rev: {'2024-01': 133.5, '2024-02': 67.0, '2024-03': 142.5}
3. Run the test: python3 -m unittest test_sales.py
     Expected OutPut: 
........
----------------------------------------------------------------------
Ran 8 tests in 0.xx s

OK


What Is Included in This Submission

Full implementation of Assignment 1
Full implementation of Assignment 2
Complete test suites for both assignments
Clean functional programming style in Assignment 2
Passing test results for both assignments
A single public GitHub repository containing everything






