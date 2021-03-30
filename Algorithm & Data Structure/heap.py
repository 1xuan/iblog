class Heap:
    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2 * (i+1)

    def max_heapify(self, arr, i):
        """ MAX HEAP

        O(lgn)
        Heapify a specific element indexed i inside arr

        >>> arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        >>> self.max_heapify(arr, 1)
        >>> arr
        [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        """
        l = self.left(i)
        r = self.right(i)

        largest = i

        if l < len(arr) and arr[l] > arr[i]:
            largest = l
        
        if r < len(arr) and arr[r] > arr[largest]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, largest)

    def build_max_heap(self, arr):
        """
        O(n)

        >>> arr = [10, 1, 16, 3, 7, 2, 8, 4, 14, 9]
        >>> Heap().build_max_heap(arr)
        >>> arr
        [16, 14, 10, 4, 9, 2, 8, 1, 3, 7]
        """
        length = len(arr)
        for i in range(length-1, -1, -1):
            self.max_heapify(arr, i)


    def heapsort(self, arr):
        """
        O(nlgn)

        >>> arr = [10, 1, 16, 3, 7, 2, 8, 4, 14, 9]
        >>> Heap().heapsort(arr)
        >>> arr
        [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
        """
        self.build_max_heap(arr)
        for i in range(len(arr)-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self._max_heapify(arr, 0, i)

    def _max_heapify(self, arr, i, length):
        """ MAX HEAP
        Add one arguments length of arr in order to change heapsort arr size
        """
        l = self.left(i)
        r = self.right(i)

        largest = i

        if l < length and arr[l] > arr[i]:
            largest = l
        
        if r < length and arr[r] > arr[largest]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._max_heapify(arr, largest, length)

