#Author: Jeremiah Danielsen
#Date  : 2023-10-13

def resis_calc(resistor_list):
    series_val = 0
    parallel_val = 0
    val = 0
    for values in resistor_list:
            series_val += values
            val = val + (1 / values)
            parallel_val = (1 / val)
    print(f'Serieresistens : {series_val}')
    print(f'Parallellresistens: {parallel_val}')

resistors = []

print('Ei22 - praktiskt prov ht23')
user_input = input('Ange resistorer: ')
user_int = user_input.split()
for i in user_int:
    res_int = int(i)
    resistors.append(res_int)
resis_calc(resistors)