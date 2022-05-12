def quiz():

    print('Welcome to AskPython Quiz')
    answer=input('Are you ready to play the Quiz ? (yes/no) :')
    score=0
    total_questions=3
    
    if answer.lower()=='yes':
        answer=input('What is it that no one wants to have, but no one wants to lose, either?')
        if answer.lower()=='a lawsuit':
            score += 1
            print('correct')
        else:
            print('Wrong Answer :(')
    
    
        answer=input('What has two hands, a round face, always runs, yet always stays in place, too? ')
        if answer.lower()=='a clock':
            score += 1
            print('correct')
        else:
            print('Wrong Answer :(')
    
        answer=input('What is always on its way but never arrives?')
        if answer.lower()=='tomorrow':
            score += 1
            print('correct')
        else:
            print('Wrong Answer :(')


    mark=(score/total_questions)*100
    print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
    print('Marks obtained:',mark)
    print('BYE!')

quiz()