# Remove Substring
# mainStr = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog", "the", "dog", "slept", "over", "the", "verandah"]
# subStr = "over"

# Aapko aisa program likhna hai, jo subStr ki saari occurences ko mainStr se hata degi. Yaani uppar wale program ka output yeh hoga:

# the quick brown fox jumped the lazy dog. the dog slept the verandah.
mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
str3= mainStr.replace("over","")
print(str3)
############################################################################
# Bonus Part
mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on"
# mainStr mei subStr ko replacementStr se replace kar kar print karo.
# the quick brown fox jumped on the lazy dog. the dog slept on the verandah.
mainStr=mainStr.replace(subStr,replacementStr)
print(mainStr)





