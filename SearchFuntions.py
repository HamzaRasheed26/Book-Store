import Book
import math

# linear search function for data type string
def linearSearch(array,text, filter):
    result = []
    books = []
    for idx in range(len(array)):
        item = str(array[idx])

        # searching Filters
        if filter == 0: # Fiter if contains
            if item.find(text) != -1:
                books.append(Book.Book_info[idx])

        elif filter == 1: # if not contains
            if item.find(text) == -1:
                books.append(Book.Book_info[idx])

        elif filter == 2: # is equal to 
            if text == item:
                books.append(Book.Book_info[idx])

        elif filter == 3: # not equal to
            if text != item:
                books.append(Book.Book_info[idx])

        elif filter == 4: # starts with
            if item.find(text) == 0:
                books.append(Book.Book_info[idx])

        elif filter == 5: # ends with
            if item.find(text) == (len(item)- len(text)):
                books.append(Book.Book_info[idx])

        elif filter == 6: # is empty
            if item  == "":
                books.append(Book.Book_info[idx])

        elif filter == 7: # is not empty
            if item  != "":
                books.append(Book.Book_info[idx])

    return books

# linear search function for data type int or float
def linearSearchIntegar(array,text, filter):
    
    if text == "":
        text = '0'

    text = float(text)
    books = []
    for idx in range(len(array)):
        item = float(array[idx])
        
        # searching Filters
        if filter == 0: # Equal to
            if item == text:
                books.append(Book.Book_info[idx])

        elif filter == 1: # not equal to
            if item != text:
                books.append(Book.Book_info[idx])

        elif filter == 2: # Greater than
            if text < item:
                books.append(Book.Book_info[idx])

        elif filter == 3: # Less than
            if text > item:
                books.append(Book.Book_info[idx])

        elif filter == 4: # Greater and equal to
            if text <= item:
                books.append(Book.Book_info[idx])

        elif filter == 5: # Less and equal to
            if text >= item:
                books.append(Book.Book_info[idx])

        elif filter == 6: # Is zero
            if item  == 0:
                books.append(Book.Book_info[idx])

        elif filter == 7: # is not zero
            if item  != 0.0:
                books.append(Book.Book_info[idx])

    return books


def BinarySearch(array,text,low,high, books, filter):
        if high > low:
            mid= (high+low)//2

            if text == array[mid] :
                books.append(Book.Book_info[mid])
                BinarySearch(array,text,low,mid, books, filter)
            if array[mid] > text:
                return BinarySearch(array,text,low,mid , books, filter)
            else:
                return BinarySearch(array,text,mid+1,high , books, filter)


def Sort(array):
    n = len(array)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            
            array[j] = temp
        interval //= 2

    return array

def jumpSearch(array, text, filter):
    print("Entering Jump Search")
    n = len(array)                          
    m = int(math.sqrt(n))         
    i = 0                               

    while i != len(array)-1 and array[i] < text:
        if array[i+m-1] == text: 
            return i+m-1
        elif array[i+m-1] > text:      
            B = array[i: i+m-1]
            return linearSearch(B, text, filter)
        i += m

    B = array[i:i+m]
    return linearSearch(B, text, filter)