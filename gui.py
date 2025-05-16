import tkinter as tk
from tkinter import ttk, messagebox
from domain import Book, EBook, DigitalLibrary

class LibraryGUI:
    def __init__(self, root):
        self.library = DigitalLibrary()
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("650x440")
        self.root.resizable(False, False)

        # --- Styles ---
        style = ttk.Style()
        style.configure('TFrame', background='#f3f4f6')
        style.configure('TLabel', background='#f3f4f6', font=('Segoe UI', 11))
        style.configure('Header.TLabel', font=('Segoe UI', 16, 'bold'))
        style.configure('TButton', font=('Segoe UI', 10, 'bold'))
        style.configure('Treeview', rowheight=24, font=('Segoe UI', 10))
        style.configure('TCheckbutton', background='#f3f4f6')

        main_frame = ttk.Frame(self.root, padding=18, style='TFrame')
        main_frame.pack(fill='both', expand=True)

        # --- Header ---
        ttk.Label(main_frame, text="Library Management System", style='Header.TLabel').grid(row=0, column=0, columnspan=4, pady=(10, 12), sticky='w')

        # --- Form Inputs ---
        ttk.Label(main_frame, text="Title:").grid(row=1, column=0, sticky='e', pady=2)
        self.title_entry = ttk.Entry(main_frame, width=25)
        self.title_entry.grid(row=1, column=1, sticky='w', pady=2)

        ttk.Label(main_frame, text="Author:").grid(row=2, column=0, sticky='e', pady=2)
        self.author_entry = ttk.Entry(main_frame, width=25)
        self.author_entry.grid(row=2, column=1, sticky='w', pady=2)

        ttk.Label(main_frame, text="ISBN:").grid(row=3, column=0, sticky='e', pady=2)
        self.isbn_entry = ttk.Entry(main_frame, width=25)
        self.isbn_entry.grid(row=3, column=1, sticky='w', pady=2)

        self.ebook_var = tk.IntVar()
        self.ebook_checkbox = ttk.Checkbutton(main_frame, text="eBook", variable=self.ebook_var, command=self.toggle_ebook)
        self.ebook_checkbox.grid(row=1, column=2, sticky='e', padx=(14, 0))

        ttk.Label(main_frame, text="Size (MB):").grid(row=2, column=2, sticky='e', pady=2)
        self.size_entry = ttk.Entry(main_frame, width=10, state='disabled')
        self.size_entry.grid(row=2, column=3, sticky='w', pady=2)

        # --- Buttons ---
        self.add_btn = ttk.Button(main_frame, text="Add Book", command=self.add_book)
        self.add_btn.grid(row=4, column=1, pady=(8, 12), sticky='w')
        self.lend_btn = ttk.Button(main_frame, text="Lend Book", command=self.lend_book)
        self.lend_btn.grid(row=4, column=2, pady=(8, 12), sticky='w')
        self.return_btn = ttk.Button(main_frame, text="Return Book", command=self.return_book)
        self.return_btn.grid(row=4, column=3, pady=(8, 12), sticky='w')

        # --- Book List ---
        ttk.Label(main_frame, text="Available Books:").grid(row=5, column=0, columnspan=2, sticky='w', pady=(8, 2))
        columns = ('Title', 'Author', 'ISBN', 'Type', 'Size/MB')
        self.tree = ttk.Treeview(main_frame, columns=columns, show='headings', height=7)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center', width=120)
        self.tree.grid(row=6, column=0, columnspan=4, sticky='nsew', pady=(0, 10))
        main_frame.rowconfigure(6, weight=1)

        # --- Author filter ---
        ttk.Label(main_frame, text="Filter by Author:").grid(row=7, column=0, sticky='e', pady=2)
        self.author_filter_entry = ttk.Entry(main_frame, width=18)
        self.author_filter_entry.grid(row=7, column=1, sticky='w', pady=2)
        self.filter_btn = ttk.Button(main_frame, text="Filter", command=self.filter_by_author)
        self.filter_btn.grid(row=7, column=2, sticky='w', padx=(6, 0))
        self.showall_btn = ttk.Button(main_frame, text="Show All", command=self.display_books)
        self.showall_btn.grid(row=7, column=3, sticky='w', padx=(0, 0))

        # --- Initial Sample Books ---
        self.library.add_book(Book("Python Fundamentals", "Ali", "111111"))
        self.library.add_book(Book("Object-Oriented Programming", "Shehroz", "222222"))
        self.library.add_book(Book("Data Science Essentials", "Ali", "333333"))
        self.library.add_ebook(EBook("Machine Learning Guide", "Shehroz", "444444", 10))
        self.display_books()

    def toggle_ebook(self):
        if self.ebook_var.get():
            self.size_entry.config(state='normal')
        else:
            self.size_entry.delete(0, tk.END)
            self.size_entry.config(state='disabled')

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        is_ebook = self.ebook_var.get()
        size = self.size_entry.get().strip()

        if not title or not author or not isbn:
            messagebox.showerror("Input Error", "Please fill all fields.")
            return

        if is_ebook:
            if not size:
                messagebox.showerror("Input Error", "Please enter download size for eBook.")
                return
            try:
                size_val = float(size)
                if size_val <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Input Error", "Download size must be a positive number.")
                return
            book = EBook(title, author, isbn, size_val)
            self.library.add_ebook(book)
        else:
            book = Book(title, author, isbn)
            self.library.add_book(book)

        self.display_books()
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.size_entry.delete(0, tk.END)
        self.ebook_var.set(0)
        self.size_entry.config(state='disabled')

    def lend_book(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Select Book", "Please select a book to lend.")
            return
        item = self.tree.item(selected[0])
        isbn = item['values'][2]
        try:
            msg = self.library.lend_book(isbn)
            messagebox.showinfo("Success", msg)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        self.display_books()

    def return_book(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Select Book", "Please select a book to return.")
            return
        item = self.tree.item(selected[0])
        isbn = item['values'][2]
        msg = self.library.return_book(isbn)
        messagebox.showinfo("Returned", msg)
        self.display_books()

    def display_books(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for book in self.library.available_books():
            if isinstance(book, EBook):
                self.tree.insert('', tk.END, values=(book.title, book.author, book.isbn, 'eBook', book.download_size))
            else:
                self.tree.insert('', tk.END, values=(book.title, book.author, book.isbn, 'Book', '-'))

    def filter_by_author(self):
        author = self.author_filter_entry.get().strip()
        if not author:
            messagebox.showinfo("Enter Author", "Please specify an author name.")
            return
        filtered = self.library.books_by_author(author)
        for i in self.tree.get_children():
            self.tree.delete(i)
        for book in filtered:
            if book.is_available:
                if isinstance(book, EBook):
                    self.tree.insert('', tk.END, values=(book.title, book.author, book.isbn, 'eBook', book.download_size))
                else:
                    self.tree.insert('', tk.END, values=(book.title, book.author, book.isbn, 'Book', '-'))