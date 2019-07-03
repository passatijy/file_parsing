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
	print('elem: ', x)
	temp_dict['ingridient_name'] = x.split('|')[0]
	out_list[i] = temp_dict
	print('temp_dict',temp_dict)
	print('out_list',out_list)
	i = i + 1
print('temp_dict',temp_dict)		

