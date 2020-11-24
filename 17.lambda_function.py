'''
Lambda Function ke bare me:

1. Ye ek anonymous function hai.
2. Lambda function me hum multiple arguemts de sakte hain. But iss fucntion ke andar kewal single expression diya ja sakta hai.

Lambda fucntion Syntax:

lambda numberOfArguments : your expression
'''

'''
Lambda fucntion me colon se pahle jo 'message' likha hai wo ek argument hai.
AUr colon ke bad print jo kiya gaya hai wo ek expression hai ki lambda ko call karte hi wo hame ye output show kardega.
'''

# ye lambda fucniton ko define kiya gaya
mylambda = lambda message : print('\n', message)

# call lambda function
mylambda('Hello Lambda funciton.')

# sum fucntion using lambda
mysum = lambda a, b : a + b
# recive_mysum_answer = mysum(1000, 200)
# mynum = int(input('\nEnter first number: '))
# print('\nMy sum lambda answer: ', mysum(int(input('\nEnter first number: ')), 200))
print('\nMy sum lambda answer: ', mysum(100, 200))

# Use lambda funciton in normal funciton
def my_lam_sum_fun(normal_a_argument):
    # define lambda fucnton with one argument
    mysum = lambda lambda_b_argument : normal_a_argument + lambda_b_argument
    # call lambda function and pass one argument lambda_b_argument
    output = mysum(75)
    print('\nMy output: ', output)

# call normal fucton and pass one argumet normal_a_argument
my_lam_sum_fun(200)