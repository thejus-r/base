#include <list>
#include <unordered_map>

using namespace std;

struct Node {
    int key;
    int value;
    int frequency;
};

class LFUCache {
    int capacity;
    int minFreq;

    // Map 1: Freq -> DLL
    unordered_map<int, list<Node>> freqListMap;

    // Map 2: Key -> Iterator
    unordered_map<int, list<Node>::iterator> keyNodeMap;

    LFUCache(int capacity, int minFreq) {
        this->capacity = capacity;
        this->minFreq = minFreq;
    }

    void updateFreq(int key) {
        auto nodeIt = keyNodeMap[key];
        int val = nodeIt->value;
        int freq = nodeIt->frequency;

        freqListMap[freq].erase(nodeIt);

        if (freqListMap[freq].empty() && minFreq == freq) {
            minFreq++;
        }

        freqListMap[freq + 1].push_front({ key, val, freq + 1 });

        keyNodeMap[key] = freqListMap[freq + 1].begin();
    }

    int get(int key) {

        if (keyNodeMap.find(key) == keyNodeMap.end()) {
            return -1;
        }

        int value = keyNodeMap[key]->value;

        updateFreq(key);

        return value;
    }

    void push(int key, int value) {
        if (capacity <= 0) return;

        // key already exists
        if (keyNodeMap.find(key) != keyNodeMap.end()) {
            keyNodeMap[key]->value = value;
            updateFreq(key);

            return;
        }

        if (keyNodeMap.size() >= capacity) {
            auto evictNode = freqListMap[minFreq].back();

            keyNodeMap.erase(evictNode.key);
            freqListMap[minFreq].pop_back();
        }

        minFreq = 1;
        freqListMap[1].push_front({ key, value, 1 });
        keyNodeMap[key] = freqListMap[1].begin();
    }




};
