# Michael Coomey - Lab #2
Answers = (
        'The function called str transforms its input into a string representation.',
        'No.  They are seperate variables in different scopes that happen to have the same name.',
        'Sure.  The body of the function could be written as:\n  Process(GetANumber("Enter a positive number, " + requestString("Enter your name")))',
        'The value returned by GetANumber is passed to the Process function as the variable N.',
        'GetANumber returns a value because the return statement has an argument, N.  The returns in the other functions do not have an argument.'
      )


def GetANumber (PromptMessage, Limit):
    Num = -1
    while ((Num < 1)|(Num > Limit)):
        Num = requestNumber(PromptMessage)
        if Num is None:
            return Num
        if ((Num <1)|(Num > Limit)):
            showError("Input is out of range! Must be 1 to " + str(Limit))
    return Num

def Process (N):
    text = ("The answer to number " + str(N) + " is: \n") + (Answers[int(N-1)])
    showInformation(text)
    return

def Run():

    MyName = requestString("Enter your name")
    N = GetANumber("Which question do you want answered, " + MyName + " (1-" + str(len(Answers)) + ")? ", len(Answers))
    if N is None:
        print "Quitting"
        return
    Process(N)
    return 