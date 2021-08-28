package app.hashtable;

import java.util.LinkedList;
import java.util.List;

@SuppressWarnings("unchecked")
public class HashTable<K,V>
{
    private Object[] values;
    public HashTable(int size)
    {
        values=new Object[size];
    }
    public HashTable()
    {
        this(5);
    }
    public void put(K key,V value)
    {
        KeyValue<K,V> keyValue=new KeyValue<>(key,value);
        int index=key.hashCode()%values.length;
        if(values[index]==null)
            values[index]=keyValue;
        else if(values[index] instanceof List)
        {
            List<KeyValue<K,V>> list=(List<KeyValue<K,V>>)values[index];
            list.add(keyValue);
        }
        else
        {
            List<KeyValue<K,V>> list=new LinkedList<>();
            list.add((KeyValue<K,V>)values[index]);
            list.add(keyValue);
            values[index]=list;
        }
    }
    public V get(K key)
    {
        int index=key.hashCode()%values.length;
        if(values[index] instanceof List)
        {
            List<KeyValue<K,V>> list=(List<KeyValue<K,V>>)values[index];
            for(KeyValue<K,V> keyValue: list)
            {
                if(keyValue.getKey().equals(key))
                    return keyValue.getValue();
            }
        }
        else
            return ((KeyValue<K,V>)values[index]).getValue();
        throw new IllegalArgumentException("Not Valid Key");
    }
    public void remove(K key)
    {
        int index=key.hashCode()%values.length;
        if(values[index] instanceof List)
        {
            List<KeyValue<K,V>> list=(List<KeyValue<K,V>>)values[index];
            for(KeyValue<K,V> keyValue: list)
            {
                if(keyValue.getKey().equals(key))
                {
                    list.remove(keyValue);
                    break;
                }
            }
            if(list.size()==0)
                values[index]=null;
            else if(list.size()==1)
                values[index]=list.get(0);
        }
        else if(values[index] instanceof KeyValue)
            values[index]=null;
        else
            throw new IllegalArgumentException("Not Valid Key");
    }
    public String toString()
    {
        StringBuilder a=new StringBuilder("{");
        for(Object value: values)
        {
            if(value instanceof List)
            {
                List<KeyValue<K,V>> list=(List<KeyValue<K,V>>)value;
                for(KeyValue<K,V> keyValue: list)
                {
                    a.append(keyValue);
                    a.append(",");
                }
            }
            else if(value instanceof KeyValue)
            {
                KeyValue<K,V> keyValue=(KeyValue<K,V>)value;
                a.append(keyValue);
                a.append(",");
            }
        }
        a.replace(a.length()-1,a.length(),"}");
        return a.toString();
    }
}