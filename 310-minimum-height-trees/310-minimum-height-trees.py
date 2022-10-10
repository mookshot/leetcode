class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 노드 갯수와 무방향 그래프를 입력받고 최소 높이가 되는 루트의 목록 리턴.
        # 리프노드를 계속 삭제하면 루트가 남게 된다. 그게 바로 정답!
        
        
        if n <= 1  :
            return [0] # n이 1이하일때 예외처리 
        
        
        # 그래프로 우선 만들어 준다.
        
        graph = collections.defaultdict(list)
        
        for i, j in edges : 
            graph[i].append(j)
            graph[j].append(i)
        
        print(graph)
        
        # 리프노드 추가. 그래프에서 1개씩만 달려있으면 리프 노드임
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        print(leaves)
        # root 남을때까지 한무 실행
        while n > 2 : 
            n -= len(leaves)
            new_leaves = []
            for i in leaves :
                neighbor = graph[i].pop() # 그래프의 리프노트 삭제 [무방향이라 양쪽 다 해줘야함]
                graph[neighbor].remove(i) # 그래프의 리프노트 삭제 [무방향이라 양쪽 다 해줘야함]
                
                if len(graph[neighbor]) == 1 :  # 그래프가 삭제되면서 기존에는 리프가 아니였는데 이제 사이즈 1남으면 리프가 됨
                    new_leaves.append(neighbor) # 새로운 리프노드에 추가 해준다.

            leaves = new_leaves # 새로운 리프노드를 leaves에 넣어준다.
        
        return leaves
