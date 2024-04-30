def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def main():
    # Take input for the array
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))

    # Call selection_sort function to sort the array
    sorted_arr = selection_sort(arr)

    # Print the sorted array
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
