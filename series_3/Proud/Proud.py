

def mergeSort(arr, sorted_arr, left, right):
	count = 0

	if (left < right):
		count = mergeSort(arr, sorted_arr, left, ((right + left) // 2))
		count += mergeSort(arr, sorted_arr, ((right + left) // 2)+1, right)
		count += merge(arr, sorted_arr, left, ((right + left) // 2)+1, right)

	return count


def merge(arr, sorted_arr, left, mid, right):
	count = 0

	i = left
	k = left
	j = mid
	while i <= mid-1 and j <= right:
		if (2*arr[j] < arr[i]):
			j += 1
			count += mid - i
		else:
			i += 1

	i = left
	k = left
	j = mid
	while i <= mid-1 and j <= right:
		if (arr[i] <= arr[j]):
			sorted_arr[k] = arr[i]
			i, k = i+1, k+1
		else:
			sorted_arr[k] = arr[j]
			k, j = k+1, j+1

	while i <= mid-1:
		sorted_arr[k] = arr[i]
		i, k = i+1, k+1

	while j <= right:
		sorted_arr[k] = arr[j]
		j, k = j+1, k+1


	for i in range(left, right + 1):
		arr[i] = sorted_arr[i]


	return count
        






if __name__ == '__main__':

	n = int(input())
	arr = [int(x) for x in input().split()]

	sorted_arr = [0] * n
	print(mergeSort(arr, sorted_arr, 0, n-1))



