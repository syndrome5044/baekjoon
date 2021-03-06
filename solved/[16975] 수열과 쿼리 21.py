"""
problem tier : Platinum 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def st_update(L, R, V, N, S, E):
    if lazy_tree[N]:
        seg_tree[N] += lazy_tree[N] * (E-S+1)
        if S != E:
            lazy_tree[N * 2] += lazy_tree[N]
            lazy_tree[N * 2 + 1] += lazy_tree[N]
        lazy_tree[N] = 0
    if S == E:
        seg_tree[N] += V
    elif L <= S and E <= R:
        seg_tree[N] += V * (E-S+1)
        lazy_tree[2 * N] += V
        lazy_tree[2 * N + 1] += V
    else:
        mid = (S + E) // 2
        if L <= mid:
            st_update(L, R, V, 2 * N, S, mid)
        if mid < R:
            st_update(L, R, V, 2 * N + 1, mid + 1, E)
        seg_tree[N] += (min(R, E) - max(L, S) + 1) * V


def st_query(L, R, N, S, E):
    if lazy_tree[N]:
        seg_tree[N] += lazy_tree[N] * (E-S+1)
        if S != E:
            lazy_tree[N * 2] += lazy_tree[N]
            lazy_tree[N * 2 + 1] += lazy_tree[N]
        lazy_tree[N] = 0
    if R < S or E < L:
        return 0
    elif L <= S and E <= R:
        return seg_tree[N]
    else:
        mid = (S + E) // 2
        return st_query(L, R, N * 2, S, mid) + st_query(L, R, N * 2 + 1, mid + 1, E)


N = int(input())
seg_tree = [0] * (N * 4)
lazy_tree = [0] * (N * 4)

arr = list(map(int, input().split()))
for i in range(N):
    st_update(i+1, i+1, arr[i], 1, 1, N)

M = int(input())
for i in range(M):
    inp = list(map(int, input().split()))
    op = inp[0]
    if op == 1:
        i, j, k = inp[1], inp[2], inp[3]
        st_update(i, j, k, 1, 1, N)
    else:
        x = inp[1]
        print(st_query(x, x, 1, 1, N))
