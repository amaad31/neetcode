class Node {
public:
    int val;
    int key;
    Node* nxt;
    Node* prv;
    Node(): val(0), key(0), nxt(nullptr), prv(nullptr) {}
    Node(int val, int key): val(val), key(key), nxt(nullptr), prv(nullptr) {}
    Node(int val, int key, Node *nxt): val(val), key(key), nxt(nxt), prv(nullptr) {}
    Node(int val, int key, Node *nxt, Node *prv): val(val), key(key), nxt(nxt), prv(prv) {}
};

class LRUCache {
public:
    int capacity;
    int curCapacity;
    Node *front;
    Node *back;
    unordered_map<int, pair<Node*, int>> nodesMap;
    LRUCache(int capacity) : capacity(capacity){
        curCapacity = 0;
        front = new Node(0, 0, nullptr, nullptr);
        back = new Node(0, 0, nullptr, nullptr);
        front->nxt = back;
        back->prv = front;
    }
    
    int get(int key) {
        if (!nodesMap.count(key)) {
            return -1;
        }
        int res = nodesMap[key].second;
        remove(nodesMap[key].first);
        put(key, res);
        return res;
    }
    
    void remove(Node *toRemove){
        if (!(nodesMap.count(toRemove->key))){
            return;
        }
        Node* tmpNode = toRemove->nxt;
        tmpNode->prv = toRemove->prv;
        toRemove->prv->nxt = tmpNode;
        nodesMap.erase(toRemove->key);
        delete toRemove;
        curCapacity--;
    }

    void put(int key, int value) {
        if (nodesMap.count(key)) {
            remove(nodesMap[key].first);
        }
        if (curCapacity == capacity) {
            remove(front->nxt);
        }
        Node* lastNode = back->prv;
        Node* newNode = new Node(value, key, back, lastNode);
        lastNode->nxt = newNode;
        back->prv = newNode;
        curCapacity++;
        nodesMap[key] = {newNode, value};
    }
};
