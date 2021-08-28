package app.binarysearchtree;

public class Node<T extends Comparable<T>>
{
    private final T data;
    private Node<T> left,right;
    public Node(T data)
    {
        this.data=data;
    }
    public void insert(T data)
    {
        if(data.compareTo(this.data)>0)
        {
            if(right==null)
                right=new Node<>(data);
            else
                right.insert(data);
        }
        else
        {
            if(left==null)
                left=new Node<>(data);
            else
                left.insert(data);
        }
    }
    public T getData()
    {
        return data;
    }
    public Node<T> getLeft()
    {
        return left;
    }
    public Node<T> getRight()
    {
        return right;
    }
    public boolean hasRight()
    {
        return right!=null;
    }
    public boolean hasLeft()
    {
        return left!=null;
    }
}