# importing librarires for different tasks.
import Book


def Convert_to_seprate_lists():
    
    titles = []
    authors = []
    prices = []
    words = []
    language = []
    categories = []
    isbns = []
    links = []
    publishes = []
    images = []

    for b in Book.Book_info:
        if type(b) != Book.Book:
                Book.Book_info.remove(b)
        titles.append(b.title)
        authors.append(b.author)
        prices.append(float(b.price))
        words.append(int(b.words)) 
        language.append(b.language)
        categories.append(b.category)
        isbns.append(b.isbn)
        links.append(b.book_link)
        publishes.append(b.publish_date)
        images.append(b.image_location)

    return [titles,authors,prices,words,language,categories,isbns,links,publishes,images]
# function for sorting array using insertion sorting algorithm

def InsertionSort(Array,start,end, order):
        for i in range(start,end):
            key=Array[i]
            print(key)
            k = Book.Book_info[i]

            j=i-1
            if order == "Asc":
                while (key< Array[j] and j>=0):
                    Array[j+1]=Array[j]
                    Book.Book_info[j+1] = Book.Book_info[j]
                    j=j-1
            elif order == "Des":
                while (key> Array[j] and j>=0):
                    Array[j+1]=Array[j]
                    Book.Book_info[j+1] = Book.Book_info[j]
                    j=j-1
            Array[j+1]=key
            Book.Book_info[j+1] = k
        return Array

def SelectionSort(Array, start, end, order):
    length = end
    for i in range(length - 1):
        minIndex = i
        if(order == "Asc"):
            for j in range(i + 1, length):
                if (Array[j] < Array[minIndex]):
                    minIndex = j
            Array[i], Array[minIndex] = Array[minIndex], Array[i]
            Book.Book_info[i], Book.Book_info[minIndex] = Book.Book_info[minIndex], Book.Book_info[i]
        elif(order == "Des"):
            for j in range(i + 1, length):
                if (Array[j] > Array[minIndex]):
                    minIndex = j
            Array[i], Array[minIndex] = Array[minIndex], Array[i]
            Book.Book_info[i], Book.Book_info[minIndex] = Book.Book_info[minIndex], Book.Book_info[i]
    return Array

def BubbleSort(array, start, end, mode):
    i = len(array)
    Sorted = False
    while ((i > 1) and not(Sorted)):
        Sorted = True
        for j in range(start, end, 1):
            if mode == "Asc":
                if (array[j-1] > array[j]):
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
                    temp_1 = Book.Book_info[j-1]
                    Book.Book_info[j-1] = Book.Book_info[j]
                    Book.Book_info[j] = temp_1
                    Sorted = False
            if mode == "Des":
                if (array[j-1] < array[j]):
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
                    temp_1 = Book.Book_info[j-1]
                    Book.Book_info[j-1] = Book.Book_info[j]
                    Book.Book_info[j] = temp_1
                    Sorted = False
        i -= 1

def partition(array, low, high, mode):
    pivot = array[high]

    i = low - 1
    if mode == "Asc":
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])
                (Book.Book_info[i], Book.Book_info[j]) = (Book.Book_info[j], Book.Book_info[i])

    if mode == "Des":
        for j in range(low, high):
            if array[j] >= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])
                (Book.Book_info[i], Book.Book_info[j]) = (Book.Book_info[j], Book.Book_info[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    (Book.Book_info[i + 1], Book.Book_info[high]) = (Book.Book_info[high], Book.Book_info[i + 1])

    return i + 1

def quickSort(array, low, high, mode):
    if low < high:
        pi = partition(array, low, high, mode)

        quickSort(array, low, pi - 1, mode)

        quickSort(array, pi + 1, high, mode)


# function for merging array using merge algorithm
def Merge(A, p, q, r, order):
    n1 = q-p +1
    n2 = r-q
    L = [0]*(n1)
    R = [0]*(n2)

    BL = [0]*(n1)
    BR = [0]*(n2)

    for i in range(n1):
        L[i] = A[p+i]
        BL[i] = Book.Book_info[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
        BR[j] = Book.Book_info[q+j+1]
    i = 0   
    j = 0     
    k = p 
    
    while i < n1 and j < n2:
        if order == "Asc":
            if L[i] <= R[j]:
                A[k] = L[i]
                Book.Book_info[k]= BL[i]
                i += 1
            else:
                A[k] = R[j]
                Book.Book_info[k]= BR[j]
                j += 1
            k += 1
        elif order == "Des":
            if L[i] <= R[j]:
                A[k] = R[j]
                Book.Book_info[k]= BR[j]
                j += 1
            else:
                A[k] = L[i]
                Book.Book_info[k]=  BL[i]
                i += 1
            k += 1
    while i < n1:
        A[k] = L[i]
        Book.Book_info[k]=  BL[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        Book.Book_info[k]=  BR[j]
        j += 1
        k += 1
            
# function for sorting array using merge sorting algorithm
def MergeSort(A, p, r, order):
    if p < r:
        q = int((p+r)/2)
        
        MergeSort(A, p, q, order)
        MergeSort(A, q+1, r, order)
        Merge(A, p, q, r, order)


def heapify(arr, N, i, order):
    largest = i  
    l = 2 * i     
    r = 2 * i + 1    
    
    if order == "Asc":
        if l < N and arr[largest] < arr[l]:
            largest = l
        
        if r < N and arr[largest] < arr[r]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            #print(arr[i])
            Book.Book_info[i], Book.Book_info[largest] = Book.Book_info[largest], Book.Book_info[i]
            heapify(arr, N, largest, order)
    elif order == "Des":
        if l < N and arr[largest] > arr[l]:
            largest = l
        
        if r < N and arr[largest] > arr[r]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            #print(arr[i])
            Book.Book_info[i], Book.Book_info[largest] = Book.Book_info[largest], Book.Book_info[i]
            heapify(arr, N, largest, order)

def BuildMaxHeap(arr, order):
    N = len(arr)
    
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i, order)

def HeapSort(array, order):
    print("In")
    BuildMaxHeap(array, order)
    N = len(array)

    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i] 
        Book.Book_info[i], Book.Book_info[0] = Book.Book_info[0], Book.Book_info[i] 
        heapify(array, i, 0, order)

    return array

def shellSort(array, n, order):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            tempBook = Book.Book_info[i]
            j = i
            if order == "Asc":
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    Book.Book_info[j] = Book.Book_info[j - interval]
                    j -= interval
            elif order == "Des":
                while j >= interval and array[j - interval] < temp:
                    array[j] = array[j - interval]
                    Book.Book_info[j] = Book.Book_info[j - interval]
                    j -= interval

            array[j] = temp
            Book.Book_info[j] = tempBook
        interval //= 2

def reverse_array(array):
    arr = [0]*len(array)

    k = 0
    for i in range(len(array)-1,-1,-1):
        print(array[i])
        arr[k] = array[i]
        Book.Book_info[k] = array[i]
        print("K: " ,arr[k])
        k += 1
    print(arr)
    return arr

def convert_to_integers(array):
    for i in range(len(array)):
        array[i] = int(array[i])

    return array

def CountingSort(arr, order):
    array = convert_to_integers(arr)
    size = max(array)

    output = [0] * len(array)

    # Initialize count array
    count = [0] * (size+1)

    # Store the count of each elements in count array
    for i in range(0, len(array)):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, size+1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = len(array) - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, len(array)):
        array[i] = output[i]
        Book.Book_info[i] = output[i]
    print(Book.Book_info)
    if order == "Des":
        return reverse_array(array)
    return array

def HybridMergeSort(A, p, r, order):
    dif = r - p
    if (p < r ):
        if dif > 43:
            q = (p + r)//2
            HybridMergeSort(A, p, q, order)
            HybridMergeSort(A, q+1, r, order)
            Merge(A, p, q, r, order)
        else:
            InsertionSort(A, p, r, order)
            p = r

# function for merging array using merge algorithm
def MultiMerge(A, B, p, q, r, order):
    n1 = q-p +1
    n2 = r-q 
    L = [0]*(n1)
    R = [0]*(n2)

    BL = [0]*(n1)
    BR = [0]*(n2)

    BookL = [0]*(n1)
    BookR = [0]*(n2)

    for i in range(n1):
        L[i] = A[p+i]
        BL[i] = B[p+i]
        BookL[i] = Book.Book_info[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
        BR[j] = B[q+j+1]
        BookR[j] = Book.Book_info[q+j+1]
    i = 0   
    j = 0     
    k = p 
    
    while i < n1 and j < n2:
        if order == "Asc":
            if L[i] <= R[j]:
                A[k] = L[i]
                B[k] = BL[i]
                Book.Book_info[k]= BookL[i]
                i += 1
            else:
                A[k] = R[j]
                B[k] = BR[j]
                Book.Book_info[k]= BookR[j]
                j += 1
            k += 1
        elif order == "Des":
            if L[i] <= R[j]:
                A[k] = R[j]
                B[k] = BR[j]
                Book.Book_info[k]= BookR[j]
                j += 1
            else:
                A[k] = L[i]
                B[k] = BL[i]
                Book.Book_info[k]=  BookL[i]
                i += 1
            k += 1
    while i < n1:
        A[k] = L[i]
        B[k] = BL[i]
        Book.Book_info[k]=  BookL[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        B[k] = BR[j]
        Book.Book_info[k]=  BookR[j]
        j += 1
        k += 1
            
# function for sorting array using merge sorting algorithm
def MultiMergeSort(A, B, p, r, order):
    if p < r:
        q = int((p+r)/2)
        
        MultiMergeSort(A, B, p, q, order)
        MultiMergeSort(A, B, q+1, r, order)
        MultiMerge(A, B, p, q, r, order)


def sameUntil(array, start):
    end = start
    key = array[start]
    for i in range(start +1 , len(array)):
        if array[i] == key:
            end += 1
        else:
            break
    return end


def MultiLevelSorting(arr1, arr2, order):
    start = 0
    end = len(arr1)

    MultiMergeSort(arr1, arr2, start, end-1, order)
    print(arr1)
    print(arr2)
    while start != end:
        p = start
        q = sameUntil(arr1, start)
        
        if p != q:
            print(p, "  ",q)
            MultiMergeSort(arr2,arr1, p, q, order)
        start = q + 1