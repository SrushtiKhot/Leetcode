class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w,a=0,0
        while(w<len(word) and a<len(abbr)):
        #If alphabet
            if abbr[a].isalpha():
                if abbr[a]==word[w]:
                    w+=1
                    a+=1
                else:
                    return False
            else: #If digit
                if abbr[a]=='0':
                    return False
                
                temp=0
                
                while(a<len(abbr) and abbr[a].isdigit()): #Loop to calculate total number to jump
                    temp=temp*10+(int)(abbr[a])
                    a+=1
                w+=temp
        return (a==len(abbr) and w==len(word))
    
    #Time complexity O(max(len(word),len(abbr)))
    #Space complexity O(1)
        