from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parents = defaultdict(lambda: None)
        self.rank = defaultdict(int)
    
    def find(self, node):
        while self.parents[node] != None:
            if self.parents[self.parents[node]]:
                self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        if self.rank[parent1] >= self.rank[parent2]:
            self.parents[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = {}
        uf = UnionFind()
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                names[account[i]] = name
                if i+1 < len(account):
                    uf.union(account[i], account[i+1])
       # print(uf.parents)
        children = {}
        for email in names.keys():
            if not uf.parents[email] and email not in children:
                children[email] = set()
                continue
            parent = uf.find(email)
           # print(email, parent)            
            if parent not in children:
                children[parent] = set()
            children[parent].add(email)
        
        
        #print(children)
        #print(names)
        uniqueAccounts = []
        for parent, emails in children.items():
            emails.add(parent)
            account = [names[parent]] + sorted(list(emails))
            uniqueAccounts.append(account)
        
        return uniqueAccounts
        

