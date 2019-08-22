class Solution:
    def lengthOfLongestSubstring(self, s):
        conc = s[0]
        leng = 0
        for i in range (0,len(s)-1): 

            if s[i+1] in conc:
                for j in range(0,len(conc)):
                    if conc[j] == s[i+1]:
                        conc = conc[j+1:] + s[i+1]
                        break

            else:
                conc = conc + s[i+1]

            if len(conc)>leng:
                leng = len(conc) 
        return "There was a maximum of {} repeating characters in the string".format(leng)

print Solution().lengthOfLongestSubstring(raw_input("enter a string, please: "))
