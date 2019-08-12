'''
@Elena Voinu
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters 
(R, G, B, Y) and the user must repeat the sequence. 
Create a for loop that compares the two strings.
For each match, add one point to user_score. Upon a mismatch, end the game.
'''

user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'

''' Your solution goes here '''
for i in range(len(simon_pattern)):
     
     if simon_pattern[i]==user_pattern[i]:
          user_score=user_score+1

     else:
          break

print('User score:', user_score)