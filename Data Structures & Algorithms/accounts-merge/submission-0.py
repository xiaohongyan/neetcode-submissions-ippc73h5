class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        
        while self.parent[i] != root:
            tmp = self.parent[i]
            self.parent[i] = root
            i = tmp
        return root

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        
        if self.size[root_i] >= self.size[root_j]:
            root_i, root_j = root_j, root_i

        self.size[root_j] += self.size[root_i]
        self.parent[root_i] =  root_j
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        res = []
        emailToAcc = {} # email : index of account

        n = len(accounts)
        dsu = DSU(n)
        for i in range(n):
            name = accounts[i][0]
            emails = accounts[i][1:]
            for email in emails:
                if email not in emailToAcc:
                    emailToAcc[email] = i
                else:
                    dsu.union(i, emailToAcc[email])

        emailGroup = defaultdict(list)  # index of acc -> list of emails     
        for e, idx in emailToAcc.items():
            root = dsu.find(idx)
            emailGroup[root].append(e)

        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res






        