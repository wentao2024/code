class LRUCache {
    class Node{
        int key;
        int val;
        Node prev;
        Node next;

        Node(int key, int val){
            this.key = key;
            this.val = val;
        }

    }
    Node head = new Node(-1,-1);
    Node tail = new Node(-1,-1);
    int cap;
    Map<Integer, Node> m = new HashMap<>();


    public LRUCache(int capacity) {
        cap= capacity;
        head.next = tail;
        tail.pre = head;
    }
    
    public int get(int key) {
        if (m.containsKey(key)){
            Node resNode = m.get(key);
            int ans = resNode.val;
            m.remove(key);
            deleteNode(resNode);
            addNode(resNode);
            m.put(key, head.next);
            return ans;
        }
        if(m.containsKey(key)){
            Node resNode = m.get(key);
            int ans = resNode.val;
            m.remove(key);
            deleteNode(resNode);
            addNode(resNode);
            m.put(key, head.next);
            return ans
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if(m.containsKey(key)){
            Node curr = m.get(key);
            m.remove(key);
            deleteNode(curr);

        }
        if(m.size()==cap){
            m.remove(tail.pre.key);
            deletNode(tail.pre);

        }
        addNode(new Node(key, value));
        m.put(key,head.next);

        
    }
    private void addNode(Node addnode){
        Node tep = head.next;
        addnode.next = tep;
        addnode.pre = head;
        head.next = addnode;
        tep.pre = addnode;
        
    }

    private void deleteNode(Node delnode){
        Node pre = delnode.pre;
        Ndoe next = delnode.next;
        pre.next = next;
        next.pre = pre;
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
