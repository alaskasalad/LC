
class Sol:
    def combine(self, arr1, arr2):
        i = j = 0
        ans = []
        while (i < len(arr1) and j < len(arr2)):
            if (arr1[i] < arr2[j]):
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

        while (i < len(arr1)):
            ans.append(arr1[i])
            i += 1

        while (j < len(arr2)):
            ans.append(arr2[j])
            j += 1

        print(ans)
        
array1 = [1, 4, 7, 20] 
array2 = [3, 5, 6]

a = Sol()
a.combine(array1, array2)

