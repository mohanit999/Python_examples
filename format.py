#placeHolder
pin, cash = input('Enter pin and cash').split(',')
#print('pin and cash are', pin, cash)
cashValue = int(cash)
#print('Type of cash is: ',type(cashValue))
atmAmount = 10000
remAmt = atmAmount-cashValue
#print('Take your cash:',cash,',','remainingAmt:',remAmt,end='-->')
#print('Thank you',end=', ')
#print('visit again')
#placeHolder
print('Take your cash {}, balance in your account is {}'.format(cashValue,remAmt))