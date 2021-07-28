package app;

@SuppressWarnings("unchecked")
public class Stack<T>
{
    private T[] objects;
    private int index=-1;
    public Stack(int size)
    {
        objects=(T[])new Object[size];
    }
    public void push(T t)
    {
        if(index<objects.length-1)
            objects[++index]=t;
        else
            throw new RuntimeException("Stack is full!");
    }
    public T peek()
    {
        if(isEmpty())
            throw new RuntimeException("Stack is empty!");
        return objects[index];
    }
    public T pop()
    {
        T t=peek();
        index--;
        return t;
    }
    public boolean isEmpty()
    {
        return index==-1;
    }
}