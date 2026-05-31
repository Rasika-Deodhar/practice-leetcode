class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []

        hashmap={}

        for i,word in enumerate(words):
            # print(i,word)
            chars = list(word)
            for c in chars:
                if c not in hashmap:
                    hashmap[c]={i:1}
                else:
                    if i in hashmap[c].keys():
                        hashmap[c][i]+=1
                    else:
                        hashmap[c][i]=1
        print(hashmap)

        common = []
        for k,v in hashmap.items():
            print(k,v)
            if len(v) == len(words):
                freq = min(v.values())
                result.extend(k*freq)
        
        return result