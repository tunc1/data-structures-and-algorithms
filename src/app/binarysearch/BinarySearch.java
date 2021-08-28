package app.binarysearch;

public class BinarySearch
{
    public int search(int[] array,int element)
    {
        return search(array, element, 0, array.length);
    }
    private int search(int[] array,int element,int start,int end)
    {
        if(end-start==1)
        {
            if(array[start]==element)
                return start;
            return -1;
        }
        int middleIndex=(start+end)/2;
        if(array[middleIndex]>element)
            return search(array, element,0,middleIndex);
        else if(array[middleIndex]>element)
            return search(array, element,middleIndex,end);
        return middleIndex;
    }
}