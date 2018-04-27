while True:
    s=input('Enter something:')
    if s=='quit':
        break
    elif len(s)<3:
        print(s)
        continue
    else:
        print('The input is long enough')
print('done')

# while True: 
#     s = input('Enter something : ') 
#     if s == 'quit': 
#         break
#     if len(s) < 3: 
#         print('Too small') 
#         continue
#     print('Input is of sufficient length')
