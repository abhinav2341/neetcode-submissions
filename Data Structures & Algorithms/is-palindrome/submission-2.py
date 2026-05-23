class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(s.split(" ")).lower()


        str=''
        for i in s:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                str+=i
            if ord(i) in range(ord('0'),ord('9')+1):
                str+=i

        i=0
        j=len(str)-1
        
        while i<j:
            # print(s[i],s[j])
            if str[i]!=str[j]:
                return False
            i=i+1
            j=j-1
        
        return True