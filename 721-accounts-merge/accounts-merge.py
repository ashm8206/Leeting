class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in graph:
                    graph[email] = set()
                if len(account) > 2:
                    first_email = account[1]
                    graph[first_email].add(email)
                    graph[email].add(first_email)
        def dfs(email, visited, component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, visited, component)
        visited = set()
        result = []
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, visited, component)
                result.append([email_to_name[email]] + sorted(component))
        return result




class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))

        ownership = {} #email : union_id

        for i, (name, *emails) in enumerate(accounts):
            
            for email in emails:
                if email in ownership:
                    uf.union(i,ownership[email])
                ownership[email] = i 
                #Seperate one to track emails and initial roots encountered 
                # to unionize them if already found.
        #print(ownership)

        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
            #print(owner, uf.find(owner))
            #ans[owner].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
        
            
                
