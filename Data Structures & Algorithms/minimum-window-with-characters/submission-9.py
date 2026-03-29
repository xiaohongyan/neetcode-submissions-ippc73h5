class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        if len(t)>len(s):
            return ""

        l = 0
        res = "" # index l...r+1, substring
        countT = {}
        window = {}



        # 1. 预处理：使用 dict 的子类 Counter 或手动构建
        for c in t:
            countT[c] =  countT.get(c, 0) + 1
        need = len(countT)
       
        # 2. 优化：只记录索引，避免频繁切片
        min_len = float("inf")
        str_range = [-1, -1]

        have = 0
        for r in range(len(s)):
            c = s[r]

            # 只有在 t 中的字符才进 window
            if c in countT:
                window[c] =  window.get(c, 0) + 1

                if window[c] == countT[c]: # found the valid window, not if window[c] >= countT[c], 只在第一上次相等是have ++, 否则have会偏大
                    have += 1

            while have == need:
                if r - l + 1 <  min_len:
                    str_range = [l, r]
                    min_len = r - l + 1
                
                # 移出左侧字符
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                
                l += 1

        l, r = str_range
        return s[l : r + 1] if min_len < float("inf") else ""