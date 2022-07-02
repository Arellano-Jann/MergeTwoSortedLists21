# def isSubsequence(s, t):
#     ascending = []
#     for char in s:
#         map(t.find, char)

# def isSubsequence(s, t):
#     ascending = list(map(t.find, s))
#     print(ascending)
#     return False if -1 in ascending else sorted(ascending) == ascending and len(set(ascending)) == len(ascending)

def isSubsequence1(s, t): # 5% cop
    if not s:
        return True
    if not t:
        return False
    if s[0] == t[0]:
        return isSubsequence(s[1:], t[1:])
    return isSubsequence(s, t[1:])

def isSubsequence2(s, t): # 74% 
    t = iter(t)
    return all(c in t for c in s)

def isSubsequence(s, t): # 83%
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i+1:]
    return True

print(isSubsequence('abc', 'abcdabdab')) # True
print(isSubsequence('abc', 'ahbgdc')) # True
print(isSubsequence('axc', 'ahbgdc')) # False
print(isSubsequence('', 'ahbgdc')) # True
print(isSubsequence('abc', '')) # False
print(isSubsequence('b', 'c')) # False
print(isSubsequence("aaaaaa", "bbaaaa")) # False
print(isSubsequence("ab", "baab")) # True