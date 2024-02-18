import helpers

print ('''
    Welcome to c-finance! 
    With this APP you can explore and compare the three most important shares from the Argentinian Agricultural sector in the stock market. 
       ''')

def mainMenu():   
    while True:
        print('''
        What do you want to do?

        ****Main Menu****
        [1] Look at the Data available (Summary)
        [2] Request new Data
        [3] Visualize Data
        [4] Quit
                
        ''')

        optionMain = int(input('Choose an option: '))   

        if optionMain == 1:
            helpers.mod2.summary()

        elif optionMain == 2:
                        
            #Ask for the inputs and make request
            inpt = helpers.mod1.askInputMenu()
            helpers.mod2.request(inpt[0],inpt[1],inpt[2])
                
        elif optionMain == 3:
                    
            #Display menu
            helpers.mod3.displayMenu()

        elif optionMain == 4:
            break

        else:
            print('Invalid choice. Should be a number between 1 and 4. Make another try. :)')

    exit

mainMenu()

