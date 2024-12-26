# Exercise 24: anagrams

def anagrams(word1, word2):
    return sorted(word1) == sorted(word2)


print(anagrams("doom", "mood"))
print(anagrams("cefgbad", "abcdefg"))
print(anagrams("tame", "team"))
print(anagrams("bomba", "clatt"))
print(anagrams("walter", "white"))
