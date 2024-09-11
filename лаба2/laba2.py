# 10. Написать функцию, которая принимает на вход две
# разных строки и возвращает количество совпадений двух символов в строках. Например, на входе две строки «xadasw» и
# «xad» совпадением будет считаться группа символов «xa» и «ad».

def search_matches(str1:str, str2:str) :

    matches = 0
    minLen = min(len(str1),len(str2))

    for i in range(minLen-1):
        substring1 = str1[i:i+2]
        substring2 = str2[i:i+2]

        if substring1 == substring2:
            matches += 1

    return f'matches {matches}'


print(search_matches('xadasw','xad'))
print(search_matches('xadasw','xadasw'))
print(search_matches('',''))


s = 'strotrka'
print(s.count('tr'))

#проверено. сделать отчет
