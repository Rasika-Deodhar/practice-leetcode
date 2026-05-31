import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # words = paragraph.replace('.',' ').split()
        cleanPara = re.sub(r"[.;!,]", " ", paragraph)
        words = cleanPara.split()
        frequency={}

        for word in words:
            cleaned = word.lower().strip(".,!-[]?'")
            if cleaned not in banned and cleaned not in frequency:
                frequency[cleaned] = 1
            if cleaned in frequency:
                frequency[cleaned]+=1
        
        result = sorted(frequency.items(), key=lambda item:item[1], reverse=True)

        print(result)

        return result[0][0]