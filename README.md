# Evenly-Spaced-Numbers

This code finds an evenly spaced set of N numbers from a larger set in O(n^2). I do this by going through each number in a list, and shifting it right or left to minimize its MSE of its distances to its right or left with the "optimal distance", which is the (end - beginning) / (N - 1).

Like K-means, this can get stuck in local minima, so I use reinitializations to try to find the global minima. I have 100% accuracy on 20,000 samples, using a less efficient recursive tree method going through possibilities of the list as "base truth".

Run ```python3 main.py``` with all the files in your directory to run the stress test, or run ```OptimalSubsampleNew.py``` and insert your own test case in the format:

like ```print(optimalSubsample(list(range(100)),10))```
or ```print(optimalSubsample([1,2,3,4,5],3)```.

Make sure the second parameter (an integer), "N", is <= to the length of your first parameter (a list) and >= 2 (the first and last number of the list provided are always in the resulting list.)

UDPATE: I have created an accurate solution and fast solution in Java using dynamic programming by storing the values of lists that are continuous from any index to the last index in an array. <br/>

You can run this solution by compiling using ```javac optimalSubsample.java``` and then ```java optimalSubsample```. You can adjust the arrays given and the numbers to choose for each array. <br/>

E.g. change the numbers in an array ```int array1[] = {0, 33, 50, 66, 100};``` and then run ```Array.printarray(optimalSubsample(array1, 4));``` (for N = 4). 
