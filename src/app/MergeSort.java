package app;

public class MergeSort
{
    public static void sort(int[] array)
    {
        sort(array,0,array.length);
    }
    private static void sort(int[] array,int start,int end)
    {
        int middle=(end+start)/2;
        if(end-start>1)
        {
            sort(array,start,middle);
            sort(array,middle,end);
        }
        int[] tmp=new int[end-start];
        int leftIndex=start,rightIndex=middle,tmpIndex=0;
        while(leftIndex<middle&&rightIndex<end)
        {
            Integer left=array[leftIndex];
            Integer right=array[rightIndex];
            if(left.compareTo(right)==-1)
            {
                tmp[tmpIndex++]=left;
                leftIndex++;
            }
            else
            {
                tmp[tmpIndex++]=right;
                rightIndex++;
            }
        }
        while(leftIndex<middle)
            tmp[tmpIndex++]=array[leftIndex++];
        while(rightIndex<end)
            tmp[tmpIndex++]=array[rightIndex++];
        for(int i=start;i<end;i++)
            array[i]=tmp[i-start];
    }
}