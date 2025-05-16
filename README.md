# Library Management System (GUI)

A simple desktop-based Library Management System built using **Python** and **Tkinter**, demonstrating **object-oriented programming** concepts such as classes, inheritance, and method overriding. This application allows users to add, lend, return, and filter both physical and digital books through an intuitive graphical interface.

---

## Features

- Add books and eBooks to the library
- Lend and return books
- View available books
- Filter books by author
- GUI built using Tkinter and ttk themed widgets
- Object-oriented structure with `Book`, `EBook`, and `DigitalLibrary` classes

---

## Technologies Used

- **Python 3**
- **Tkinter** (for GUI)
- **ttk** (themed widgets for better UI)

---

## Folder Structure

project
- gui.py # Contains the GUI logic
- domain.py # Contains Book, EBook, and DigitalLibrary class definitions
- main.py # Entry point to run the application
- README.md # Project documentation
## How to Run

1. Make sure you have Python 3 installed.

2. Clone or download this repository.

3. Run the following command in your terminal or command prompt:

```bash
python maiin.py
The application window should launch, allowing you to interact with the library system.
```
### 📚 Class Overview

**Book**  
Represents a physical book with the following attributes:
- Title  
- Author  
- ISBN  
- Availability status  

**EBook** *(inherits from Book)*  
Represents a digital book with an additional attribute:
- Download size (in MB)

**DigitalLibrary**  
Manages the collection of books and provides methods to:
- Add physical books and eBooks  
- Lend books  
- Return books  
- Filter books by author  
- List available books  

### 🖥️ GUI Functionalities

- **Add Book/eBook**:  
  Enter the title, author, and ISBN.  
  To add an eBook, check the "eBook" box and provide the download size.

- **Lend Book**:  
  Select a book from the list and click the "Lend Book" button.

- **Return Book**:  
  Select a book from the list and click the "Return Book" button.

- **Filter by Author**:  
  Enter an author's name and click "Filter" to see books by that author.  
  Click "Show All" to reset the list and view all available books.

