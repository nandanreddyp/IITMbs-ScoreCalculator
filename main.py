from ScoresCal import *
def Calculate():
    global course
    print('Note: For any course, if you not attempted any quiz or ope give score as 0.')
    if course=='0 Python':
        Q1=input('Enter Quiz1 marks: ')
        Q3=input('Enter EndTerm/Quiz3 marks: ')
        P1=input('Enter OPE1 marks: ')
        P2=input('Enter OPE2 marks: ')
        GA=input('Enter Average Graded Assignment marks (including GRPA\'s): ')
        yesno=input(f'You entered {Q1,Q3,P1,P2,GA}, proceed? (y/n): ').lower()
        if yesno[0]=='y':
            py=StudProf(100)
            py.python(Q1,Q3,P1,P2,GA)
            play=input('Do you want to check for other course? (y/n): ').lower()
            if play[0]=='y':
                CourseSelec()
            else:
                print('\nThankyou for your time, hope you got your final score. For any feedback text me at telegram @pnreddyz !\n')
        else:
            Calculate()
    else:        
        Q1=input('Enter Quiz1 marks: ')
        Q2=input('Enter Quiz2 marks: ')
        Q3=input('Enter EndTerm/Quiz3 marks: ')
        GA=input('Enter Average Graded Assignment marks: ')
        yesno=input(f'You entered {Q1,Q2,Q3,GA}, proceed? (y/n): ').lower()
        if yesno[0]=='y':
            Stud = SubCal(Q1,Q2,Q3,GA)
            m1=Stud.meth1();m2=Stud.meth2()
            marks=StudProf(max(int(m1),int(m2)))
            if course=='2 Stats2':
                marks.stats2()
            else:
                marks.other()
            play=input('Do you want to check for other course? (y/n): ').lower()
            if play[0]=='y':
                CourseSelec()
            else:
                print('\nThankyou for your time, hope you got your final score. For any feedback text me at telegram @pnreddyz!\n')
        else:
            Calculate()
def CourseSelec():
    global course
    print(*courses,sep='\n')
    selection=input('Give the index number of your selection. Like 0,3 for English1\n')
    level=courses[int(selection[0])];course=level[int(selection[-1])]
    print(f'Your selection is {course}')
    proceed=input('Do you want to proceed? (y/n): ').lower()
    if proceed[0]=='y':
        Calculate()
    else:
        CourseSelec()
print('Welcome to Score Calculator of IITM BS Foundation Level\n')
Name=input('Your name? ')
print(f'Hi, {Name}. Select the course you want to calculate final score :')
CourseSelec()

# Ga-10
# Max(quiz1,quiz2)-(20)---a% x 0.2
# End term-(60)---a% x0.6
# Bonus(Course participation -10)
#meth 2
# Ga- 10
# Quiz1-(20)--- a% x 0.2
# Quiz2-(30)---a% x 0.3
# End term -(40)---a% x 0.4
# Bonus(Course participation - 10)
