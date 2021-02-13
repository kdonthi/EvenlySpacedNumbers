class listplusN {
	public int[]	list;
	public int	mse;
}

class Array {
	public static int[] slices(int[] array, int si, int ei) { 
		//Returns the element in array1 from indices si to ei, inclusive.
		int newarraylen = (ei - si) + 1;
		int newarray[] = new int[newarraylen];
		int counter = 0;
		for (int i = si; i <= ei; i++) {
			newarray[counter++] = array[i];
		}
		return (newarray);
	}
	public static int[] concat(int[] array1, int[] array2) {
		int newarraylen = array1.length + array2.length;
		int newarray[] = new int[newarraylen];
		int index = 0;
		for (int i = 0; i < array1.length; i++)
		{
			newarray[index++] = array1[i];
		}
		for (int i = 0; i < array2.length; i++)
		{
			newarray[index++] = array2[i];
		}
		return newarray;
	}
	public static void printarray(int[] array) {
		for (int i = 0; i < array.length; i++)
		{
			System.out.printf("%d ",array[i]);
		}
		System.out.println();
	}
	public static int[] arrcpy(int[] src)
	{
		int newarray[] = new int[src.length];
		for (int i = 0; i < src.length; i++)
			newarray[i] = src[i];
		return (newarray);
	}
	public static int straighttoend(int[] array, int lastindex) {
		int i = array[0];
		int index = 0;
		while(index <= lastindex) {
			if (i++ != array[index++])
				return (0);
		}
		return (1);
	}	
}
public class optimalSubsample {
	public static int square(int number) {
		return (number * number);
	}
	public static int mse(int[] ia, int optimaldiff, int[] original) {
		int error = 0;
		//Array.printarray(original);
		for (int i = 0; i < (ia.length - 1); i++)
		{ 
			//System.out.println(i);
			error += square(original[ia[i + 1]] - original[ia[i]]) - optimaldiff;
		}
		return (error);
	}
	public static listplusN recur(int[] list, int N, int[] original, int optimaldiff, listplusN[][] indbyN) {
		listplusN obj = new listplusN();
		int[] rtrnarray;
		int length = list.length;
		/*
		if (list.length < N || N < 2) { //if the list can no longer achieve N number
			obj.list = null;
			obj.mse = -1;
			return (obj);
		} */
		if (N == 2) //if we only have to choose two numbers, just choose begin and end
		{
			rtrnarray = new int[2];
			rtrnarray[0] = list[0];
			rtrnarray[1] = list[length - 1];
			obj.list = rtrnarray;
			//Array.printarray(rtrnarray);
			obj.mse  = mse(rtrnarray, optimaldiff, original);;
			return (obj);
		}
		else if (list.length == N) { //if N == length of the list, return the whole list
			obj.list = Array.arrcpy(list);
			obj.mse = mse(list, optimaldiff, original);
			return (obj);
		}
		else if (Array.straighttoend(list, list.length - 1) == 1) {
			if (indbyN[list[0]][N-1] != null) {
				return (indbyN[list[0]][N-1]);
			}
		}

		//When including a number, it is the same as recur({0, list[1]}, 2) + recur({list[1] -> list[len-1], 2})
		listplusN rtrn1a = recur(Array.slices(list, 0, 1), 2,  original, optimaldiff, indbyN);
		listplusN rtrn1b = recur(Array.slices(list, 1, list.length - 1), N - 1, original, optimaldiff, indbyN);
		int[] removedindex = Array.concat(Array.slices(list, 0, 0), Array.slices(list, 2, list.length - 1)); //removing the number at first index
		listplusN rtrn2 = recur(removedindex, N, original, optimaldiff, indbyN);
		int firstindex = 0;
		int[] rtrn1bfirstrem;
		int[] conc;

		if (rtrn1a.mse == -1 || rtrn1b.mse == -1)
			return (rtrn2);
		else if (rtrn2.mse == -1)
			return (rtrn1a);
		else if (rtrn1a.mse + rtrn1b.mse < rtrn2.mse) {
				rtrn1bfirstrem = Array.slices(rtrn1b.list, 1, (rtrn1b.list).length - 1);
				obj.list = Array.concat(rtrn1a.list, rtrn1bfirstrem);
				obj.mse = rtrn1a.mse + rtrn1b.mse;
				if (Array.straighttoend(list, list.length - 1) == 1 && indbyN[list[0]][N-1] == null)
						indbyN[list[0]][N-1] = obj;
				
		}
		else if (rtrn1a.mse + rtrn1b.mse >= rtrn2.mse) {
			obj.list = Array.arrcpy(rtrn2.list);
			obj.mse = rtrn2.mse;
			if (Array.straighttoend(list, list.length - 1) == 1 && indbyN[list[0]][N-1] == null)
				indbyN[list[0]][N-1] = obj;
		}
		return (obj);
			
	}

	public static int[] opSub(int[] array, int N) {
		int optimaldiff = (array[array.length - 1] - array[0]) / (N-1);
		listplusN[][] indexbyN = new listplusN[array.length][N];
		int[] indexarray = new int[array.length];
		for (int i = 0; i < array.length; i++)
			indexarray[i] = i;
		listplusN[][] arrayindexbyN = new listplusN[array.length][N];
		int[] finalia = recur(indexarray, N, array, optimaldiff, arrayindexbyN).list;
		int[] returnlist = new int[finalia.length];
		for (int i = 0; i < finalia.length; i++)
		{
			returnlist[i] = array[finalia[i]]; //converting indexes into numbers
		}

		return (returnlist);
	}

	public static void main (String[] args) {
		int array1[] = new int[100];
		int array2[] = {0,33,50,66,100};
		int array3[] = {0,1,2,3,4,100};
		System.out.println(Array.straighttoend(array2, 3));
		System.out.println(Array.straighttoend(array3, 5));

		for (int i = 0; i < 100; i++)
		{
			array1[i] = i;
		}
		Array.printarray(opSub(array1, 10));
		Array.printarray(opSub(array2, 4));
		
	}
}


