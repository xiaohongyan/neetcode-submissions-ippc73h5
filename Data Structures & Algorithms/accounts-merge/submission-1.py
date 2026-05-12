class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        res = []
        n = len(accounts)
        adj = defaultdict(list)
        emailToName = {}
        for acc in accounts:
            name = acc[0]
            firstEmail =acc[1]
            emailToName[firstEmail] = name
            for i in range(2, len(acc)):
                nextEmail = acc[i]
                adj[firstEmail].append(nextEmail)
                adj[nextEmail].append(firstEmail)    
                emailToName[nextEmail] = name

        emailGroup = defaultdict(list) # name, emails
        visited = set()

        def dfs(email, component):
            visited.add(email)
            component.append(email)

            for nei in adj[email]:
                if nei not in visited:
                    dfs(nei, component)
            
        for e in emailToName:
            if e not in visited:
                component = []
                dfs(e, component)
                res.append([emailToName[e]] + sorted(component))
        
        return res

        



