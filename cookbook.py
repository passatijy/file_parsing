from sys import getdefaultencoding
import json 
with open('recipt.txt', encoding = 'utf-8') as f:
	inp_data_list = []
	for line in f:
		inp_data_list.append(line)
f.closed

# Сколько рецептов:
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
			i = i + 1
		out_list.append(inp_list[k])
		k = k + 1
	return out_list

def list_to_dict(inp_list):
	out_dict = {}
	out_dict_key = ''
	out_dict_key = inp_list.pop(0)
	out_dict[out_dict_key] = inp_list
	return out_dict

def lst_iter_to_lst_of_d(inp_list):
	out_l_of_d = []
	input_temp_list	= clean_list(repeat_until_rcpcount(count_of_chapters(inp_list),inp_list).copy())
	for one_rcpt in input_temp_list:
		out_l_of_d.append(list_to_dict(one_rcpt))
	return out_l_of_d

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

def get_shop_list_by_dishes(dishes, person_count, menu):
	result = {}
	for ordered_dish in dishes:
		print('Dish:', ordered_dish)
		for dish in menu:
			if list(dish.keys())[0] == ordered_dish: 
				#print('Dish(second cycle):', dish)
				for ingridient in dish:
					print('ingridient ', ingridient)
					temp_dict = {}
					for dish_elem in dish[ingridient]:
						if dish_elem['ingridient_name'] not in result.keys():
							print('dish_elem[ingridient_name]', dish_elem['ingridient_name'])
							print('result values: ', result.keys())
							print('dish elem: ', dish_elem)
							for key in dish_elem:
								if key == 'quantity':
									temp_dict['quantity'] = int(dish_elem[key]) * person_count
								if key == 'measure':
									temp_dict['measure'] = dish_elem[key]
							#print('Temp dict: ', temp_dict)
							result[dish_elem['ingridient_name']] = temp_dict.copy()
						else: 
							print('dish elem: ', dish_elem, 'DUPLICATE FOUND!!!!')
							for key in dish_elem:
								if key == 'quantity':
									temp_dict['quantity'] = (int(temp_dict['quantity']) + int(dish_elem[key])) * person_count
								if key == 'measure':
									temp_dict['measure'] = dish_elem[key]
							#print('Temp dict: ', temp_dict)
							result[dish_elem['ingridient_name']] = temp_dict.copy()
						print('---------------------------------------------------------------------------')
					print('===================================dish finished=====================')
	return result

#print('Zakupka:', json.dumps(get_shop_list_by_dishes(['Omelett','Fajitos'],3,menu),sort_keys=True, indent=4, separators = (',',':')))

#print('cookbook result:', json.dumps(result_to_dict_of_dicts(lst_iter_to_lst_of_d(inp_data_list)), sort_keys=True, indent=4, separators = (',',':')))


def main_routine():
	menu = result_to_dict_of_dicts(lst_iter_to_lst_of_d(inp_data_list))
	menu_list=[]
	repeat = True
	while repeat == True:
		inp = input('Введите действие: q - выход; m - показать меню, l - составить список покупок:')
		if inp == 'q':
			repeat = False
		elif inp == 'm':
			print('Menu: ', json.dumps(menu, sort_keys=True, indent=2, separators = (',',':')))
		elif inp == 'l':
			for k in menu:

				menu_list.append(str(k.keys()).replace('dict_keys',''))
			print('доступные блюда', menu_list)
			inp_dish_list = input('         введите список блюд: ')
			inp_user_count = input('  введите количество персон: ')
			print('Список закупок:', json.dumps(get_shop_list_by_dishes(['Omelett','Fajitos'],3,menu),sort_keys=True, indent=4, separators = (',',':')))
		else:
			print('Неверный ввод, повторите.')

main_routine()

