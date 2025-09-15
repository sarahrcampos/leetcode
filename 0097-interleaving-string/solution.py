class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:  
        cache = {}      
        def dfs(i1, i2, i3):
            if i3 == len(s3) and i1 == len(s1) and i2 == len(s2): #fim da string
                return True
            if i3 == len(s3):
                return False
            if (i1, i2, i3) in cache:
                return cache[(i1,i2,i3)]

            if i1 < len(s1) and i2 < len(s2) and s1[i1] == s3[i3] and s2[i2] == s3[i3]: #se ambos são iguais
                cache[(i1,i2,i3)] = dfs(i1 + 1, i2, i3 + 1) or dfs(i1, i2 + 1, i3 + 1)
            elif i1 < len(s1) and s1[i1] == s3[i3]: #se apenas s1 é igual
                cache[(i1,i2,i3)] =  dfs(i1 + 1, i2, i3 + 1)
            elif i2 < len(s2) and s2[i2] == s3[i3]: #se apenas s2 é igual
                cache[(i1,i2,i3)] =  dfs(i1, i2 + 1, i3 + 1)            
            else:
                cache[(i1,i2,i3)] = False #ambos são diferentes ou chegou no fim das 2 strings, mas não de 1 delas
                        
            return cache[(i1,i2,i3)] 
        
        return dfs(0,0,0)
            
            
