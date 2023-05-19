import time
import pandas as pd
import Data
from collections import defaultdict

def to_multimap(arr):
    multimap = defaultdict(list)
    for obj in arr:
        multimap[obj.FullName].append(obj)
    return multimap

def multimap_search(multimap, key):
    # f = open('times.txt', 'a')
    # start_time = time.time()
    result = multimap.get(key)
    if result:
        # print("       %s seconds       " % (time.time() - start_time))
        # note = ' time = ' + str(time.time() - start_time) + ' !! MULTIMAP !!' + '\n'
        # f.write(note)
        # f.close()
        return result
    else:
        # print("       %s seconds       " % (time.time() - start_time))
        # note = ' time = ' + str(time.time() - start_time) + ' !! MULTIMAP !!' + '\n'
        # f.write(note)
        # f.close()
        return None


def to_excel_file(arr, file_name: str):
    df = pd.DataFrame(data = data_array(arr), columns = ['Date', 'Flight', 'Full Name', 'Place'])
    file_name = file_name + '.xlsx'
    writer = pd.ExcelWriter(file_name, engine ='xlsxwriter')
    df.to_excel(writer, 'flight_table1')
    writer.close()

def from_excel_file(file_name: str):
    xl = pd.ExcelFile(file_name)
    df = xl.parse('flight_table1')
    arr = []
    for i in range(len(df)):
        row = df.iloc[i]
        data = Data.Data(row[1].to_pydatetime(), int(row[2]), str(row[3]), int(row[4]))
        arr.append(data)
    return arr

def data_array(array):
    arr = []
    for i in range(len(array)):
        arr2 = []
        arr2.append(array[i].Date)
        arr2.append(array[i].Flight)
        arr2.append(array[i].FullName)
        arr2.append(array[i].Place)
        arr.append(arr2)
    return arr

def heapify(heap, index, size):
    l = 2 * index + 1
    r = 2 * index + 2
    if (l < size and heap[l] > heap[index]):
        largest = l
    else:
        largest = index
    if (r < size and heap[r] > heap[largest]):
        largest = r
    if (largest != index):
        heap[largest], heap[index] = heap[index], heap[largest]
        heapify(heap, largest, size)


def heap_sort(data_file: str):
    array = from_excel_file(data_file)
    length = len(array)
    beginning = (length - 2) // 2
    while beginning >= 0:
        heapify(array, index = beginning, size = length)
        beginning = beginning - 1
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, index=0, size=i)
    note2 = data_file.rsplit(".", 1)[0] + '_heap_sorted'
    to_excel_file(array, note2)

def linear_search(data_file: str, text_file: str, key):
    f = open(text_file, 'a')
    array = from_excel_file(data_file)
    start_time = time.time()
    for obj in array:
        if not isinstance(obj.FullName, int):  # Проверка, что поле FullName является не числовым
            if obj.FullName == key:
                note = data_file + ' time = ' + str(time.time() - start_time) + ' !! LINEAR SEARCH !!' + '\n'
                f.write(note)
                f.close()
                return obj
    return None

def binary_search(data_file: str, text_file: str, key):
    f = open(text_file, 'a')
    array = from_excel_file(data_file)
    start_time = time.time()
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if not isinstance(array[mid].FullName, int):  # Проверка, что поле FullName является не числовым
            if array[mid].FullName == key:
                note = data_file + ' time = ' + str(time.time() - start_time) + ' !! BINARY SEARCH !!' + '\n'
                f.write(note)
                f.close()
                return array[mid]
            elif array[mid].FullName < key:
                left = mid + 1
            else:
                right = mid - 1
        else:
            left = mid + 1
    return None

key = "Ekaterina Nikitichna Poloznova"
array = from_excel_file('flight_info_100.xlsx')
multimap = to_multimap(array)

result_multimap = multimap_search(multimap, key)
result_linear = linear_search('flight_info_100.xlsx', 'times.txt', key)
heap_sort('flight_info_100.xlsx')
result_binary = binary_search('flight_info_100_heap_sorted.xlsx', 'times.txt', key)

if result_multimap:
    print("Найденный объект данных (multimap):", result_multimap)
else:
    print("Объект данных не найден (multimap)")

if result_linear:
    print("Найденный объект данных (прямой поиск):", result_linear)
else:
    print("Объект данных не найден (прямой поиск)")

if result_binary:
    print("Найденный объект данных (бинарный поиск):", result_binary)
else:
    print("Объект данных не найден (бинарный поиск)")


key = "Eduard Petrovich Chepelov"
array = from_excel_file('flight_info_500.xlsx')
multimap = to_multimap(array)

result_multimap = multimap_search(multimap, key)
result_linear = linear_search('flight_info_500.xlsx', 'times.txt', key)
heap_sort('flight_info_500.xlsx')
result_binary = binary_search('flight_info_500_heap_sorted.xlsx', 'times.txt', key)

if result_multimap:
    print("Найденный объект данных (multimap):", result_multimap)
else:
    print("Объект данных не найден (multimap)")

if result_linear:
    print("Найденный объект данных (прямой поиск):", result_linear)
else:
    print("Объект данных не найден (прямой поиск)")

if result_binary:
    print("Найденный объект данных (бинарный поиск):", result_binary)
else:
    print("Объект данных не найден (бинарный поиск)")


key = 'Kseniya Alekseevna Ryashentseva'
array = from_excel_file('flight_info_1000.xlsx')
multimap = to_multimap(array)

result_multimap = multimap_search(multimap, key)
result_linear = linear_search('flight_info_1000.xlsx', 'times.txt', key)
heap_sort('flight_info_1000.xlsx')
result_binary = binary_search('flight_info_1000_heap_sorted.xlsx', 'times.txt', key)

if result_multimap:
    print("Найденный объект данных (multimap):", result_multimap)
else:
    print("Объект данных не найден (multimap)")

if result_linear:
    print("Найденный объект данных (прямой поиск):", result_linear)
else:
    print("Объект данных не найден (прямой поиск)")

if result_binary:
    print("Найденный объект данных (бинарный поиск):", result_binary)
else:
    print("Объект данных не найден (бинарный поиск)")


key = 'Oksana Valerevna Solomashina'
array = from_excel_file('flight_info_2500.xlsx')
multimap = to_multimap(array)

result_multimap = multimap_search(multimap, key)
result_linear = linear_search('flight_info_2500.xlsx', 'times.txt', key)
heap_sort('flight_info_2500.xlsx')
result_binary = binary_search('flight_info_2500_heap_sorted.xlsx', 'times.txt', key)

if result_multimap:
    print("Найденный объект данных (multimap):", result_multimap)
else:
    print("Объект данных не найден (multimap)")

if result_linear:
    print("Найденный объект данных (прямой поиск):", result_linear)
else:
    print("Объект данных не найден (прямой поиск)")

if result_binary:
    print("Найденный объект данных (бинарный поиск):", result_binary)
else:
    print("Объект данных не найден (бинарный поиск)")


key = 'Vitaliy Nikolaevich Evgin'
array = from_excel_file('flight_info_5000.xlsx')
multimap = to_multimap(array)

result_multimap = multimap_search(multimap, key)
result_linear = linear_search('flight_info_5000.xlsx', 'times.txt', key)
heap_sort('flight_info_5000.xlsx')
result_binary = binary_search('flight_info_5000_heap_sorted.xlsx', 'times.txt', key)

if result_multimap:
    print("Найденный объект данных (multimap):", result_multimap)
else:
    print("Объект данных не найден (multimap)")

if result_linear:
    print("Найденный объект данных (прямой поиск):", result_linear)
else:
    print("Объект данных не найден (прямой поиск)")

if result_binary:
    print("Найденный объект данных (бинарный поиск):", result_binary)
else:
    print("Объект данных не найден (бинарный поиск)")


key = "Gerasim Fedorovich Tanaylov"
array = from_excel_file('flight_info_7500.xlsx')
multimap = to_multimap(array)

result_multimap = multimap_search(multimap, key)
result_linear = linear_search('flight_info_7500.xlsx', 'times.txt', key)
heap_sort('flight_info_7500.xlsx')
result_binary = binary_search('flight_info_7500_heap_sorted.xlsx', 'times.txt', key)

if result_multimap:
    print("Найденный объект данных (multimap):", result_multimap)
else:
    print("Объект данных не найден (multimap)")

if result_linear:
    print("Найденный объект данных (прямой поиск):", result_linear)
else:
    print("Объект данных не найден (прямой поиск)")

if result_binary:
    print("Найденный объект данных (бинарный поиск):", result_binary)
else:
    print("Объект данных не найден (бинарный поиск)")



key = "Yliya Olegovna Evgina"
array = from_excel_file('flight_info_10000.xlsx')
multimap = to_multimap(array)

result_multimap = multimap_search(multimap, key)
result_linear = linear_search('flight_info_10000.xlsx', 'times.txt', key)
heap_sort('flight_info_10000.xlsx')
result_binary = binary_search('flight_info_10000_heap_sorted.xlsx', 'times.txt', key)

if result_multimap:
    print("Найденный объект данных (multimap):", result_multimap)
else:
    print("Объект данных не найден (multimap)")

if result_linear:
    print("Найденный объект данных (прямой поиск):", result_linear)
else:
    print("Объект данных не найден (прямой поиск)")

if result_binary:
    print("Найденный объект данных (бинарный поиск):", result_binary)
else:
    print("Объект данных не найден (бинарный поиск)")
