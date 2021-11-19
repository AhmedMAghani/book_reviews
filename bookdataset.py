import csv
import pandas as pd
import os
class Book:
    def __init__(self,ISBN,book_title,book_author,year_of_publication, publisher, rating=0.0, rating_count=0):
        self.ISBN=ISBN
        self.book_title=book_title
        self.book_author=book_author
        self.year_of_publication=year_of_publication
        self.publisher=publisher
        self.rating=rating
        self.rating_count=rating_count
    def __str__(self):
        return 'Book Information:\n ISBN: '+self.ISBN+'\n Title: ' + self.book_title + '\n Author: ' + self.book_author +'\n Year Of Publication: '+ self.year_of_publication+'\n Publisher: '+self.publisher+'\n Rating: '.format(self.rating)+'\n Rating Count: '.format(self.rating_count)
    
    def convert_to_list(self):
        return [self.ISBN, self.book_title, self.book_author, self.year_of_publication, self.publisher, self.rating, self.rating_count]

class Location:
    def __init__(self,city,state,country):
        self.city= city.strip() if city else "N/A"
        self.state= state.strip() if state else "N/A"
        self.country= country.strip() if state else "N/A"
    def __str__(self):
        return 'City: '+self.city+'\n State: ' + self.state + '\n Country: ' + self.country
    
    def __repr__(self):
        return self.city +','+ self.state +','+ self.country

class User:
    def __init__(self, user_id, location, age = None, password=None, reviewed_list=None):
        self.user_id = user_id
        location_list = list(location.split(","))
        self.location = Location(*location_list[-3:])
        self.age = age
        if password:
            self.password = password
        else:
            self._set_password()
        if reviewed_list:
            self.reviewed_list = reviewed_list
        else:
            self.reviewed_list = []

    def __str__(self):
        return 'User ID: {}, Password: {}, Location: {}, Age: {}, Reviewed List: {}'.format(self.user_id, self.password, self.location, self.age, self.reviewed_list)
    def _set_password(self):
        self.password = self.get_first_letter(self.location.city) + self.get_first_letter(self.location.state) + self.get_first_letter(self.location.country)
        if self.age is not None and self.age.strip() != "":
            self.password += str(int(float(self.age.strip())))
        else:
            self.password += str(0)
    
    def get_first_letter(self,word):
        trimed_word = word.strip()
        if trimed_word == "N/A" or trimed_word == "n/a":
            return ""
        elif trimed_word:
            return trimed_word[0]
        else:
            return ""

    def convert_to_list(self):
        return [self.user_id, self.location.__repr__(), self.age, self.password, self.reviewed_list]

class Bookdataset:
    BOOKS_CSV = "csv_folder/Books.csv"
    BOOKS_DAT = "data_folder/Books.dat"
    USER_CSV = "csv_folder/Users.csv"
    USER_DAT = "data_folder/Users.dat"
    REVIEWS = "csv_folder/Review_small.csv"
    def __init__(self):
        self.review_dataframe = pd.read_csv(Bookdataset.REVIEWS)
        self.db=[]
        self.booksList=[]
        self.usersList=[]
        if os.path.isfile(Bookdataset.BOOKS_DAT) and os.path.isfile(Bookdataset.USER_DAT):
            self.load_objs()
        else:
            self.load_books()
            self.load_users()
        self.init_rating()
        self.init_reviewed()
        self.save_objs()

    def load_books(self):
      with open(Bookdataset.BOOKS_CSV, "r") as file:
        csv_book_reader = csv.reader(file)
        next(csv_book_reader, None)
        for row in csv_book_reader:
            self.booksList.append(Book(*row))

    def load_users(self):
        with open(Bookdataset.USER_CSV, "r") as file:
            csv_user_reader = csv.reader(file)
            next(csv_user_reader, None)
            for row in csv_user_reader:
                self.usersList.append(User(*row))

    def init_rating(self):
        avg_review_per_book = self.review_dataframe.drop("User-ID",axis=1).groupby("ISBN").agg(['mean','count'])['Book-Rating']['mean'].to_dict()
        reviews_count_per_book = self.review_dataframe.drop("User-ID",axis=1).groupby("ISBN").agg(['mean','count'])['Book-Rating']['count'].to_dict()
        for book in self.booksList:
            book.rating = avg_review_per_book.get(book.ISBN,0.0)
            book.rating_count = reviews_count_per_book.get(book.ISBN,0)

    def init_reviewed(self):
        reviewed_books_per_user = self.review_dataframe.drop("Book-Rating",axis=1).groupby("User-ID")["ISBN"].agg(lambda book_list: book_list.to_list()).to_dict()
        for user in self.usersList:
            user.reviewed_list = reviewed_books_per_user.get(int(user.user_id), list())

    def load_objs(self):
        with open(Bookdataset.BOOKS_DAT,'r') as books_dat:
            books_dat_reader = csv.reader(books_dat)
            for row in books_dat_reader:
                self.booksList.append(Book(*row))

        with open(Bookdataset.USER_DAT,'r') as user_dat:
            user_dat_reader = csv.reader(user_dat)
            for row in user_dat_reader:
                self.usersList.append(User(*row))
    
    def save_objs(self):
        with open(Bookdataset.BOOKS_DAT,'w',newline='') as books_dat:
            books_writer = csv.writer(books_dat)
            for book in self.booksList:
                books_writer.writerow(book.convert_to_list())
        with open(Bookdataset.USER_DAT,'w',newline='') as users_dat:
            users_writer = csv.writer(users_dat)
            for user in self.usersList:
                users_writer.writerow(user.convert_to_list())
    
    def search_books(self,query_book):
        search_list = self.booksList
        if query_book.ISBN:
            search_list = list(filter(lambda book: book.ISBN.strip() == query_book.ISBN.strip(), search_list))
        if query_book.book_title:
            search_list = list(filter(lambda book: book.book_title.strip() == query_book.book_title.strip(), search_list))
        if query_book.book_author:
            search_list = list(filter(lambda book: book.book_author.strip() == query_book.book_author.strip(), search_list))
        if query_book.year_of_publication:
            search_list = list(filter(lambda book: book.year_of_publication.strip() == query_book.year_of_publication.strip(), search_list))
        if query_book.publisher:
            search_list = list(filter(lambda book: book.publisher.strip() == query_book.publisher.strip(), search_list))
        
        return search_list
        

    def search_users(self,query_user):
        search_list = self.usersList
        if query_user.user_id:
            search_list = list(filter(lambda user: user.user_id == query_user.user_id, search_list))
        if query_user.age:
            search_list = list(filter(lambda user: user.age == query_user.age, search_list))
        if query_user.location.city != "N/A":
            search_list = list(filter(lambda user: user.location.city.strip() == query_user.location.city.strip(), search_list))
        if query_user.location.state != "N/A":
            search_list = list(filter(lambda user: user.location.state.strip() == query_user.location.state.strip(), search_list))
        if query_user.location.country != "N/A":
            search_list = list(filter(lambda user: user.location.country.strip() == query_user.location.country.strip(), search_list))
                
        return search_list

    def sort_books(self,sort_key,reversed=False):
        if sort_key == "ISBN":
            self.booksList.sort(key=lambda book: book.ISBN,reverse=reversed)
        elif sort_key == "book_title":
            self.booksList.sort(key=lambda book: book.book_title,reverse=reversed)
        elif sort_key == "book_author":
            self.booksList.sort(key=lambda book: book.book_author,reverse=reversed)
        elif sort_key == "year_of_publication":
            self.booksList.sort(key=lambda book: book.year_of_publication,reverse=reversed)
        elif sort_key == "publisher":
            self.booksList.sort(key=lambda book: book.publisher,reverse=reversed)
        elif sort_key == "rating":
            self.booksList.sort(key=lambda book: book.rating,reverse=reversed)
        elif sort_key == "rating_count":
            self.booksList.sort(key=lambda book: book.rating_count,reverse=reversed)
        
        return self.booksList