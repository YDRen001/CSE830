#include <iostream>
#include <unordered_set>
#include <map>
#include <ctime>
#include <vector>
using namespace std;
double measure_insert_time_hash(int n) {
    unordered_multiset<int> hash_table;
    clock_t start_time = clock();
    int random_value;
    for (int i = 0; i < n; i++) {
        random_value=rand()%n;
        hash_table.insert(i);
    }
    clock_t end_time = clock() - start_time;
    return static_cast<double>(end_time) / CLOCKS_PER_SEC;
}
double measure_insert_time_tree(int n) {
    multimap<int, int> tree;
    clock_t start_time = clock();
    int random_value;
    for (int i = 0; i < n; i++) {
        random_value=rand()%n;
        tree.insert({random_value, random_value}); 
    }
    clock_t end_time = clock() - start_time;
    return static_cast<double>(end_time) / CLOCKS_PER_SEC;
}
int main() {
    double hash_table_time=0,tree_time=0,total_time;
    int n = 1, i;
    cout << "N\ttable_hash\tbinary_tree" << endl;
    while(hash_table_time<3&&tree_time<3) {
        n *= 10;
        cout << n << "\t";
        total_time = 0;
        for (i = 0; i < 20; i++)
            total_time += measure_insert_time_hash(n);
        hash_table_time = total_time/20;
        cout << hash_table_time << "\t\t";
        total_time = 0;
        for (i = 0; i < 20; i++)
            total_time += measure_insert_time_tree(n);
        tree_time = total_time/20;
        cout << tree_time << endl;
    }
    return 0;
}
