from datetime import date, datetime

dateFormat = ('%Y-%m-%d')

def start_date(y): 
    while True:
        stDate = input('Insert the start date (YYYY-MM-DD): ')    
        
        try:  
            stDate = datetime.strptime(stDate,dateFormat)
            print("The data format is correct")
            y.append(stDate)
            end_date(y)
            break
        
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD. Try again.")
            
def end_date(y):    
    while True:
        endDate = input('Insert the end date(YYYY-MM-DD): ') 
            
        try:
            endDate = datetime.strptime(endDate,dateFormat)
            print("The data format is correct")

            if endDate > y[1]:
                print("End date is ok")
                y.append(endDate)
                #corre la funcion de busqueda
                break

            else: 
                print('The "end date" should be after the "start date". Try again.')

        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD. Try again.")
        

def askInputMenu():
    
    inpts = []
    
    while True:
    
        print('''
        The available tickers are:
        [1] BNG.BA  Bunge Limited (Farm Products)
        [2] DD.BA   Caterpillar Inc. (Farm & Construction Machinery)
        [3] CAT.BA  E. I. du Pont de Nemours and Company (Agricultural Chemicals)
            ''')

        ticker = int(input('Insert the ticker you want to request: '))

        tk = ["BNG.BA", "DD.BA", "CAT.BA"]

        if ((ticker >= 1) and (ticker <= 3)):
            inpts.append(tk[ticker-1])
            start_date(inpts)
            break
                          
        else:       
            print('Invalid choice, should be 1, 2 or 3. Try again.')
    
    return inpts