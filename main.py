import gspread, random
from faker import Faker

fake = Faker()

gc = gspread.service_account(filename='credentials.json')

sh = gc.open_by_key('15L6MwWfeVfG8lFYMkXUA_Bff3ge3dCqtrJlfBWDZjMg')

worksheet = sh.sheet1

# in JSON form
resp_in_json = worksheet.get_all_records()

# in LIST form
resp_in_list = worksheet.get_all_values()

data = ['Aditya', '26', 'Agra']

# Insert single row
# worksheet.insert_row(data, 1)

# delete single row
# worksheet.delete_row(1)

# multiple delete rows
# for i in range(1, len(resp_in_list)+1):
# 	worksheet.delete_rows(i)
# print(resp_in_list)


# ===============================================

lt = []
for i in range(10):
	lt = [
		fake.name(),
		fake.email(),
		fake.address(),
		fake.text(),
		str(random.randint(18, 50))
		]

	# worksheet.insert_row(lt)
# print(lt)

# get particular cell value
print(worksheet.get('A6'))
print(worksheet.get('C5'))

# update row
# update_row = worksheet.update('B1', 'Bingo!')
update_row = worksheet.update([['adam', 'demo', 'hjgsgfsdfsdj', 'uuriewyewrtywe', 72], 
										['adam1', 'demo1', 'hjgsgfsdfsdj', 'uuriewyewrtywe', 72]])