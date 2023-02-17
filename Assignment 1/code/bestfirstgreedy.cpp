#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int,int>>> adj(7);

void addEdge(int u, int v, int wt) {
    adj[u].push_back(make_pair(wt,v));
    //adj[v].push_back(make_pair(wt,u));
}

void do_bestfirstsearch(int s, int key, int n) {
    vector<bool> visited(n, false);
    priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    // Initialising source to 0
    pq.push(make_pair(0,s));
    visited[s] = true;
    while (!pq.empty())
    {
        /* code */
        int x = pq.top().second;
        cout << x << " ";
        pq.pop();

        if(x == key) {
            break;
        }
        for(int i = 0; i < adj[x].size(); i++) {    
            if(visited[adj[x][i].second] == false) {     // visiting a particular neighbor of top node x
                visited[adj[x][i].second] = true;
                //cout << adj[x][i].second << " ";
                pq.push(make_pair(adj[x][i].first, adj[x][i].second));  // adding that neighbour to pq
            }
        }
    }
}

int main() {
    int V = 7;
   // adj list is basically an array of vectors, each vector is made of pairs
    
    addEdge(0, 1, 5);
    addEdge(0, 3, 3);
    addEdge(1, 2, 1);
    addEdge(2, 4, 6);
    addEdge(2, 6, 8);
    addEdge(3, 5, 2);
    addEdge(3, 4, 2);
    addEdge(4, 1, 4);
    addEdge(5, 6, 3);
    addEdge(6, 4, 4);
    //cout << adj[4].size() << endl;
    do_bestfirstsearch(0, 6, V);
    return 0;
}