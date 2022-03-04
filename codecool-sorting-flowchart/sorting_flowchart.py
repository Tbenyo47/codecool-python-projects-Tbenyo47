my_list = [1, 2, 56, 32, 51, 2, 8, 92, 15]

def bubbleSort(array):
    
  # végig menni a listán
  for i in range(len(array)):

    # Összehasonlítani a lista elemeit
    for j in range(0, len(array) - i - 1):

      
      if array[j] > array[j + 1]:
        change_array = array[j]
        array[j] = array[j+1]
        array[j+1] = change_array


my_list = [1, 2, 56, 32, 51, 2, 8, 92, 15]

bubbleSort(my_list)

print('Sorted Array in Ascending Order:')
print(my_list)