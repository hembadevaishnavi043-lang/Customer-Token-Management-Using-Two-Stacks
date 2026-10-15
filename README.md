# Customer-Token-Management-Using-Two-Stacks
Mini project implementing a queue using two stacks in Python

## Introduction
This project implements a queue using two stacks in Python. It manages customer tokens and serves customers in FIFO (First In, First Out) order.

## Objectives
- Add customers and generate token numbers.
- Serve customers in FIFO order.
- Display waiting customers.
- Count the number of waiting customers.

## Data Structure Used
- Stack
- Queue
- List

## Operations
1. Add Customer
2. Serve Customer
3. Display Waiting Queue
4. Count Waiting Customers
5. Exit

## Algorithm
Two stacks are used to implement the queue. New customers are added to Stack 1. When a customer needs to be served, elements are transferred to Stack 2 if it is empty. The top element of Stack 2 is then removed, ensuring FIFO order.

## Technology
Python 3

## Conclusion
This project demonstrates the implementation of a queue using two stacks and shows how FIFO order can be maintained.
