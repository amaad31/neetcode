class DynamicArray {
    int cap;
    int* arr;
    int idx;
public:
    DynamicArray(int capacity) {
        cap = capacity;
        arr = new int[capacity];
        idx = 0;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (idx == cap){
            resize();
        }
        arr[idx] = n;
        idx += 1;
    }

    int popback() {
        if (idx > 0){
            idx -= 1;
        }
        return arr[idx];
    }

    void resize() {
        int* newArr = new int[cap * 2];
        for (int i = 0; i < cap; i++){
            newArr[i] = arr[i];
        }
        delete [] arr;
        cap = cap * 2;
        arr = newArr;
    }

    int getSize() {
        return idx;
    }

    int getCapacity() {
        return cap;
    }
    ~DynamicArray() {
        delete[] arr;
    }
};
