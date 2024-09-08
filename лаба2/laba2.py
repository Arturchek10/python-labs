def search_matches(str1:str, str2:str) -> int:

    matches = 0
    minLen = min(len(str1),len(str2))

    for i in range(minLen-1):
        substring1 = str1[i:i+2]
        substring2 = str2[i:i+2]

        if substring1 == substring2:
            matches += 1

    return (matches)


print(search_matches('xadasw','xada'))