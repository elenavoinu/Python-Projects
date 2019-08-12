#Elena Voinu
#Using a conditional expression, write a statement that increments num_users if update_direction is 3, 
#otherwise decrements num_users. Ex: if num_users is 8 and update_direction is 3, then num_users becomes 9;
#if update_direction is 0, then num_users becomes 7. 


num_users = 8
update_direction = 3

#''' Your solution goes here '''
num_users = num_users + 1 if update_direction == 3 else num_users - 1

print('New value is:', num_users)