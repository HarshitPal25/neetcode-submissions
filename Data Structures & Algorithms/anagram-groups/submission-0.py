class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        anagram = {}
        for words in strs:
            sorted_word = "".join(sorted(words)) #withou join it would return a list of sorted word like [a,e,t]
            if sorted_word in anagram:
                anagram[sorted_word].append(words) # if the sorted key is present in dict it would add the word to that key as value
            else:
                anagram[sorted_word] = [words] #if key not present it would create sorted word as key and add the word to it as value
        return list(anagram.values()) # this helps return a list of only the values of anagram