# Trivia Game (by grandmaster Brendon Tran 😁)
import random
import time

def trivia():
  topic = random.randint(1, 4)
  name = input('Welcome to Brendon\'s trivia! Enter your name: ')
  instr = input(f'''\nHello, {name}! Here are instructions for the game:\n
- Each question will give you three answer choices listed with a number. Type the number of the desired answer choice to submit your answer.
- There are currently three different quiz topics. They are randomly chosen after you\'re ready.
- Be quick! You only get 10 seconds to answer each question.
- At the end, we'll show you the results to see which ones you got correct and incorrect.\n
Are you ready? Type yes to continue. ''')

  if instr == 'Yes' or instr == 'yes':
    print('\nNice! Have fun and good luck!')
  elif instr == 'YES' or instr == 'YES!':
    print('\nI like the confidence! Glhf! :]')
  elif instr == 'nuh uh' or instr == 'Nuh uh':
    print('\nyuh huh')
  elif instr == 'No' or instr == 'no':
    print('\naww :[ see you again!')
    exit()
  elif instr == 'NO' or instr == 'NO!':
    print('\nOkay okay! Sorry!')
    exit()
  else:
    print('\nStop trolling. BE GONE! 🪄')
    exit()

# Celebrities
  def celeb():
    points = 0
    q1 = int(input('''\nQ1) As of April 2024, who is the most popular music artist?
1. Drake
2. Taylor Swift
3. DJ Khaled
4. Lana Del Ray\nEnter your answer number here: '''))
    if q1 == 2:
      points += 1
    else:
      points += 0
    
    q2 = int(input('''\nQ2) Who was the first winner of The Masked Singer?
1. T-Pain
2. Wayne Brady
3. Amber Riley
4. Jewel\nEnter your answer number here: '''))
    if q2 == 1:
      points += 1
    else:
      points += 0
    
    q3 = int(input('''\nQ3) Which tech entrepreneur named his son X Æ A-12?
1. Bill Gates
2. Steve Jobs
3. Mark Zuckerberg
4. Elon Musk\nEnter your answer number here: '''))
    if q3 == 4:
      points += 1
    else:
      points += 0
    
    q4 = int(input('''\nQ4) Who created the hit song "Nobody" in 2018?
1. Kim Kardashian
2. Mitski
3. Beyonce
4. Cardi B\nEnter your answer number here: '''))
    if q4 == 2:
      points += 1
    else:
      points += 0
    
    q5 = int(input('''\nQ5) Who is the oldest Kardashian sibling?
1. Rob Kardashian
2. Kim Kardashian
3. Kourtney Kardashian
4. Khloe Kardashian\nEnter your answer number here: '''))
    if q5 == 3:
      points += 1
    else:
      points += 0
    
    # Celebrity Overview
    print(f'\nCorrect: {points}')
    print(f'Incorrect: {5 - points}')
    if points == 5 or points == 4:
      print('Amazing job! 🔥')
    elif points == 3 or points == 2:
      print('Okay... not bad!')
    else:
      print('Better luck next time! Come back strong!')
    
    print('\nQuestion Overview:')
    if q1 == 2:
      print('Q1: ✅')
    else:
      print('Q1: ❌')
    if q2 == 1:
      print('Q2: ✅')
    else:
      print('Q2: ❌')
    if q3 == 4:
      print('Q3: ✅')
    else:
      print('Q3: ❌')
    if q4 == 2:
      print('Q4: ✅')
    else:
      print('Q4: ❌')
    if q5 == 3:
      print('Q5: ✅')
    else:
      print('Q5: ❌')
    retry = int(input('''\nSelect what to do next: 
1. Retry topic
2. Try a different topic
3. Quit
Enter the number here: '''))
    if retry == 1:
      return celeb()
    elif retry == 2:
      topic  = random.choice([2, 3])
      if topic == 2:
        print('\nTopic: Music')
        return music()
      else:
        print('\nTopic: Programming')
        return prgrm()
    else:
      print('\nThank you for playing! -Brendon :]')
      exit()
  
# Musical Instruments
  def music():
    points = 0
    q1 = int(input('''\nQ1) What year was the clarinet invented?
1. 1532
2. 1879
3. 1802
4. 1698\nEnter your answer number here: '''))
    if q1 == 4:
      points += 1
    else:
      points += 0
    
    q2 = int(input('''\nQ2) If there are 52 white keys on a piano, how many black keys does it have?
1. 26
2. 52
3. 36
4. 32\nEnter your answer number here: '''))
    if q2 == 3:
      points += 1
    else:
      points += 0
    
    q3 = int(input('''\nQ3) What is the oldest musical instrument in existence?
1. Drums
2. Bagpipe
3. Harp
4. Erhu\nEnter your answer number here: '''))
    if q3 == 1:
      points += 1
    else:
      points += 0
    
    q4 = int(input('''\nQ4) Which of the following is considered a woodwind instrument?
1. Trombone
2. Saxophone
3. Violin
4. Baritone\nEnter your answer number here: '''))
    if q4 == 2:
      points += 1
    else:
      points += 0
    
    q5 = int(input('''\nQ5) When was the violin invented? (approximately)
1. 1600s
2. 1530s
3. 1720s
4. 1400s\nEnter your answer number here: '''))
    if q5 == 2:
      points += 1
    else:
      points += 0
    
    # Music Overview
    print(f'\nCorrect: {points}')
    print(f'Incorrect: {5 - points}')
    if points == 5 or points == 4:
      print('Amazing job! 🔥')
    elif points == 3 or points == 2:
      print('Okay... not bad!')
    else:
      print('Better luck next time! Come back strong!')
    
    print('\nQuestion Overview:')
    if q1 == 4:
      print('Q1: ✅')
    else:
      print('Q1: ❌')
    if q2 == 3:
      print('Q2: ✅')
    else:
      print('Q2: ❌')
    if q3 == 1:
      print('Q3: ✅')
    else:
      print('Q3: ❌')
    if q4 == 2:
      print('Q4: ✅')
    else:
      print('Q4: ❌')
    if q5 == 2:
      print('Q5: ✅')
    else:
      print('Q5: ❌')
    retry = int(input('''\nSelect what to do next: 
1. Retry topic
2. Try a different topic
3. Quit
Enter the number here: '''))
    if retry == 1:
      return music()
    elif retry == 2:
      topic  = random.choice([1, 3])
      if topic == 1:
        print('\nTopic: Celebrities')
        return celeb()
      else:
        print('\nTopic: Programming')
        return prgrm()
    else:
      print('\nThank you for playing! -Brendon :]')
      exit()
  
# Programming
  def prgrm():
    points = 0
    q1 = int(input('''\nQ1) What does HTML stand for? 
1. Hypertext Markup Language
2. Hashmap Texting Markup Language
3. Hyper Terabyte Mashup Linguistic
4. Hypertech Mainframe Language\nEnter your answer number here: '''))
    if q1 == 1:
      points += 1
    else:
      points += 0
    
    q2 = int(input('''\nQ2) Approximately 98 percent of websites use this coding language.
1. Python
2. Git
3. Javascript
4. C++\nEnter your answer number here: '''))
    if q2 == 3:
      points += 1
    else:
      points += 0
    
    q3 = int(input('''\nQ3) What function do you use to print out an object in Python?
1. print()
2. console.log()
3. $echo
4. input()\nEnter your answer number here: '''))
    if q3 == 1:
      points += 1
    else:
      points += 0
    
    q4 = int(input('''\nQ4) What is the purpose of the programming language CSS?
1. Overall website structure
2. Website display
3. Website interactiveness
4. CSS isn\'t a web developing language\nEnter your answer number here: '''))
    if q4 == 2:
      points += 1
    else:
      points += 0

    q5 = int(input('''\nQ5) Which element would you use to display a heading in HTML?
1. heading('')
2. <header>
3. <title>
4. <h1>\nEnter your answer number here: '''))
    if q5 == 4:
      points += 1
    else:
      points += 0
    
    # Programming Overview
    print(f'\nCorrect: {points}')
    print(f'Incorrect: {5 - points}')
    if points == 5 or points == 4:
      print('Amazing job! 🔥')
    elif points == 3 or points == 2:
      print('Okay... not bad!')
    else:
      print('Better luck next time! Come back strong!')
    
    print('\nQuestion Overview:')
    if q1 == 1:
      print('Q1: ✅')
    else:
      print('Q1: ❌')
    if q2 == 3:
      print('Q2: ✅')
    else:
      print('Q2: ❌')
    if q3 == 1:
      print('Q3: ✅')
    else:
      print('Q3: ❌')
    if q4 == 2:
      print('Q4: ✅')
    else:
      print('Q4: ❌')
    if q5 == 4:
      print('Q5: ✅')
    else:
      print('Q5: ❌')
    retry = int(input('''\nSelect what to do next: 
1. Retry topic
2. Try a different topic
3. Quit
Enter the number here: '''))
      
    if retry == 1:
      return prgrm()
    elif retry == 2:
      topic  = random.choice([1, 2])
      if topic == 2:
        print('\nTopic: Music')
        return music()
      else:
        print('\nTopic: Celeb')
        return celeb()
    else:
      print('\nThank you for playing! -Brendon :]')
      exit()

  # Topic Selector
  if topic == 1:
    topic = 'Celebrities'
    print('\nTopic: ' + topic)
    return celeb()
  elif topic == 2:
    topic = 'Musical Instruments'
    print('\nTopic: ' + topic)
    return music()
  elif topic == 3:
    topic = 'Programming'
    print('\nTopic: ' + topic)
    return prgrm()
  else:
    print('Error')
    exit()

trivia()