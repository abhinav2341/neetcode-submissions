class Solution:
    def isValid(self, s: str) -> bool:
      st=[]
      for x in s:
        if x in ['(','[','{']:
          st.append(x)
        else:
          if len(st)==0:
            return False
          if x==')' and st[-1]=='(':
            st.pop()
          elif x==']' and st[-1]=='[':
            st.pop()
          elif x=='}' and st[-1]=='{':
            st.pop()
          else:
            return False
      return len(st) == 0
