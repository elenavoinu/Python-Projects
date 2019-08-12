# Elena Voinu

male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }

# Use set methods to create sets all_names, neutral_names, and specific_names.

''' Your solution goes here '''
all_names = male_names.union(female_names)
#Added print statements just to check if the right names are displayed
print("All of the top 10 male and all of the top 10 female names:\n",all_names,"\n")
neutral_names = male_names.intersection(female_names)
print("Names found in both male_names and female_names:\n",neutral_names,"\n")
specific_names =male_names.symmetric_difference(female_names)
print("Gender specific names found only in one of the top 10 sets:\n",specific_names)
