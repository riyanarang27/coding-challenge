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
screenshots/
assignment2/
screenshots/
venv/

What each folder means:

- README.md → This main file. It explains Assignment 1 and Assignment 2.
- assignment1/ → Contains all code, tests, and screenshots for Assignment 1.
- assignment2/ → Contains all code, tests, and screenshots for Assignment 2.
- venv/ → Virtual environment folder.

How to activate virtual enviroment:

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate


Assignment 1 
Assignment 1 shows how two threads (a Producer and a Consumer) work together using a shared queue.What Assignment 1 program does:

- The producer creates numbers(data).
- The consumer takes numbers(data) from the queue.
- The queue has a small size, so the producer or consumer sometimes needs to wait.
- This shows thread synchronization and blocking queues.

Files for Assignment 1:
1. assignment1/producer_consumer.py
2. assignment1/test_producer_consumer.py

For testing the Assignment 1:
1. cd assignment1
2. Run the program: python3 producer_consumer.py
    Expected Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
3.Run the Test: python3 -m unittest test_producer_consumer.py
    Expected Test Result: 
......
----------------------------------------------------------------------
Ran 6 tests in 0.xx s

OK






