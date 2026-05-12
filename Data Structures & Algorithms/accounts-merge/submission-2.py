class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        res = []
        adj = defaultdict(list)     # 邻接表：用于构建邮箱之间的图关系
        emailToName = {}            # 映射：邮箱 -> 用户名（用于最后找回名字）

        # --- 步骤 1：构建图 (Graph Construction) ---
        for acc in accounts:
            name = acc[0]           # 账户名
            firstEmail = acc[1]     # 取第一个邮箱作为“中心点”来连接其他邮箱
            
            # 建立邮箱到名字的映射，即使该账户只有一个邮箱也能被记录
            if firstEmail not in emailToName:
                emailToName[firstEmail] = name
                
            for i in range(2, len(acc)):
                nextEmail = acc[i]
                # 在第一个邮箱和当前邮箱之间建立无向边
                # 这种“星型结构”足以让同一账户下的所有邮箱连通
                adj[firstEmail].append(nextEmail)
                adj[nextEmail].append(firstEmail)
                emailToName[nextEmail] = name

        visited = set()             # 标记集合：记录已访问过的邮箱，防止死循环和重复计算

        # --- 步骤 2：深度优先搜索 (DFS) ---
        def dfs(email, component):
            visited.add(email)      # 标记当前邮箱已访问
            component.append(email) # 将当前邮箱加入当前连通分量（同一个人的邮箱集合）

            # 访问所有相邻的邮箱（即在同一个账户里出现过的邮箱）
            for nei in adj[email]:
                if nei not in visited:
                    dfs(nei, component)
            
        # --- 步骤 3：遍历并合并 (Traversal & Merging) ---
        for e in emailToName:
            if e not in visited:
                # 发现一个新的连通分量，说明是一个独立的人
                component = []
                dfs(e, component)
                # 题目要求：结果需包含名字，且邮箱部分需要按字典序排序
                # [emailToName[e]] 是一个列表，+ 拼接两个列表
                res.append([emailToName[e]] + sorted(component))
        
        return res