def bubbleSort(bubbleSortArr):
    n = len(bubbleSortArr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if bubbleSortArr[j] > bubbleSortArr[j + 1]:
                bubbleSortArr[j], bubbleSortArr[j +
                                                1] = bubbleSortArr[j + 1], bubbleSortArr[j]
