//package code;
import java.util.*;

class Vertex {
    int val;
    Vertex pred;        // parent node
    boolean isVisited;

    Vertex(int val, Vertex pred) {
        this.val = val;
        this.pred = pred;
    }

}

class GraphDFS {
    int V;              // no of vertices
    List<Vertex> adj[];
    boolean flag = false;

    GraphDFS(int V) {
        this.V = V;
        adj = new ArrayList[V];
        for(int i = 0; i < V; i++) {
            adj[i] = new ArrayList<>();
        }
    }

    public static void main(String[] args) {
        GraphDFS g = new GraphDFS(11);

        Vertex v1 = new Vertex(1, null);
        Vertex v2 = new Vertex(2, v1);
        Vertex v8 = new Vertex(8, v1);
        Vertex v5 = new Vertex(5, v1);
        Vertex v3 = new Vertex(3, v8);
        Vertex v4 = new Vertex(4, v8);
        Vertex v6 = new Vertex(6, v8);
        Vertex v7 = new Vertex(7, v6);
        Vertex v9 = new Vertex(9, v2);
        Vertex v10 = new Vertex(10, v6);

        g.addToVertex(v1, v8);
        g.addToVertex(v1, v5);
        g.addToVertex(v1, v2);

        g.addToVertex(v8, v6);
        g.addToVertex(v8, v4);
        g.addToVertex(v8, v3);

        g.addToVertex(v6, v7);
        g.addToVertex(v6, v10);
        

        g.addToVertex(v2, v9);

        g.dfs(v1, v3);

    }

    // connects a vertex to another vertex by adding it to the adjacency list of that vertex
    void addToVertex(Vertex v, Vertex w) {
        adj[v.val].add(w);
    }
    
    
    void dfs(Vertex s, Vertex key) {
        if(flag == true)
            return;
        s.isVisited = true;
        if(s.val == key.val) {
            System.out.println("Goal found: " + s.val);
            Vertex temp = s;
            System.out.println("Path: ");
                while(temp.pred != null) {
                    System.out.print(temp.val+"<-");
                    temp = temp.pred;
                }
                System.out.println(temp.val);
                flag = true;
                return;
        }
        System.out.print(s.val+"->");
        Iterator<Vertex> it = adj[s.val].listIterator();
        while(it.hasNext()) {
            Vertex n = it.next();
            if(n.isVisited == false) {
                dfs(n,key);
            }
        }
    }
}