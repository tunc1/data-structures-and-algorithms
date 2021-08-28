package app.binarysearchtree;

public class BinarySearchTree<E extends Comparable<E>>
{
    private Node<E> root;
    public void insert(E data)
    {
        if(root==null)
            root=new Node<>(data);
        else
            root.insert(data);
    }
    public boolean search(E data)
    {
        if(root==null)
            return false;
        Node<E> tmp=root;
        while(true)
        {
            int result=data.compareTo(tmp.getData());
            if(result>0)
            {
                if(tmp.hasRight())
                    tmp=tmp.getRight();
                else
                    return false;
            }
            else if(result<0)
            {
                if(tmp.hasLeft())
                    tmp=tmp.getLeft();
                else
                    return false;
            }
            else
                return true;
        }
    }
}