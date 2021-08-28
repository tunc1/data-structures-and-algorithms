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
    private class Node<T extends Comparable<T>>
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
}