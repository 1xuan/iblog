class QuickSort:
    def quicksort(self, arr, p, r):
        """
        >>> lt = [2, 8, 7, 1, 3, 5, 6, 4]
        >>> QuickSort().quicksort(lt, 0, len(lt)-1)
        >>> lt
        [1, 2, 3, 4, 5, 6, 7, 8]
        """
        if p < r:
            q = self.partition(arr, p, r)
            self.quicksort(arr, p, q-1)
            self.quicksort(arr, q+1, r)

    def partition(self, arr, p, r):
        x = arr[r]
        i = p - 1
        for j in range(p, r):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[r] = arr[r], arr[i+1]

        return i+1


class LinearSort:
    def countsort(self, arr, k):
        """
        >>> lt = [2, 8, 7, 1, 3, 5, 6, 4]
        >>> LinearSort().countsort(lt, 9)
        [1, 2, 3, 4, 5, 6, 7, 8]
        """
        n = len(arr)
        res = [None] * n
        temp = [0] * k
        for e in arr:
            temp[e] += 1
        for i in range(1, k):
            temp[i] += temp[i-1]
        for e in arr:
            res[temp[e]-1] = e
            temp[e] -= 1
        return res


