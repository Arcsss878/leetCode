class Solution(object):
    def assignEdgeWeights(self, edges):
        # Modulo yang diminta soal
        MOD = 10**9 + 7

        # Pada tree:
        # jumlah node = jumlah edge + 1
        n = len(edges) + 1

        # Jika hanya ada 1 node:
        # Tidak ada edge yang bisa diberi bobot.
        # Cost path = 0 (genap)
        # Jadi tidak ada cara menghasilkan cost ganjil.
        if n == 1:
            return 0

        # Membuat adjacency list
        #
        # graph[i] berisi semua tetangga node i
        graph = [[] for _ in range(n + 1)]

        # Karena tree bersifat undirected,
        # masukkan kedua arah
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS untuk mencari depth maksimum
        def dfs(node, parent):

            # depth maksimum dari node ini ke bawah
            depth = 0

            # Kunjungi semua tetangga
            for nxt in graph[node]:

                # Jangan kembali ke parent
                if nxt != parent:

                    # Cari depth subtree anak
                    #
                    # dfs(nxt,node) = depth anak
                    #
                    # +1 karena bergerak satu edge
                    depth = max(depth, 1 + dfs(nxt, node))

            return depth

        # Root selalu node 1
        max_depth = dfs(1, 0)

        # Jumlah cara = 2^(k-1)
        # k = jumlah edge dari root ke node terdalam
        return pow(2, max_depth - 1, MOD)
        