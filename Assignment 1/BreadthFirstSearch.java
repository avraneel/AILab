import java.util.*;

class BreadthFirstSearch {
    public static void main(String[] args) {
        Graph G = new Graph();
        bfs(G);
    }

    static void bfs(Graph G, Vertex s) {

        for(int i = 0; i < G.V.size(); i++) {
            G.V.get(i).color = "white";
            G.V.get(i).pred = null;
            G.V.get(i).d = 9999;
        }

        Queue<Integer> = new PriorityQueue<>();

    }

}