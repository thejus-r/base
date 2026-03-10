
#include <mutex>
#include <string>
#include <unordered_map>
#include <shared_mutex>

using namespace std;

class KVStore {
private:
    unordered_map<string, string> store;
    mutable shared_mutex rw_lock;

public:
    void put(const string& key, const string& value) {
        unique_lock<shared_mutex> lock(rw_lock);
        store[key] = value;
    }

    string get(const string &key) {

        shared_lock<shared_mutex> lock(rw_lock);

        auto it = store.find(key);

        if (it != store.end()) {
            return it->second;
        }

        return "";
    }

    void remove(const string& key) {
        unique_lock<shared_mutex> lock(rw_lock);
        store.erase(key);
    }

    void apply_commit(const unordered_map<string, string>& draft_writes) {
        unique_lock<shared_mutex> lock(rw_lock);

        for (const auto& pair: draft_writes) {
            store[pair.first] = pair.second;
        }

    }

};

class Transaction {
    private:
    KVStore& db;
    unordered_map<string, string> draft_writes;

    public:
    Transaction(KVStore& database): db(database) {}

    void put(const string& key, const string& value) {
        draft_writes[key] = value;
    }

    string get(const string& key) {
        auto it = draft_writes.find(key);

        if (it != draft_writes.end()) {
            return it->second;
        }

        return db.get(key);
    }

    void commit() {
        if (draft_writes.empty()) return;

        db.apply_commit(draft_writes);
        draft_writes.clear();
    }

    void rollback() {
        draft_writes.clear();
    }
};
