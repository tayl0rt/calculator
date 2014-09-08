"""
Calculator using functions for each operation, then calling the function based on user input.
Taylor Thompson, 2014
Version: 1.0 (stable)

The looping function is a while statement that runs again whether done = True/False.

The final elif in the if statement takes q from the user's raw_input and changes
done to done = False.

Any incorrect input from the user causes the error statement 'Sorry I don't know what you mean
and loops back to the selection process!
"""

done = False
while not done:

    # Application introduction
    print 'Hello, welcome to Basic Calculator'
    print 'Please select which type of math operation I can calculate for you!'
    print '1 - Addition'
    print '2 - Subtraction'
    print '3 - Multiplication'
    print '4 - Division'

    # app_process takes the actual decision from the user - selection determines which
    # part of the if statement to use
    app_process = raw_input('You can type 1, 2, 3, 4, or q (quit) ')

    # addition
    if app_process == '1':
        print 'You have selected Addition. We\'ll use the format a + b = c'
        a = float(raw_input('What is a? '))
        b = float(raw_input('What is b? '))
        c = a + b
        print 'the answer is ', c

    # subtraction
    elif app_process == 2:
        print 'You have selected Subtraction. We\'ll use the format a - b = c'
        a = float(raw_input('What is a? '))
        b = float(raw_input('What is b? '))
        c = a - b
        print 'The answer is ', c

    # multiplication
    elif app_process == 3:
        print 'You have selected Multiplication. We\'ll use the format a * b = c'
        a = float(raw_input('What is a? '))
        b = float(raw_input('What is b? '))
        c = a * b
        print 'The answer is ', c
    # division
    elif app_process == 4:
        print 'You have selected Division. We\'ll use the format a / b = c'
        a = float(raw_input('What is a? '))
        b = float(raw_input('What is b? '))
        c = a / b
        print 'The answer is ', c

    # q exits the application
    elif app_process == 'q':
        print 'Take care until next time!'
        done = True
    # any incorrect/irrelevant input triggers an "error-like" statement!
    else:
        print 'Sorry I don\'t know what you mean!'