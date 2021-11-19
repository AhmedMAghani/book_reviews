import tkinter
from tkinter import *
from bookdataset import *
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class BooksDatasetUi:
    def say_hello(self):
        print("Hello")

    def __init__(self):
        self.width = "510"
        self.hight = "400"
        self.main_window = tkinter.Tk()
        self.main_window.resizable(width=False, height=False)
        self.bookDataset = Bookdataset()
        self.main_window.geometry(self.width+'x'+self.hight)
        self.main_window.title('CMP 151 Students Book Review')
        self.tab_parent = ttk.Notebook(self.main_window)
        self.add_tabs()
        self.load_tabs_content()
        self.tab_parent.bind("<<NotebookTabChanged>>", self.on_tab_selected)
        self.tab_parent.pack(expand=1, fill='both')
        self.disable_tabs()
        self.say_hello()
        tkinter.mainloop()

    def on_tab_selected(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        print(tab_text)
        if tab_text == "Quit":
            self.bookDataset.save_objs()
            self.main_window.destroy()
        if tab_text == "Logout":
            self.disable_tabs()
            self.tab_parent.tab(0, text="Login")

    def add_tabs(self):
        self.tab_login = tkinter.Frame(self.tab_parent)
        self.tab_add_user = tkinter.Frame(self.tab_parent)
        self.tab_search_users = tkinter.Frame(self.tab_parent)
        self.tab_add_book = tkinter.Frame(self.tab_parent)
        self.tab_search_books = tkinter.Frame(self.tab_parent)
        self.tab_sort_books = tkinter.Frame(self.tab_parent)
        self.quit_button = tkinter.Frame(self.tab_parent)

        self.tab_parent.add(self.tab_login, text="Login")
        self.tab_parent.add(self.tab_add_user, text="Add User")
        self.tab_parent.add(self.tab_search_users, text="Search Users")
        self.tab_parent.add(self.tab_add_book, text="Add Book")
        self.tab_parent.add(self.tab_search_books, text="Search Books")
        self.tab_parent.add(self.tab_sort_books, text="Sort Books")
        self.tab_parent.add(self.quit_button, text="Quit")

    def disable_tabs(self, disable=True):
        active = "disabled" if disable else "normal"
        for i in range(1, 6):
            self.tab_parent.tab(i, state=active)

    def setup_quit_tab(self):
        self.saving_label = tkinter.Label(self.quit_button, text="Saving Please Wait!").grid(
            row=0, column=0, padx=180, pady=30)

    def setup_login_tab(self):

        self.username_label = tkinter.Label(self.tab_login, text="Username")
        self.username_login_entry = tkinter.Entry(self.tab_login)

        self.password_label = tkinter.Label(self.tab_login, text="Password")
        self.password__login_entry = tkinter.Entry(self.tab_login, show='*')

        self.loginButton = tkinter.Button(
            self.tab_login, text="Login", width=10, height=1, command=self.validate_admin_credentials)

        self.username_label.grid(row=0, column=0, padx=15, pady=15)
        self.username_login_entry.grid(
            row=0, column=1, columnspan=2, padx=15, pady=15)
        self.password_label.grid(row=1, column=0, padx=15, pady=15)
        self.password__login_entry.grid(
            row=1, column=1, columnspan=2, padx=15, pady=15)
        self.loginButton.grid(row=2, column=1, columnspan=2, padx=15, pady=15)

        self.tab_login.grid_columnconfigure((0, 1, 2), weight=1)

    def load_tabs_content(self):
        self.setup_login_tab()
        self.setup_add_user_tab()
        self.setup_search_users_tab()
        self.setup_add_book_tab()
        self.setup_search_books_tab()
        self.setup_sort_books_tab()
        self.setup_quit_tab()

    def validate_admin_credentials(self):
        print("username entered :", self.username_login_entry.get())
        print("password entered :", self.password__login_entry.get())

        self.validate_username = self.username_login_entry.get()
        self.validate_password = self.password__login_entry.get()

        if (self.validate_username == "admin") & (self.validate_password == "admin"):
            print("logged In")
            self.disable_tabs(False)
            self.tab_parent.tab(0, text="Logout")
            self.tab_parent.select(1)
            self.username_login_entry.delete(0, END)
            self.password__login_entry.delete(0, END)
        else:
            self.username_login_entry.delete(0, END)
            self.password__login_entry.delete(0, END)
            print("Wrong Password or User Name")

    def setup_add_user_tab(self):
        self.city_label = tkinter.Label(self.tab_add_user, text="City")
        self.city_entry = tkinter.Entry(self.tab_add_user)

        self.state_label = tkinter.Label(self.tab_add_user, text="State")
        self.state_entry = tkinter.Entry(self.tab_add_user)

        self.country_label = tkinter.Label(self.tab_add_user, text="Country")
        self.country_entry = tkinter.Entry(self.tab_add_user)

        self.age_label = tkinter.Label(self.tab_add_user, text="Age")
        self.age_entry = tkinter.Entry(self.tab_add_user)

        self.cancel_button = tkinter.Button(
            self.tab_add_user, text="Cancel", width=10, height=1, command=self.clear_add_user)
        self.addUser_button = tkinter.Button(
            self.tab_add_user, text="Add", width=10, height=1, command=self.add_user_to_book_dataset)

        self.city_label.grid(row=0, column=0, padx=15, pady=15)
        self.city_entry.grid(row=0, column=1, padx=15, pady=15)
        self.state_label.grid(row=1, column=0, padx=15, pady=15)
        self.state_entry.grid(row=1, column=1, padx=15, pady=15)
        self.country_label.grid(row=2, column=0, padx=15, pady=15)
        self.country_entry.grid(row=2, column=1, padx=15, pady=15)
        self.age_label.grid(row=3, column=0, padx=15, pady=15)
        self.age_entry.grid(row=3, column=1, padx=15, pady=15)
        self.cancel_button.grid(row=4, column=0, padx=15, pady=15)
        self.addUser_button.grid(row=4, column=1, padx=15, pady=15)

        self.tab_add_user.grid_columnconfigure((0, 1, 2), weight=1)

    def add_user_to_book_dataset(self):
        new_user_id = str(int(self.bookDataset.usersList[-1].user_id) + 1)
        new_user_location = str(self.city_entry.get(
        )) + "," + str(self.state_entry.get()) + "," + str(self.country_entry.get())
        new_user_age = None if self.age_entry.get().strip() == "" else self.age_entry.get()
        new_user = User(new_user_id, new_user_location, new_user_age)
        self.bookDataset.usersList.append(new_user)
        print("Saved User:\n", self.bookDataset.usersList[-1])

    def clear_add_user(self):
        self.city_entry.delete(0, END)
        self.state_entry.delete(0, END)
        self.country_entry.delete(0, END)
        self.age_entry.delete(0, END)

    def setup_add_book_tab(self):
        tkinter.Label(self.tab_add_book, text="ISBN").grid(
            row=0, column=0, padx=15, pady=15)
        self.add_book_ISBN_entry = tkinter.Entry(self.tab_add_book)
        self.add_book_ISBN_entry.grid(row=0, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_add_book, text="Title").grid(
            row=1, column=0, padx=15, pady=15)
        self.add_book_title_entry = tkinter.Entry(self.tab_add_book)
        self.add_book_title_entry.grid(row=1, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_add_book, text="Author").grid(
            row=2, column=0, padx=15, pady=15)
        self.add_book_author_entry = tkinter.Entry(self.tab_add_book)
        self.add_book_author_entry.grid(row=2, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_add_book, text="Year").grid(
            row=3, column=0, padx=15, pady=15)
        self.add_book_year_entry = tkinter.Entry(self.tab_add_book)
        self.add_book_year_entry.grid(row=3, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_add_book, text="Publisher").grid(
            row=4, column=0, padx=15, pady=15)
        self.add_book_publisher_entry = tkinter.Entry(self.tab_add_book)
        self.add_book_publisher_entry.grid(row=4, column=1, padx=15, pady=15)

        self.CancelButton = tkinter.Button(self.tab_add_book, text="Cancel", width=10, height=1,
                                           command=self.clear_add_book).grid(row=5, column=0, padx=15, pady=15)
        self.AddBookButton = tkinter.Button(self.tab_add_book, text="Add", width=10, height=1,
                                            command=self.add_book_to_book_dataset).grid(row=5, column=1, padx=15, pady=15)

        self.tab_add_book.grid_columnconfigure((0, 1, 2), weight=1)

    def add_book_to_book_dataset(self):
        new_book = Book(self.add_book_ISBN_entry.get(), self.add_book_title_entry.get(
        ), self.add_book_author_entry.get(), self.add_book_year_entry.get(), self.add_book_publisher_entry.get())
        self.bookDataset.booksList.append(new_book)
        print("Saved Book\n",self.bookDataset.booksList[-1])

    def clear_add_book(self):
        self.add_book_ISBN_entry.delete(0, END)
        self.add_book_title_entry.delete(0, END)
        self.add_book_author_entry.delete(0, END)
        self.add_book_year_entry.delete(0, END)
        self.add_book_publisher_entry.delete(0, END)

    def setup_search_users_tab(self):
        tkinter.Label(self.tab_search_users, text=" ID  ").grid(
            row=0, column=0, padx=15, pady=15)
        self.search_users_id_entry = tkinter.Entry(self.tab_search_users)
        self.search_users_id_entry.grid(row=0, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_users, text=" City  ").grid(
            row=1, column=0, padx=15, pady=15)
        self.search_users_city_entry = tkinter.Entry(self.tab_search_users)
        self.search_users_city_entry.grid(row=1, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_users, text=" State  ").grid(
            row=2, column=0, padx=15, pady=15)
        self.search_users_state_entry = tkinter.Entry(self.tab_search_users)
        self.search_users_state_entry.grid(row=2, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_users, text="Country").grid(
            row=3, column=0, padx=15, pady=15)
        self.search_users_country_entry = tkinter.Entry(self.tab_search_users)
        self.search_users_country_entry.grid(row=3, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_users, text=" Age ").grid(
            row=4, column=0, padx=15, pady=15)
        self.search_users_age_entry = tkinter.Entry(self.tab_search_users)
        self.search_users_age_entry.grid(row=4, column=1, padx=15, pady=15)

        self.search_users_cancel_button = tkinter.Button(self.tab_search_users, text="Cancel", width=10, height=1,
                                                         command=self.clear_search_users).grid(row=5, column=0, padx=15, pady=15)
        self.search_users_button = tkinter.Button(self.tab_search_users, text="Search", width=10, height=1,
                                                  command=self.search_user_from_book_dataset).grid(row=5, column=1, padx=15, pady=15)

        self.tab_search_users.grid_columnconfigure((0, 1, 2), weight=1)

    def search_user_from_book_dataset(self):
        query_user_location = str(self.search_users_city_entry.get()) + "," + str(
            self.search_users_state_entry.get()) + "," + str(self.search_users_country_entry.get())
        query_age = str(float(self.search_users_age_entry.get())) if self.search_users_age_entry.get() else None
        query_user = User(self.search_users_id_entry.get(
        ), query_user_location, query_age)
        query_reults = self.bookDataset.search_users(query_user)
        for user in query_reults:
            print(user)
        print("Number of results:",len(query_reults))

    def clear_search_users(self):
        self.search_users_id_entry.delete(0, END)
        self.search_users_city_entry.delete(0, END)
        self.search_users_state_entry.delete(0, END)
        self.search_users_country_entry.delete(0, END)
        self.search_users_age_entry.delete(0, END)

    def setup_search_books_tab(self):
        tkinter.Label(self.tab_search_books, text="ISBN").grid(
            row=0, column=0, padx=15, pady=15)
        self.search_books_ISBN_entry = tkinter.Entry(self.tab_search_books)
        self.search_books_ISBN_entry.grid(row=0, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_books, text="Title").grid(
            row=1, column=0, padx=15, pady=15)
        self.search_books_title_entry = tkinter.Entry(self.tab_search_books)
        self.search_books_title_entry.grid(row=1, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_books, text="Author").grid(
            row=2, column=0, padx=15, pady=15)
        self.search_books_author_entry = tkinter.Entry(self.tab_search_books)
        self.search_books_author_entry.grid(row=2, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_books, text="Year").grid(
            row=3, column=0, padx=15, pady=15)
        self.search_books_year_entry = tkinter.Entry(self.tab_search_books)
        self.search_books_year_entry.grid(row=3, column=1, padx=15, pady=15)

        tkinter.Label(self.tab_search_books, text="Publisher").grid(
            row=4, column=0, padx=15, pady=15)
        self.search_books_publisher_entry = tkinter.Entry(
            self.tab_search_books)
        self.search_books_publisher_entry.grid(
            row=4, column=1, padx=15, pady=15)

        self.search_books_cancel_button = tkinter.Button(self.tab_search_books, text="Cancel", width=10, height=1,
                                                         command=self.clear_search_books).grid(row=5, column=0, padx=15, pady=15)
        self.search_books_button = tkinter.Button(self.tab_search_books, text="Search", width=10, height=1,
                                                  command=self.search_books_from_book_dataset).grid(row=5, column=1, padx=15, pady=15)

        self.tab_search_books.grid_columnconfigure((0, 1, 2), weight=1)

    def search_books_from_book_dataset(self):
        query_book = Book(self.search_books_ISBN_entry.get(), self.search_books_title_entry.get(
        ), self.search_books_author_entry.get(), self.search_books_year_entry.get(), self.search_books_publisher_entry.get())
        query_reults = self.bookDataset.search_books(query_book)
        for book in query_reults:
            print(book)
        print("Number of results:",len(query_reults))

    def clear_search_books(self):
        self.search_books_ISBN_entry.delete(0, END)
        self.search_books_title_entry.delete(0, END)
        self.search_books_author_entry.delete(0, END)
        self.search_books_year_entry.delete(0, END)
        self.search_books_publisher_entry.delete(0, END)

    def setup_sort_books_tab(self):
        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(
            self.tab_sort_books, text='ISBN', width=15, variable=self.radio_var, value=0)
        self.rb2 = tkinter.Radiobutton(
            self.tab_sort_books, text='Title', width=15, variable=self.radio_var, value=1)
        self.rb3 = tkinter.Radiobutton(
            self.tab_sort_books, text='Author', width=15, variable=self.radio_var, value=2)
        self.rb4 = tkinter.Radiobutton(
            self.tab_sort_books, text='Year', width=15, variable=self.radio_var, value=3)
        self.rb5 = tkinter.Radiobutton(
            self.tab_sort_books, text='Publisher', width=15, variable=self.radio_var, value=4)
        self.rb6 = tkinter.Radiobutton(
            self.tab_sort_books, text='Rating', width=15, variable=self.radio_var, value=5)
        self.rb7 = tkinter.Radiobutton(
            self.tab_sort_books, text='Rating Count', width=15, variable=self.radio_var, value=6)

        self.rb1.grid(row=0, column=0)
        self.rb2.grid(row=0, column=1)
        self.rb3.grid(row=0, column=2)
        self.rb4.grid(row=1, column=0)
        self.rb5.grid(row=1, column=1)
        self.rb6.grid(row=1, column=2)
        self.rb7.grid(row=2, column=0)

        self.SearchBookButton = tkinter.Button(self.tab_sort_books, text="Sort", width=10, height=1,
                                               command=self.sort_books_in_book_dataset).grid(row=3, column=2)

        self.tab_sort_books.grid_columnconfigure((0, 1, 2), weight=1)

    def sort_books_in_book_dataset(self):
        sort_list = ["ISBN", "book_title", "book_author",
                     "year_of_publication", "publisher", "rating", "rating_count"]
        print("Sort by:", sort_list[self.radio_var.get()])
        sorted_books = self.bookDataset.sort_books(
            sort_list[self.radio_var.get()])
        for book in sorted_books:
            print(book)


if __name__ == "__main__":
    try:
        mygui = BooksDatasetUi()
    except:
        print("Error: Something Went Wrong!")
