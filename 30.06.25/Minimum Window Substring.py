import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = 0
        need = collections.Counter(t)
        start, end = len(s), 3 * len(s) 
        d = {}
        deq = collections.deque([])
        for i, c in enumerate(s):
            if c in need:
                deq.append(i)
                d[c] = d.get(c, 0) + 1
                if d[c] <= need[c]:
                    cnt += 1
                while deq and d[s[deq[0]]] > need[s[deq[0]]]:
                    d[s[deq.popleft()]] -= 1
                if cnt == len(t) and deq[-1] - deq[0] < end - start:
                    start, end = deq[0], deq[-1]
        return s[start:end + 1]

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        m, n = len(s), len(t)
        if m < n:
            return ans
        need = Counter(t)
        window = Counter()
        i, cnt, mi = 0, 0, inf
        for j, c in enumerate(s):
            window[c] += 1
            if need[c] >= window[c]: 
                cnt += 1
            while cnt == n:
                if j - i + 1 < mi: # in while
                    mi = j - i + 1
                    ans = s[i : j + 1]
                c = s[i]
                if need[c] >= window[c]:
                    cnt -= 1
                window[c] -= 1
                i += 1
        return ans
      
