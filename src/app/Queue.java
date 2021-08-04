package app;

import java.util.LinkedList;
import java.util.List;

public class Queue<T>
{
    private List<T> list;
    public Queue()
    {
        list=new LinkedList<>();
    }
    public void add(T t)
    {
        list.add(t);
    }
    public T remove()
    {
        return list.remove(0);
    }
    public T element()
    {
        return list.get(0);
    }
    public boolean isEmpty()
    {
        return list.isEmpty();
    }
}