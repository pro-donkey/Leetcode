class Solution {

    private void dfs(int node, boolean[] vis, ArrayList<ArrayList<Integer>> adjLs) {

        vis[node] = true;

        for (Integer it : adjLs.get(node)) {

            if (!vis[it]) {
                dfs(it, vis, adjLs);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {

        int V = isConnected.length;
        ArrayList<ArrayList<Integer>> adjLs = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < V; i++) {
            adjLs.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (isConnected[i][j] == 1 && i != j) {
                    adjLs.get(i).add(j);
                    adjLs.get(j).add(i);
                }
            }
        }

        boolean[] vis = new boolean[V];
        int cnt = 0;
        for (int i = 0; i < V; i++) {
            if (!vis[i]) {
                cnt += 1;
                dfs(i, vis, adjLs);
            }
        }

        return cnt;
    }
}
