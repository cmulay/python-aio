# Imports
import time
import gensentence

# Setting the test phrase and calculating total number of words
test_phrase = gensentence.generate_sentence()
total_count = len(test_phrase.split())

# Setting the Window
print('-------------\n'+'This is Typing Test! Enter the words at your pace we will calculate your accuracy and wpm and much more !\n'+'-------------\n')
neglect = input("Press ENTER to start\n----------------")

t0 = time.time()  # Timer starts only when ENTER has been pressed.
print('Test Phrase:\n\n\t'+test_phrase, '\n')
print('-------------\n')
# Getting User Entered String
get_text = str(input("Start Typing:\n\n\t"))
print("")
t1 = time.time()  # Timer ends

# Calculating Results
input_total_count = len(get_text.split())
accuracy = len(set(get_text.split()) & set(test_phrase.split()))
accuracy = (accuracy / total_count)
timeTaken = (t1 - t0)
wpm = (input_total_count / timeTaken) * 60
# Displaying Results
print('Total words \t :', input_total_count)
print('Time used \t :', round(timeTaken, 2), 'seconds')
print('Your accuracy \t :', round(accuracy, 3) * 100, '%')
print('Speed is \t :', round(wpm, 2), 'words per minute')

print('-Developed by: Chinmay Mulay'
      '-Enhanced by @kaar07')

