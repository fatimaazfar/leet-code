class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = []
        for i in range(len(s)):
            if s[i] == '(':
                c.append('r')
            elif s[i] == ')' and c and c[-1] == 'r':
                c.pop()
            elif s[i] == '{':
                c.append('c')
            elif s[i] == '}' and c and c[-1] == 'c':
                c.pop()
            elif s[i] == '[':
                c.append('s')
            elif s[i] == ']' and c and c[-1] == 's':
                c.pop()
            else:
                c.append('x')
                
        if not c:
            return True
        return False
                
        