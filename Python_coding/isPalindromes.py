def isPalidrome():
  string1 = input('Enter a string : ')
  string2 = string1[::-1]
  if string1 == string2:
    print('is a  Palindrome')
  else:
    print ('not a palindrome')
isPalidrome()
 