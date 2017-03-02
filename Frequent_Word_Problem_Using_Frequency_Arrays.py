def SymbolToNumber(x):
    return {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3,
    }[x]
def PatternToNumber(pattern):
    if(len(pattern)== 0):
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:len(pattern)-1]
    return (4 * PatternToNumber(prefix) + SymbolToNumber(symbol))

#print PatternToNumber("AGT")

def NumberToSymbol(x):
    return {
         0 : 'A',
         1 : 'C',
         2 : 'G',
         3 : 'T',
    }[x]

def NumberToPattern(index, k):
    if (k == 1):
        return NumberToSymbol(index)
    prefixIndex = index/4
    r = index%4
    symbol = NumberToSymbol(r)
    prefixPattern = NumberToPattern(prefixIndex,k-1)
    return prefixPattern + symbol

#print NumberToPattern(15,2)

def computingFrequencies(text,k):
    frequencyArray = []
    for i in range(0,(4**k)):
        frequencyArray.append(0)
    for i in range(0, len(text)-k+1):
        pattern = text[i:i+k]
        j = PatternToNumber(pattern)
        frequencyArray[j] = frequencyArray[j] + 1
    return frequencyArray

def fasterFrequentWords(text, k):
    frequentPatterns = []
    frequencyArray = computingFrequencies(text, k)
    maxCount = max(frequencyArray)
    for i in range(0,(4**k)):
        if frequencyArray[i] == maxCount:
            pattern = NumberToPattern(i,k)
            frequentPatterns.append(pattern)
    return frequentPatterns

text = "AACGAAAAAATTTTTTT"
print fasterFrequentWords(text,2)
