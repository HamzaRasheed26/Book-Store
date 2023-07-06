# importing librarires for different tasks.
from array import array
from re import S
import sys
from turtle import color
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import webbrowser
import Book
import SortingFuncs as sortF
import time
import SearchFuntions as searchF


# class for login page
class Login_Page(QMainWindow):
    def __init__(self):
        super(Login_Page, self).__init__()
        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("Login_Page_1.ui", self)

        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # Command to make the backgroud of Window transparent.
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # These 2 lines are used to put funnctions on close and minimize buttons.
        #self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        self.CrossButton.clicked.connect(lambda: self.close())
        self.sign_in_btn.clicked.connect(lambda: self.checkCredentials())

    # checking the credentials input by uesr
    def checkCredentials(self):
        username = self.username_text_box.text()
        password = self.password_text_box.text()

        print(username)
        print(password)

        if username == "admin" and password == "123":
            # Jumping to Home page 
            self.window = Home_Page()
            self.window.show()
            self.close()


# class for home page
class Home_Page(QMainWindow):
    def __init__(self):
        super(Home_Page, self).__init__()

        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("HomePage.ui", self)

        # Function to load the previous data of student at the start of program.
        
        self.load_table()
        self.books_table.hideColumn(8)
        self.books_table.hideColumn(9)
        self.remove_btn.clicked.connect(lambda: self.remove_data())
        self.view_btn.clicked.connect(lambda: self.view_book_info())
        self.Edit_btn.clicked.connect(lambda: self.edit_book_info())
        self.Add_btn.clicked.connect(lambda: self.add_book_info())
        self.sort_btn.clicked.connect(lambda: self.sorting_window())
        self.search_btn.clicked.connect(lambda: self.search_window())
        self.reset_btn.clicked.connect(lambda: self.load_table())
        self.multiSort_btn.clicked.connect(lambda: self.MultiSorting_window())
    
    def edit_book_info(self):
        idx = self.books_table.currentRow()
        print("index",idx)
        if idx >= 0 and idx < self.books_table.rowCount():
            BookData = []
            BookData.append(self.books_table.item(idx,0).text())
            BookData.append(self.books_table.item(idx,1).text())
            BookData.append(self.books_table.item(idx,2).text())
            BookData.append(self.books_table.item(idx,3).text())
            BookData.append(self.books_table.item(idx,4).text())
            BookData.append(self.books_table.item(idx,5).text())
            BookData.append(self.books_table.item(idx,6).text())
            BookData.append(self.books_table.item(idx,7).text())
            BookData.append(self.books_table.item(idx,8).text())
            BookData.append(self.books_table.item(idx,9).text())

            print(BookData)

            mydialog = edit_page(BookData, self.books_table, idx)
            mydialog.setModal(True)
            mydialog.exec()
        else:
            msg=QMessageBox()
            msg.setWindowTitle("--- Book Store ---")
            msg.setText("Please Select a Book.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()

    def add_book_info(self):
        mydialog = add_page(self.books_table)
        mydialog.setModal(True)
        mydialog.exec()

    # function to view book info in seprate window
    def view_book_info(self):
        idx = self.books_table.currentRow()
        print("index",idx)
        if idx >= 0 and idx < self.books_table.rowCount():
            BookData = []
            BookData.append(self.books_table.item(idx,0).text())
            BookData.append(self.books_table.item(idx,1).text())
            BookData.append(self.books_table.item(idx,2).text())
            BookData.append(self.books_table.item(idx,3).text())
            BookData.append(self.books_table.item(idx,4).text())
            BookData.append(self.books_table.item(idx,5).text())
            BookData.append(self.books_table.item(idx,6).text())
            BookData.append(self.books_table.item(idx,7).text())
            BookData.append(self.books_table.item(idx,8).text())
            BookData.append(self.books_table.item(idx,9).text())

            print(BookData)

            self.window = Info_Page(BookData, self.books_table)
            self.window.show()
        else:
            msg=QMessageBox()
            msg.setWindowTitle("--- Book Store ---")
            msg.setText("Please Select a Book.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()


    # function to remove data from table
    def remove_data(self):
        idx = self.books_table.currentRow()
        
        if idx >= 0 and idx < self.books_table.rowCount():
            self.books_table.removeRow(idx)
            Book.remove_book(idx)
            Book.store_all_data(PATH)
        else:
            msg=QMessageBox()
            msg.setWindowTitle("--- Book Store ---")
            msg.setText("Please Select a Book.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()

    
    # This is a helping Function to load the content of the table after every event.
    def load_table(self):
        
        roww = 0
        self.books_table.setRowCount(len(Book.Book_info))
        for book in Book.Book_info:
            print("wait")
            if type(book) != Book.Book:
                Book.Book_info.remove(book)
                continue
            self.books_table.setItem(roww, 0 , QtWidgets.QTableWidgetItem((book.title)))
            self.books_table.setItem(roww, 1 , QtWidgets.QTableWidgetItem((book.author)))
            self.books_table.setItem(roww, 2 , QtWidgets.QTableWidgetItem((book.price)))
            self.books_table.setItem(roww, 3 , QtWidgets.QTableWidgetItem((book.words)))
            self.books_table.setItem(roww, 4 , QtWidgets.QTableWidgetItem((book.language)))
            self.books_table.setItem(roww, 5 , QtWidgets.QTableWidgetItem((book.category)))
            self.books_table.setItem(roww, 6 , QtWidgets.QTableWidgetItem((book.publish_date)))
            self.books_table.setItem(roww, 7 , QtWidgets.QTableWidgetItem((book.isbn)))
            self.books_table.setItem(roww, 8 , QtWidgets.QTableWidgetItem((book.book_link)))
            self.books_table.setItem(roww, 9 , QtWidgets.QTableWidgetItem((book.image_location)))
            roww += 1

    # opening sorting dialogue
    def sorting_window(self):
        mydialog = sorting_window(self.lbl_time)
        mydialog.setModal(True)
        mydialog.exec()
        self.load_table()

    # opening sorting dialogue
    def MultiSorting_window(self):
        mydialog = MultiSorting_window(self.lbl_time)
        mydialog.setModal(True)
        mydialog.exec()
        self.load_table()
        
    # opening searching dialogue
    def search_window(self):
        mydialog = searching_window(self.books_table, self.lbl_time)
        mydialog.setModal(True)
        mydialog.exec()
        
# class for home page
class Info_Page(QMainWindow):
    def __init__(self, BookData, table):
        super(Info_Page, self).__init__()

        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("BookInfo.ui", self)

        self.b = table.currentRow()

        # Adding data of Book into labels
        self.lblBookTitle.setText(BookData[0])
        self.lblAuthor.setText(BookData[1])
        self.lblCategory.setText(BookData[5])
        if BookData[2] != "0":
            self.lblPrice.setText(BookData[2] + "$")
        else:
            self.lblPrice.setText("Free")
        self.lblWords.setText(BookData[3])
        self.lblLanguage.setText(BookData[4])
        self.lblISBN.setText(BookData[7])
        self.lblPublishDate.setText(BookData[6])
        self.pixmap = QPixmap(BookData[9])
        self.label_9.setPixmap(self.pixmap)

        self.btnViewWebsite.clicked.connect(lambda: self.openingWebsiteLink(BookData[8]))
        self.btnNext.clicked.connect(lambda: next_book(BookData))
        self.btnPrevious.clicked.connect(lambda: previous_book(BookData))

        def next_book(BookData ):
            # Adding data of Book into labels

            idx = self.b + 1
            if idx < table.rowCount():
                self.b += 1
                name = table.item(idx, 0).text()
                author = table.item(idx, 1).text()
                category = table.item(idx , 5).text()
                price = table.item(idx , 2).text()
                word = table.item(idx , 3).text()
                language = table.item(idx , 4).text()
                isbn = table.item(idx , 7).text()
                publish = table.item(idx , 6).text()
                BookData[8] = table.item(idx , 8).text()
                imageLocation = table.item(idx , 9).text()

                self.lblBookTitle.setText(name)
                self.lblAuthor.setText(author)
                self.lblCategory.setText(category)
                if price != "0":
                    self.lblPrice.setText(price + "$")
                else:
                    self.lblPrice.setText("Free")
                self.lblWords.setText(word)
                self.lblLanguage.setText(language)
                self.lblISBN.setText(isbn)
                self.lblPublishDate.setText(publish)
                self.pixmap = QPixmap(imageLocation)
                self.label_9.setPixmap(self.pixmap)

        def previous_book(BookData):
            # Adding data of Book into labels
            if self.b >= 1:
                name = table.item(self.b - 1, 0).text()
                author = table.item(self.b - 1, 1).text()
                category = table.item(self.b - 1, 5).text()
                price = table.item(self.b - 1, 2).text()
                word = table.item(self.b - 1, 3).text()
                language = table.item(self.b - 1, 4).text()
                isbn = table.item(self.b - 1, 7).text()
                publish = table.item(self.b - 1, 6).text()
                BookData[8] = table.item(self.b - 1 , 8).text()
                imageLocation = table.item(self.b - 1, 9).text()

                self.b -= 1

                self.lblBookTitle.setText(name)
                self.lblAuthor.setText(author)
                self.lblCategory.setText(category)
                if price != "0":
                    self.lblPrice.setText(price + "$")
                else:
                    self.lblPrice.setText("Free")
                self.lblWords.setText(word)
                self.lblLanguage.setText(language)
                self.lblISBN.setText(isbn)
                self.lblPublishDate.setText(publish)
                self.pixmap = QPixmap(imageLocation)
                self.label_9.setPixmap(self.pixmap)

    # function for opening book link on chrome or default internet browser
    def openingWebsiteLink(self, url):
        if url == "":
            webbrowser.open_new("https://www.smashwords.com/books/category/1/newest/0/any/any/0")
        else:
            webbrowser.open_new(url)

# class for edit page
class edit_page(QDialog):
    def __init__(self, BookData, table, idx):
        super(edit_page, self).__init__()

        self.filename = ""
        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("EditBook.ui", self) 

        print(BookData)

        self.isbn_line_edit.setText(BookData[7])
        self.title_line_edit.setText(BookData[0])
        self.author_line_edit.setText(BookData[1])
        self.category_line_edit.setText(BookData[5])
        self.price_line_edit.setText(BookData[2])
        self.word_line_edit.setText(BookData[3])
        self.language_line_edit.setText(BookData[4])
        self.published_date_line_edit.setText(BookData[6])
        self.open_file_lbl.setText("Open File: " + BookData[9])

        self.clear_btn.clicked.connect(lambda: self.clear_fields())
        self.update_btn.clicked.connect(lambda: self.edit_book(table, idx))
        self.file_dialog_btn.clicked.connect(lambda: self.open_dialog())

    def clear_fields(self):
        self.isbn_line_edit.setText("")
        self.title_line_edit.setText("")
        self.author_line_edit.setText("")
        self.category_line_edit.setText("")
        self.price_line_edit.setText("")
        self.word_line_edit.setText("")
        self.language_line_edit.setText("")
        self.published_date_line_edit.setText("")
        self.open_file_lbl.setText("Open File: ")

    def edit_book(self, table, idx):
        if (self.title_line_edit.text() != "" and self.author_line_edit.text() != "" and self.price_line_edit.text() != "" and self.word_line_edit.text() != "" and self.language_line_edit.text() != "" and self.category_line_edit.text() != "" and self.published_date_line_edit.text() != "" and self.isbn_line_edit.text() != "" and self.open_file_lbl.text() != "Open File: "):
            data = []
            
            title = self.title_line_edit.text()
            author = self.author_line_edit.text()
            price = self.price_line_edit.text()
            word = self.word_line_edit.text()
            language = self.language_line_edit.text()
            category = self.category_line_edit.text()
            publish_date = self.published_date_line_edit.text()
            isbn = self.isbn_line_edit.text()
            image_location = self.filename[0]

            Book.edit(idx, isbn, title, author, category, price, word, language, publish_date, "", image_location)
            Book.store_all_data(PATH)

            data.append(self.title_line_edit.text())
            data.append(self.author_line_edit.text())
            data.append(self.price_line_edit.text())
            data.append(self.word_line_edit.text())
            data.append(self.language_line_edit.text())
            data.append(self.category_line_edit.text())
            data.append(self.published_date_line_edit.text())
            data.append(self.isbn_line_edit.text())

            data.append("")
            location = self.open_file_lbl.text()
            location = location.replace("Open File: ","")
            data.append(location)
            print("Location: ", location)

            table.setItem(idx, 0 , QtWidgets.QTableWidgetItem(data[0]))
            table.setItem(idx, 1 , QtWidgets.QTableWidgetItem((data[1])))
            table.setItem(idx, 2 , QtWidgets.QTableWidgetItem((data[2])))
            table.setItem(idx, 3 , QtWidgets.QTableWidgetItem((data[3])))
            table.setItem(idx, 4 , QtWidgets.QTableWidgetItem((data[4])))
            table.setItem(idx, 5 , QtWidgets.QTableWidgetItem((data[5])))
            table.setItem(idx, 6 , QtWidgets.QTableWidgetItem((data[6])))
            table.setItem(idx, 7 , QtWidgets.QTableWidgetItem((data[7])))
            table.setItem(idx, 8 , QtWidgets.QTableWidgetItem((data[8])))
            table.setItem(idx, 9 , QtWidgets.QTableWidgetItem((data[9])))

            self.close()
        else:
            msg=QMessageBox()
            msg.setWindowTitle("--- Book Store ---")
            msg.setText("Please Fill all the required input.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()

    def open_dialog(self):
        self.filename = QFileDialog.getOpenFileName(self, "Open File", "", "All File (*);; Jpg File (*jpg);; PNG File (*png)")

        self.open_file_lbl.setText(self.open_file_lbl.text() + str(self.filename[0]))
        if self.filename:
            print(self.filename[0])
            self.open_file_lbl.setText("Open File: " + self.filename[0])

# class for add page
class add_page(QDialog):
    def __init__(self, table):
        super(add_page, self).__init__()
        self.filename = ""
        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("Add_Page.ui", self) 

        self.clear_btn.clicked.connect(lambda: self.clear_fields())
        self.add_btn.clicked.connect(lambda: self.add_book(table))
        self.file_dialog_btn.clicked.connect(lambda: self.open_dialog())

    def clear_fields(self):
        self.isbn_line_edit.setText("")
        self.title_line_edit.setText("")
        self.author_line_edit.setText("")
        self.category_line_edit.setText("")
        self.price_line_edit.setText("")
        self.word_line_edit.setText("")
        self.language_line_edit.setText("")
        self.published_date_line_edit.setText("")
        self.open_file_lbl.setText("Open File: ")

    def add_book(self, table):
        if (self.title_line_edit.text() != "" and self.author_line_edit.text() != "" and self.price_line_edit.text() != "" and self.word_line_edit.text() != "" and self.language_line_edit.text() != "" and self.category_line_edit.text() != "" and self.published_date_line_edit.text() != "" and self.isbn_line_edit.text() != "" and self.open_file_lbl.text() != "Open File: "):
            data = []
            title = self.title_line_edit.text()
            author = self.author_line_edit.text()
            price = self.price_line_edit.text()
            word = self.word_line_edit.text()
            language = self.language_line_edit.text()
            category = self.category_line_edit.text()
            publish_date = self.published_date_line_edit.text()
            isbn = self.isbn_line_edit.text()
            image_location = self.filename[0]

            book = Book.Book(isbn, title, author, category, price, word, language, publish_date, "", image_location)

            data.append(self.title_line_edit.text())
            data.append(self.author_line_edit.text())
            data.append(self.price_line_edit.text())
            data.append(self.word_line_edit.text())
            data.append(self.language_line_edit.text())
            data.append(self.category_line_edit.text())
            data.append(self.published_date_line_edit.text())
            data.append(self.isbn_line_edit.text())
            data.append("")
            data.append(self.filename[0])

            Book.add_book(book)
            Book.store_data(book,PATH)

            currentRow = table.currentRow()
            table.insertRow(currentRow+1)

            table.setItem(currentRow+1, 0 , QtWidgets.QTableWidgetItem(data[0]))
            table.setItem(currentRow+1, 1 , QtWidgets.QTableWidgetItem((data[1])))
            table.setItem(currentRow+1, 2 , QtWidgets.QTableWidgetItem((data[2])))
            table.setItem(currentRow+1, 3 , QtWidgets.QTableWidgetItem((data[3])))
            table.setItem(currentRow+1, 4 , QtWidgets.QTableWidgetItem((data[4])))
            table.setItem(currentRow+1, 5 , QtWidgets.QTableWidgetItem((data[5])))
            table.setItem(currentRow+1, 6 , QtWidgets.QTableWidgetItem((data[6])))
            table.setItem(currentRow+1, 7 , QtWidgets.QTableWidgetItem((data[7])))
            table.setItem(currentRow+1, 8 , QtWidgets.QTableWidgetItem((data[8])))
            table.setItem(currentRow+1, 9 , QtWidgets.QTableWidgetItem((data[9])))

            self.close()
        else:
            msg=QMessageBox()
            msg.setWindowTitle("--- Book Store ---")
            msg.setText("Please Fill all the required input.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()

    def open_dialog(self):
        self.filename = QFileDialog.getOpenFileName(self, "Open File", "", "All File (*);; Jpg File (*jpg);; PNG File (*png)")

        self.open_file_lbl.setText(self.open_file_lbl.text() + str(self.filename[0]))
        if self.filename:
            print(self.filename[0])

# class for multi level sorting ui page
class MultiSorting_window(QDialog):
    def __init__(self,lbl_time, parent =None):
        super(MultiSorting_window, self).__init__(parent)

        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("MultiLevelSort.ui", self)

        self.ascending_radio_button.setChecked(True)

        self.cancel_btn.clicked.connect(lambda: self.close_window())
        self.sort_btn.clicked.connect(lambda: self.sortCol(lbl_time))

    def close_window(self):
        self.close()

    def selectCol(self, idx, lists):
        array = []
        if idx == 0:
            array = lists[0] # title
        elif idx == 1:
            array = lists[1] # author
        elif idx == 2:
            array = lists[5] # category
        elif idx == 3:
            array = lists[2] # price
        elif idx == 4:
            array = lists[3] # words
        elif idx == 5:
            array = lists[4] # languages
        elif idx == 6:
            array = lists[8] # publishes
        elif idx == 7:
            array = lists[6] # isbns
        return array

    def sortCol(self,lbl_time):
        self.hide()
        
        lbl_time.setText("Time : "  + "calculating......")
        lists = sortF.Convert_to_seprate_lists()

        # selecting order Ascending/Descending
        order = ""
        if(self.ascending_radio_button.isChecked()):
            order = "Asc"
        if(self.descending_radio_button.isChecked()):
            order = "Des"
        
        # selecting col from first combo box 
        idx = self.column_sort_combo_box.currentIndex()
        array1 = self.selectCol(idx, lists)

        # selecting col from second combo box
        idx = self.column_sort_combo_box_2.currentIndex()
        array2 = self.selectCol(idx, lists)

        start = time.time()
        # calling Multi Level sorting Function
        sortF.MultiLevelSorting(array1, array2, order)

        end = time.time()
        lbl_time.setText("Time : " + str(end - start) + "sec")

        self.close()

# class for sorting ui page
class sorting_window(QDialog):
    def __init__(self,lbl_time, parent =None):
        super(sorting_window, self).__init__(parent)

        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("Sorting.ui", self)

        self.ascending_radio_button.setChecked(True)

        self.cancel_btn.clicked.connect(lambda: self.close_window())
        self.sort_btn.clicked.connect(lambda: self.sortDecide(lbl_time))
        
    def close_window(self):
        self.close()

    def sortDecide(self,lbl_time):
        self.hide()
        
        lbl_time.setText("Time : "  + "calculating......")
        lists = sortF.Convert_to_seprate_lists()

        i = self.column_sort_combo_box.currentIndex()
        if i == 0:
            array = lists[0] # title
        elif i == 1:
            array = lists[1] # author
        elif i == 2:
            array = lists[5] # category
        elif i == 3:
            array = lists[2] # price
        elif i == 4:
            array = lists[3] # words
        elif i == 5:
            array = lists[4] # languages
        elif i == 6:
            array = lists[8] # publishes
        elif i == 7:
            array = lists[6] # isbns

        order = ""
        if(self.ascending_radio_button.isChecked()):
            order = "Asc"
        if(self.descending_radio_button.isChecked()):
            order = "Des"

        start = time.time()
        if self.sort_by_combo_box.currentText() == "Insertion Sort":
            # insertion sort
            sortF.InsertionSort(array,0 , len(array)-1, order)

        elif self.sort_by_combo_box.currentText() == "Selection Sort":
            # selection sort
            sortF.SelectionSort(array,0 , len(array)-1, order)

        elif self.sort_by_combo_box.currentText() == "Bubble Sort":
            # Bubble sort
            sortF.BubbleSort(array,0 , len(array)-1, order)
        
        elif self.sort_by_combo_box.currentText() == "Quick Sort":
            # Quick sort
            sortF.quickSort(array,0 , len(array)-1, order)

        elif self.sort_by_combo_box.currentText() == "Merge Sort":
            # Merge Sort
            sortF.MergeSort(array, 0, len(array)-1, order)

        elif self.sort_by_combo_box.currentText() == "Hybrid Sort":
            # HybridMerge Sort
            sortF.HybridMergeSort(array, 0, len(array)-1, order)

        elif self.sort_by_combo_box.currentText() == "Heap Sort":
            # sorting function
            sortF.HeapSort(array, order)

        elif self.sort_by_combo_box.currentText() == "Shell Sort":
            # sorting function
            sortF.shellSort(array, len(array), order)
            
        elif self.sort_by_combo_box.currentText() == "Smooth Sort":
            return
            # sorting function
        elif self.sort_by_combo_box.currentText() == "Counting Sort":
            sortF.CountingSort(array, order)
            
        elif self.sort_by_combo_box.currentText() == "Radix Sort":
            # sorting function
            return
        elif self.sort_by_combo_box.currentText() == "Bucket Sort":
            return
            # sorting function
        

        end = time.time()
        lbl_time.setText("Time : " + str(end - start) + "sec")

        self.close()

# class for searching ui page
class searching_window(QDialog):
    def __init__(self,books_table, lbl_time):
        super(searching_window, self).__init__()

        # Here we imported the QT Designer file which we made as Python GUI FIle.
        loadUi("Search.ui", self)

        self.cb_Column.currentTextChanged.connect(lambda: self.filterChange())
        self.btn_Cancel.clicked.connect(lambda: self.close_window())
        self.btn_Search.clicked.connect(lambda: self.search_decide(books_table, lbl_time))

    def close_window(self):
        self.close()

    def filterChange(self):
        i = self.cb_Column.currentIndex()
        
        print(i)
        if i == 2 or i == 3:
            self.cb_Filter.clear()
            colItems = [ "Equal to", "Not Equal", "Greater than", "Less than", "Greater and equal to","Less and equal to","Is zero", "Is not zero"]
            self.cb_Filter.addItems(colItems)
        else:
            self.cb_Filter.clear()
            colItems = ["Contains", "Not Contains", "is equal to", "Is not equal to", "Starts with", "Ends with", "Is empty", "Is not empty"]
            self.cb_Filter.addItems(colItems)

    def search_decide(self,books_table, lbl_time):
        
        lists = sortF.Convert_to_seprate_lists()
        # these lines are used to select on which operation will perform 
        i = self.cb_Column.currentIndex()
        if i == 0:
            array = lists[0] # title
        elif i == 1:
            array = lists[1] # author
        elif i == 2:
            array = lists[2] # price
        elif i == 3:
            array = lists[3] # words
        elif i == 4:
            array = lists[4] # languages
        elif i == 5:
            array = lists[5] # category
        elif i == 6:
            array = lists[8] # publishes
        elif i == 7:
            array = lists[6] # isbns

        filter = self.cb_Filter.currentIndex()
        text = self.input.text()
        
        start = time.time()

        # here we choose searching function
        if self.cb_Search.currentText() == "Linear Search":
            # Linear Search
            if i == 2 or i == 3:
                # search function if colunm data type is int or float
                arr = searchF.linearSearchIntegar(array, text, filter)
                self.load_table(books_table, arr)
            else:
                # search function if colunm data type is string
                arr = searchF.linearSearch(array, text, filter)
                self.load_table(books_table, arr)

        elif self.cb_Search.currentText() == "Binary Search":
            books = []
            #array = searchF.Sort(array)
            searchF.BinarySearch(array,text,0,len(array)-1, books, filter)
            self.load_table(books_table, books)

        if self.cb_Search.currentText() == "Jump Search":
            # Jump Search
            arr = searchF.jumpSearch(array, text, filter)
            self.load_table(books_table, arr)

        end = time.time()
        lbl_time.setText("Time : " + str(end - start) + "sec")
        self.close()
    
    # This is a helping Function to load the content of the table after every event.
    def load_table(self, books_table, array):
        
        roww = 0
        books_table.setRowCount(len(array))
        for book in array:
            if type(book) != Book.Book:
                array.remove(book)
                continue
            books_table.setItem(roww, 0 , QtWidgets.QTableWidgetItem((book.title)))
            books_table.setItem(roww, 1 , QtWidgets.QTableWidgetItem((book.author)))
            books_table.setItem(roww, 2 , QtWidgets.QTableWidgetItem((book.price)))
            books_table.setItem(roww, 3 , QtWidgets.QTableWidgetItem((book.words)))
            books_table.setItem(roww, 4 , QtWidgets.QTableWidgetItem((book.language)))
            books_table.setItem(roww, 5 , QtWidgets.QTableWidgetItem((book.category)))
            books_table.setItem(roww, 6 , QtWidgets.QTableWidgetItem((book.publish_date)))
            books_table.setItem(roww, 7 , QtWidgets.QTableWidgetItem((book.isbn)))
            books_table.setItem(roww, 8 , QtWidgets.QTableWidgetItem((book.book_link)))
            books_table.setItem(roww, 9 , QtWidgets.QTableWidgetItem((book.image_location)))
            roww += 1

# main body of code
PATH = "DATA17.csv"
Book.load_data(PATH)
app = QApplication(sys.argv)
window = Home_Page()
window.show()
sys.exit(app.exec_())
