# Sorting
# Space Complexity: O(n) sorted() creates a new list
# Time Complexity: O(n log n) 

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
                    
        # sortedS = sorted(s)
        # sortedT = sorted(t)

        # for i in range(len(sortedS)):
        #     if(sortedS[i] != sortedT[i]):
        #         return False
        # return True

        return sorted(s) == sorted(t) # same thing, less code, you can compare lists in Python this way

# Hash Map
# Space Complexity: O(1) since we have at most 26 different characters
# Time Complexity: O(n+m) Where n is the length of string s and m is the length of string t

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        
        # return True

        # Better version would be:

        return countS == countT # dict equality in Python compares keys AND values