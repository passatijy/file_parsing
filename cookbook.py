from sys import getdefaultencoding
import json 
with open('recipt.txt') as f:
	inp_data_list = []
	for line in f:
		inp_data_list.append(line)
f.closed

# Сколько рецептов
def count_of_chapters(input_list):
	counter = 0
	'''
	Входной параметр - список с "главами", разбитый по пустым строкам. Считаю количество пустых строк.
	'''
	for one_item in input_list:
		if one_item == '\n':
			counter = counter + 1
	return counter

# надо разобрать лист из элементов по рецептам. Логика - читаю и удаляю с возвратом элементы 
# до тех пор пока не встретится
# пустая строка

def create_recpt(input_list):
	'''
	принимаю входящий список, и читаю его s позиции до пустой строки, выдаю список с собраным рецептом 
	и позицию на которой остановился при чтении.
	'''
	pos = 0
	output_list = []
	for one_item in input_list:
		pos = pos + 1
		if one_item != '\n':
			output_list.append(one_item)
		else:
			break
	return [output_list, pos]

#def create_list_of_rcpt(input_list):
#	pos = create_recpt(input_list)[1]
def clean_after_one_rcpt(input_list, pos):
	k = 0
	output_list = input_list.copy()
	while k < pos:
		#print('k= ',k)
		#print(output_list)
		del output_list[0]
		k = k + 1
	return output_list

def repeat_until_rcpcount(rcptcount,input_list):
	i = 0
	output_big_list = []
	output_list = []
	input_temp_list = input_list.copy()
	temp = []
	while i <= rcptcount:
		temp = create_recpt(input_temp_list).copy()
		output_big_list.append(temp[0])
		input_temp_list = clean_after_one_rcpt(input_temp_list,temp[1]).copy()
		i = i + 1
	return output_big_list

def clean_list(inp_list):
	out_list = []
	k = 0
	while k < len(inp_list):
		out_word = []
		if inp_list[k][0] == '\n':
			del inp_list[k][0]
		i = 0
		while i < len(inp_list[k]):
			inp_list[k][i] = inp_list[k][i].replace('\n','')
			#print('заменили', inp_list[k][i])
			i = i + 1
		out_list.append(inp_list[k])
		#print('Элемент списка номер :', k, ' является ', inp_list[k])
		k = k + 1
	return out_list
# ['Omelett', '3', 'Egg | 2 | pc', 'Milk | 100 | ml', 'Tomato | 2 | pc']
# {'Omelett': ['3', 'Egg | 2 | pc', 'Milk | 100 | ml', 'Tomato | 2 | pc']}
# {'Omelett':[{'name':Egg,'quan':2,'meas':'pc'},{'Milk | 100 | ml'},{'Tomato | 2 | pc'}}]}
def list_to_dict(inp_list):
	out_dict = {}
	out_dict_key = ''
	out_dict_key = inp_list.pop(0)
	#print('Первый элемент',inp_list.pop(0),'остальное', inp_list)
	out_dict[out_dict_key] = inp_list
	return out_dict

def lst_iter_to_lst_of_d(inp_list):
	out_l_of_d = []
	input_temp_list	= clean_list(repeat_until_rcpcount(count_of_chapters(inp_list),inp_list).copy())
	for one_rcpt in input_temp_list:
		#print('one rcpt', one_rcpt)
		out_l_of_d.append(list_to_dict(one_rcpt))
	return out_l_of_d
# ['Omelett', '3', 'Egg | 2 | pc', 'Milk | 100 | ml', 'Tomato | 2 | pc']
# {'Omelett': ['3', 'Egg | 2 | pc', 'Milk | 100 | ml', 'Tomato | 2 | pc']}
# {'Omelett':[{'ingridient_name':Egg,'quantity':2,'meas':'pc'},{'Milk | 100 | ml'},{'Tomato | 2 | pc'}]}
# temp_list1 = [{'Omelett': ['3', 'Egg | 2 | pc', 'Milk | 100 | ml', 'Tomato | 2 | pc']}, {'Omelssasett': ['3', 'Easgg | 2 | pc', 'Mialk | 100 | ml', 'Togato | 2 | pc']}]
def result_to_dict_of_dicts(inp_list):
	big_in_list = inp_list.copy()
	k = 0
	while k < len(big_in_list):
		in_dict = big_in_list[k]
		for x in in_dict:
			in_list = in_dict[x]
			del in_list[0]
			out_list = [dict(zip(["ingridient_name", "quantity", "measure"], elem.split('|'))) for elem in in_list]
			big_in_list[k][x] = out_list
		k += 1
	return big_in_list

# проверяю словарь из словарей
#print('словарь из словарей из тестового списка. ',result_to_dict_of_dicts(temp_list1) )
# проверяю счетчик
#print('Количество абзацев: ', count_of_chapters(inp_data_list))
# проверяю генерацию рецепта из неразделенного списка
#end_pos = create_recpt(inp_data_list)[1]
#new_list = clean_after_one_rcpt(inp_data_list,end_pos)
#print('Собраный рецепт: ', create_recpt(inp_data_list)[0], 'position: ', create_recpt(inp_data_list)[1])
#print('Default encoding', getdefaultencoding())
#print('проверяю зачистку добавленых')

#print('Входной', inp_data_list)
#print('Потом', new_list)

# проверяю основной цикл
#print('Совсем конец', repeat_until_rcpcount(count_of_chapters(inp_data_list),inp_data_list))
#print('--- --- ---            --- --- ---')
#half_ready = clean_list(repeat_until_rcpcount(count_of_chapters(inp_data_list),inp_data_list))
#print('Очищеный', half_ready)
#print('--- --- ---            --- --- ---')
#print('List - to - dict', lst_iter_to_lst_of_d(inp_data_list))
#print('--- --- ---            --- --- ---')
#print('List - to - dict of dicts', result_to_dict_of_dicts(lst_iter_to_lst_of_d(inp_data_list)))
print('cookbook result:', json.dumps(result_to_dict_of_dicts(lst_iter_to_lst_of_d(inp_data_list)), sort_keys=True, indent=4, separators = (',',':')))