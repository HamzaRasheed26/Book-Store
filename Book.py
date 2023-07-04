import os.path
import csv
import pandas as pd

class Book:
	def __init__(self, isbn, title, author, category, price, words, language, publish_date, book_link, image_location):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.category = category
		self.price = price
		self.words = words
		self.language = language
		self.publish_date = publish_date
		self.book_link = book_link
		self.image_location = image_location

	def setIsbn(self,isbn):
		self.isbn = isbn
	def setTitle(self,title):
		self.title = title
	def setAuthor(self,author):
		self.author = author
	def setCategory(self,category):
		self.category = category
	def setPrice(self,price):
		self.price = price
	def setWords(self,words):
		self.words = words
	def setLanguage(self,language):
		self.language = language
	def setPublish_date(self,publish_date):
		self.publish_date = publish_date
	def setBook_link(self,book_link):
		self.book_link = book_link
	def setImage_location(self,image_location):
		self.image_location = image_location
PATH = "3.csv"

Book_info = []

def add_book(book):
	Book_info.append(book)

def remove_book(index):
	Book_info.remove(Book_info[index])

def edit(idx, isbn, title, author, category, price, words, language, publish_date, book_link, image_location):
	Book_info[idx].setIsbn(isbn)
	Book_info[idx].setTitle(title)
	Book_info[idx].setAuthor(author)
	Book_info[idx].setPrice(price)
	Book_info[idx].setWords(words)
	Book_info[idx].setLanguage(language)
	Book_info[idx].setCategory(category)
	Book_info[idx].setPublish_date(publish_date)
	Book_info[idx].setBook_link(book_link)
	Book_info[idx].setImage_location(image_location)

def load_data(PATH):
	with open(PATH, "r",encoding="utf-8") as fileInput:
		data = list(csv.reader(fileInput))
		#print(data)   
		for row in data:
			title = str(row[0])
			author = str(row[1])
			price = str(row[2])
			words = str(row[3])
			language = str(row[4])
			category = str(row[5])
			publish_date = str(row[6])
			isbn = str(row[7])
			book_link = str(row[8])
			image_location = row[9]
			book = Book(isbn,title, author, category, price, words, language, publish_date, book_link, image_location)
			Book_info.append(book)

def convert_class_attr_into_array(book):
	arr = []
	arr.append(book.title)
	arr.append(book.author)
	arr.append(book.price)
	arr.append(book.words)
	arr.append(book.language)
	arr.append(book.category)
	arr.append(book.publish_date)
	arr.append(book.isbn)
	arr.append(book.book_link)
	arr.append(book.image_location)
	return arr

def store_data(book, PATH):
	arr = convert_class_attr_into_array(book)
	with open(PATH, 'a',encoding="utf-8", newline='') as f:
		writer = csv.writer(f)
		writer.writerow(arr)

def store_all_data(PATH):
	with open(PATH, 'w',encoding="utf-8", newline='') as f:
		writer = csv.writer(f)

		for row in Book_info:
			arr = convert_class_attr_into_array(row)

			writer.writerow(arr)