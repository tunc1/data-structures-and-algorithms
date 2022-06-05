package app.heap;

public class MinHeap
{
    private int[] array;
    private int currentSize=0;
    public MinHeap(int capacity)
    {
        array=new int[capacity];
    }
    public void insert(int element)
    {
        if(currentSize<array.length)
        {
            array[currentSize++]=element;
            int tmpIndex=currentSize-1;
            while(true)
            {
                int parentIndex=(tmpIndex-1)/2;
                if(array[tmpIndex]<array[parentIndex])
                {
                    int tmp=array[tmpIndex];
                    array[tmpIndex]=array[parentIndex];
                    array[parentIndex]=tmp;
                }
                else
                    break;
                tmpIndex=parentIndex;
            }
        }
    }
    public int pop()
    {
        int toReturn=array[0];
        array[0]=array[--currentSize];
        array[currentSize]=0;
        int tmpIndex=0;
        boolean changed;
        do
        {
            changed=false;
            if(tmpIndex*2+2<currentSize)
            {
                int left=array[tmpIndex*2+1];
                int right=array[tmpIndex*2+2];
                if(array[tmpIndex]>left&&array[tmpIndex]>right)
                {
                    if(left<right)
                    {
                        int tmp=array[tmpIndex];
                        array[tmpIndex]=array[tmpIndex*2+1];
                        array[tmpIndex*2+1]=tmp;
                        tmpIndex=tmpIndex*2+1;
                        changed=true;
                    }
                    else
                    {
                        int tmp=array[tmpIndex];
                        array[tmpIndex]=array[tmpIndex*2+2];
                        array[tmpIndex*2+2]=tmp;
                        tmpIndex=tmpIndex*2+2;
                        changed=true;
                    }
                }
                else if(array[tmpIndex]>left)
                {
                    int tmp=array[tmpIndex];
                    array[tmpIndex]=array[tmpIndex*2+1];
                    array[tmpIndex*2+1]=tmp;
                    tmpIndex=tmpIndex*2+1;
                    changed=true;
                }
                else if(array[tmpIndex]>right)
                {
                    int tmp=array[tmpIndex];
                    array[tmpIndex]=array[tmpIndex*2+2];
                    array[tmpIndex*2+2]=tmp;
                    tmpIndex=tmpIndex*2+2;
                    changed=true;
                }
            }
            else if(tmpIndex*2+1<currentSize)
            {
                int left=array[tmpIndex*2+1];
                if(array[tmpIndex]>left)
                {
                    int tmp=array[tmpIndex];
                    array[tmpIndex]=array[tmpIndex*2+1];
                    array[tmpIndex*2+1]=tmp;
                    tmpIndex=tmpIndex*2+1;
                    changed=true;
                }
            }
        }
        while(changed);
        return toReturn;
    }
}