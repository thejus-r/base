#include <list>
#include <unordered_map>
#include <utility>

using namespace std;

class LRUCache {
    int capacity;
    list<pair<int, int>> List;

    unordered_map<int, list<pair<int, int>>::iterator> cacheMap;

    LRUCache(int capacity) {
        this->capacity = capacity;
    }

    int get(int key) {
        auto it = cacheMap.find(key);

        if (it == cacheMap.end()) {
            return -1;
        }

        int value = it->second->second;
        List.erase(it->second);
        List.push_front({key, value});

        cacheMap[key] = List.begin();
        return value;
    }

    void push(int key, int value) {
        auto it = cacheMap.find(key);

        // exists already
        if (it != cacheMap.end()) {
            // removed from list
            List.erase(it->second);
            cacheMap.erase(it);
        }

        List.push_front({key, value});
        cacheMap[key] = List.begin();

        if (cacheMap.size() > capacity) {
            auto lastNode = List.back().first;
            List.pop_back();
            cacheMap.erase(lastNode);
        }

    }
};
