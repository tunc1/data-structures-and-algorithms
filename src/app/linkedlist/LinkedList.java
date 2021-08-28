package app.linkedlist;

public class LinkedList<T>
{
    private Node<T> head,tail;
    public void add(T t)
    {
        Node<T> node=new Node<>(t);
        if(head==null)
        {
            head=node;
            tail=node;
        }
        else if(head==tail)
        {
            tail=node;
            head.setNext(tail);
        }
        else
        {
            tail.setNext(node);
            tail=node;
        }
    }
    public void add(T t,int index)
    {
        Node<T> node=new Node<>(t);
        if(index==0)
        {
            node.setNext(head);
            head=node;
        }
        else
        {
            Node<T> tmp=head;
            for (int i=0;i<index-1;i++)
                tmp=tmp.getNext();
            node.setNext(tmp.getNext());
            tmp.setNext(node);
        }
    }
    public void update(T t,int index)
    {
        Node<T> node=head;
        for (int i=0;i<index;i++)
            node=node.getNext();
        node.setData(t);
    }
    public T get(int index)
    {
        Node<T> node=head;
        for (int i=0;i<index;i++)
            node=node.getNext();
        return node.getData();
    }
    public void delete(int index)
    {
        if(index==0)
            head=head.getNext();
        else
        {
            Node<T> node=head;
            for (int i=0;i<index-1;i++)
                node=node.getNext();
            node.setNext(node.getNext().getNext());
        }
    }
}