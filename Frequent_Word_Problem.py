def patternCount(text, pattern):
    count = 0
    for i in range(0, len(text)):
        if (text[i: i+len(pattern)] == pattern):
            count = count + 1

    return count


def frequentWords(text, k):
    frequentPatterns = []
    count = []
    for i in range(0, len(text)-k):
        pattern = text[i:(i+k)]
        count.append(patternCount(text, pattern))
    #print count

    maxCount = max(count)
    #print "Max Count", maxCount

    for i in range(0, len(text)-k):
        if (count[i] == maxCount):
            frequentPatterns.append(text[i:(i+k)])

    frequentPatterns = list(set(frequentPatterns))
    return frequentPatterns

text = "AAATATATATAGAGAGAGAGCAATGCAAGCTCGAATCGTGTCAA"
print frequentWords(text,2)
 
