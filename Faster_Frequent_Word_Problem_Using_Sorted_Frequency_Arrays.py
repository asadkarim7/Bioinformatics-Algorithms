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

def frequentWordsbySorting(text, k):
    frequentPatterns = []
    index = []
    count = []
    for i in range(0, len(text)-k+1):
        pattern = text[i : i+k]
        index.append(PatternToNumber(pattern))
        count.append(1)

    index.sort()

    for i in range(1, len(text)-k+1):
        if index[i] == index[i-1]:
            count[i] = count[i-1] + 1

    maxCount = max(count)

    for i in range(0, len(text)-k+1):
        if (count[i] == maxCount):
            pattern = NumberToPattern(index[i],k)
            frequentPatterns.append(pattern)
    return frequentPatterns


text = "AACGAAAAAATTTTTTT"
print frequentWordsbySorting(text,2)
