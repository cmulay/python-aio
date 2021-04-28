# Imports
import time

# Setting the test phrase and calculating total number of words
test_phrase = "The woods are lovely, dark and deep, But I have promises to keep, And miles to go before I sleep, And miles to go before I sleep."
total_count = len(test_phrase.split())

t0 = time.time()
# Setting the Window
print('-------------\n'+'This is Typing Test! Enter the words at your pace we will calculate your accuracy and wpm and much more !\n'+'-------------\n')
print('Test Phrase:\n'+test_phrase, '\n')
print('-------------\n')
print('Start Typing:\n')
# Getting User Entered String
get_text = str(input())
# Calculating Results
t1 = time.time()
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

print('-Developed by: Chinmay Mulay')
