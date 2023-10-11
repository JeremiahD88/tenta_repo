

print('Beräknar differensen av jämna/udda tal...')

udda_list = []
jämn_list = []

for i in range(2, 2002,2):
    jämn_list.append(i)

for i in range(1, 2001,2):
    udda_list.append(i)

sum_udda = sum(udda_list)
sum_jämn = sum(jämn_list)

print(f'Differensen: {sum_jämn - sum_udda}')

#print(udda_list)
#print(len(jämn_list))
