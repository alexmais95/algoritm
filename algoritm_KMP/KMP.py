text = 'theloplohello'

pi = [0] * len(text)
j = 0
i = 1

while i < len(text):
    if text[i] == text[j]:
        pi[i] = j + 1
        j += 1
        i += 1
    else:
        if j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j-1]

print(pi)
