'''
cook_book = {
  'Омлет': [
    {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
'''

#for one_rcpt in [{'oml':['3','eg|3|sh','tom|5|sh']}]:
#for x in {'oml':['3','eg|3|sh','tom|5|sh']}:
#	temp_val = one_rcpt[x]
#	del temp_val[0]

input_list = {'Omelett': ['3', 'Egg | 2 | pc', 'Milk | 100 | ml', 'Tomato | 2 | pc']}
int_list = []
temp_dict = {}
out_list = []

input_list2 = ['3', 'Egg | 2 | pc', 'Milk | 100 | ml', 'Tomato | 2 | pc']
out_list = list(range(int(input_list2[0])))
del input_list2[0]
i = 0
for x in input_list2:
	temp_dict = {}
	#print('elem: ', x)
	temp_dict['ingridient_name'] = x.split('|')[0]
	out_list[i] = temp_dict
	#print('temp_dict',temp_dict)
	#print('out_list',out_list)
	i = i + 1
print('Ready list of dicts:',temp_dict)		

'''
in_list = ['aa|11|ml','bb|22|gr']
out_list = [dict(zip(["ingridient_name", "quantity", "measure"], elem.split('|'))) for elem in in_list]
'''

big_in_list = [{'omlet':['1', 'aa|11|ml','bb|22|gr']}, {'fried potato':['2', 'pot|33|pc','tomat|100|gr']}]
#in_dict = {'omlet':['1', 'aa|11|ml','bb|22|gr']}
#in_list = ['1', 'aa|11|ml','bb|22|gr']
k = 0
while k < len(big_in_list):
    in_dict = big_in_list[k]
    for x in in_dict:
        in_list = in_dict[x]
        del in_list[0]
        out_list = [dict(zip(["ingridient_name", "quantity", "measure"], elem.split('|'))) for elem in in_list]
        big_in_list[k][x] = out_list
    k += 1
'''
#tmp_d = in_list3['dd']
for elem in in_list3:
    out_dict3 = {}
    tmp_d = elem.split('|')
    out_dict3['ingridient_name'] = tmp_d[0]
    out_dict3['quantity'] = tmp_d[1]
    out_dict3['measure'] = tmp_d[2]
    out_list.append(out_dict3)
'''


#print('out_dic', out_dict3)
print('out_list', out_list)
print('out_dict', in_dict)
print('out big dict', big_in_list)
