
# Smart Service Desk Management System

## Project Overview
A Python-based application designed to manage employee IT support requests.

## Features
- Create service requests
- View all requests
- Search requests using Request ID
- Resolve open requests
- Prevent duplicate Request IDs
- Store data permanently using JSON

## Technologies Used
- Python
- Object-Oriented Programming
- JSON
- Git and GitHub

## Project Concepts
- OOP
- Exception Handling
- File Handling
- SOLID Principles
- Domain-Driven Design (DDD)
- Git Branching and Merging

## Project Structure
- domain: Business logic and domain classes
- application: Application operations
- infrastructure: JSON file handling
- data: Stored service requests
- main.py: Application entry point

## How to Run

Open the project folder in VS Code and execute:

python main.py

## Git Workflow
Development work is performed in the development branch.
After testing, development is merged into main.
The final working application is maintained in main.


## Development Status
The project is developed and tested using a separate development branch.
All completed changes are merged into the main branch after verification.

## Error Handling
The application uses custom exceptions to handle:
- Duplicate service request IDs
- Requests that cannot be found
- Invalid priority values
- Invalid menu choices
- Empty menu input

## Data Persistence
All service requests are stored in `data/requests.json`.
The application loads existing requests when it starts and saves changes automatically.