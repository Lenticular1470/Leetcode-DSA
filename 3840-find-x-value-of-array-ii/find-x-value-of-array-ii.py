class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        tree = [(1, [0] * k) for _ in range(4*n)] 

        def merge(a, b):
            prod1, cnt1 = a
            prod2, cnt2 = b

            prod = (prod1 * prod2) % k

            cnt = cnt1[:]

            for r in range(k):
                cnt[(prod1 * r) % k] += cnt2[r]
            return prod, cnt
        
        def build(node, l, r):
            if l == r:
                val = nums[l] % k
                cnt = [0] * k
                cnt[val] = 1
                tree[node] = (val, cnt)
                return 

            mid = (l+r) // 2

            build(node*2, l, mid)
            build(node*2+1, mid+1, r)

            tree[node] = merge(tree[node*2], tree[node*2+1])
        def update(node, l, r, idx, val):
            if l==r:
                val %= k
                cnt = [0]*k
                cnt[val] = 1
                tree[node] = (val, cnt)
                return
            mid = (l+r) //2

            if idx <= mid:
                update(node *2, l, mid, idx, val)
            else:
                update(node*2+1, mid+1, r, idx, val)
            tree[node] = merge(tree[node*2], tree[node*2+1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l+r) // 2

            if qr <= mid:
                return query(node*2, l, mid, ql, qr)
            if ql > mid:
                return query(node*2+1, mid+1, r, ql, qr)
            left = query(node*2, l, mid, ql, qr)
            right = query(node*2+1, mid+1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n-1)
        ans = []
        for idx, val, strt, x in queries:
            update(1, 0, n-1, idx, val)

            _, cnt = query(1, 0, n-1, strt, n-1)
            ans.append(cnt[x])
        return ans

        