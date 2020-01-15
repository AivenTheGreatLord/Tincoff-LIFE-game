import random as rd
import math as m

f = open('VAM.txt', 'r')
text = f.read()
words = text.split()
i_dict = {}

for i in range(1,len(words)):
    if words[i-1] in i_dict:
        i_dict[words[i-1]] += [words[i]]
    else:
        i_dict[words[i-1]] = [words[i]]

average_length = round(len(words)/len(text.split(".")))
delta_add = int(average_length/3)

print("Напишите NEXT для генерации следующего предложения или EXIT чтобы выйти")

while True:
    command = input()
    if command == "NEXT":
        s = [words[rd.randint(0,len(words))]]
        this_average_length = average_length + round(rd.randint(-1 * delta_add, delta_add))
        for i in range(1,this_average_length):
            if s[i-1] in i_dict:
                r = rd.randint(0,len(i_dict[s[i-1]])-1)
                values = i_dict[s[i-1]]
                s.append(values[r])
                #s.append(i_dict[s[i-1]][rd.randint(0,len(i_dict[s[i-1]]))])
            else:
                s.append(words[rd.randint(0,len(words))])
        print(*s)
    elif command == "EXIT":
        break
    else:
        continue
