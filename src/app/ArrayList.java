package app;

@SuppressWarnings("unchecked")
public class ArrayList<T>
{
    private T[] array;
    private int index=-1,expand=5;
    public ArrayList()
    {
        array=(T[])new Object[expand];
    }
    private void expand()
    {
        if(array.length-1==index)
        {
            T[] tmp=(T[])new Object[expand+array.length];
            for(int i=0;i<array.length;i++)
                tmp[i]=array[i];
            array=tmp;
        }
    }
    public void add(T t)
    {
        expand();
        array[++index]=t;
    }
    public void add(T t,int index)
    {
        expand();
        for(int i=this.index+1;i>=index;i--)
            array[i]=array[i-1];
        array[index]=t;
        this.index++;
    }
    public void update(T t,int index)
    {
        array[index]=t;
    }
    public T get(int index)
    {
        return array[index];
    }
    public void delete(int index)
    {
        for (int i=index;i<this.index;i++)
            array[i]=array[i+1];
        array[this.index]=null;
    }
}