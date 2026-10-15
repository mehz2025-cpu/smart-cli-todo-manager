# Smart CLI ToDo Manager

A command-line task manager built with Python and JSON. This project includes two implementations that demonstrate the progression from procedural programming to object-oriented design.

## Versions

### V1 — Procedural

* Uses standalone functions
* Stores tasks in a list
* Loads and saves tasks using JSON
* Supports adding, listing, completing, and deleting tasks

### V2 — Object-Oriented

* Organizes functionality in a `TaskManager` class
* Encapsulates task data and operations
* Uses a dictionary to map menu choices to methods
* Validates empty task titles
* Supports adding, listing, completing, and deleting tasks

## Requirements

* Python 3
* No external dependencies

## Usage

Run either version from its own directory:

```bash
python todo.py
```

The application creates `tasks.json` in the current working directory to store tasks.

## Project Structure

```text
smart-cli-todo-manager/
├── v1/
│   └── todo.py
├── v2/
│   └── todo.py
├── .gitignore
└── README.md
```

## Concepts Demonstrated

* Functions and classes
* Lists and dictionaries
* JSON file handling
* Input validation
* Exception handling
* Command-line menus

## Note

This project is intended for learning Python fundamentals and software design.
