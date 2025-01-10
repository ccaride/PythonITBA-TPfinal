import .mod1
import .mod4

def displayMenu():
    while True:    
        print('''
                        
        You can visualize the data as a Report (table) or as a Graph.
        [1] Report
        [2] Graph
        
            ''')

        optionDisp = int(input('Choose an option: '))

        if optionDisp == 1:
            print('You have chosen Report')
            inpt = mod1.askInputMenu()
            a = mod4.filter(inpt)
            mod4.report(a)
            break
                                
        elif optionDisp == 2:
            print('You have chosen Graph')
            inpt = mod1.askInputMenu()
            a = mod4.filter(inpt)
            mod4.graphic(a)
            break

        else:
            print('Invalid choice, should be 1 or 2. Make another try.')
