import matplotlib.pyplot as plt

bookList = []

def menuOrExit():
    print(58*'-')
    while True:
        try:
            choice = input('Would you like to return to the main menu? (Y) or (N) ')
            if choice.lower() == 'y':
                menu() #recalls the menu
                break
            elif choice.lower() == 'n':
                exit() #exits program
        except(TypeError, ValueError):
            pass
    print(58*'-')

def getBooks():
    totalValue = 0
    numOfBooks = 0
    # Code to calculate the total value and number of books
    print('-------------------------Option 1-------------------------')
    print('TITLE, AUTHOR, FORMAT, PUBLISHER, COST, STOCK, GENRE', 58*'-') #Formatting of file
    for book in bookList: #iterates over list to get each entity
        print(f'{book[1]} \nAuthor: {book[0]} \nFormat: {book[2]} \nPublisher:{book[3]} \nCost: {book[4]} \nStock:'
              f'{book[5]} \nGenre: {book[6]} \n\n', 58*'-') #entity items
        totalValue += float(book[4]) * float(book[5])  # calculates the total value of books in stock from the list
        numOfBooks += int(book[5])  # calculates the number of books in stock from the list
    print(f'Total Value: £{totalValue} Number Of Books: {numOfBooks}') #Outputs the total value of books in stock and number of books in stock.

    menuOrExit()

def getAverage():
    totalCost = 0
    averageCost = 0
    for book in bookList:
        if int(book[5]) > 0:
            totalCost += float(book[4])
    averageCost = totalCost / len(bookList) #calculates the average cost of books

    print('-------------------------Option 2-------------------------')
    print(f'The Average Cost of All Books Currently in Stock: £ {averageCost:.2f}')
    menuOrExit()

def getGenreReport():
    print('-------------------------Option 3-------------------------')
    genreDict = {}
    for i in range(len(bookList)):
        genre = bookList[i]
        if genre[6] in genreDict:   #plots the bar chart from the values gathered by the above code
            genreDict[genre[6]] = genreDict[genre[6]] + 1 * int(genre[5])
        else:
            genreDict[genre[6]] = 1 * int(genre[5])

    for key, value in genreDict.items(): #for loop to output each of the keys and its value
        print(f'{key} ---> {value}')
    menuOrExit()

def addNewBook():
    totalValue = 0
    numOfBooks = 0
    for book in bookList:
        totalValue += float(book[4]) * float(book[5])#calculates the total value of books in stock from the list
    originalAverageCost = float(totalValue) / len(bookList) #Calcs the original average costs of book

    innerList = [] #innerlist for the book data to added before appendage to main list
    print('-------------------------Option 4-------------------------')
    print('TITLE, AUTHOR, FORMAT, PUBLISHER, COST, STOCK, GENRE', 58*'-')  # Formatting of book input
    while True:
        try:
            title = str(input('Title: '))
            if (len(title) >= 2 ): #checks for a valid length for the title
                innerList.append(title)
                break #stop the while loop once the condition above is met
        except (TypeError, EOFError): #handles any input errors the user may have / makes sure the correct data is inputted.
            pass #reloops until no exceptions occur

    while True:
        try:
            author = str(input('Author: '))
            if (len(author) > 2):#checks for a valid length for the title
                innerList.append(author)
                break
        except (TypeError, EOFError):
            pass

    while True:
        try:
            availFormats = ['hb', 'pb'] #format available
            format = int(input('Chose Format, 1. Hardback 2. Paperback '))
            if (format > 0 and format <= 2): #makes sure input is within the range available
                    innerList.append(availFormats[format - 1]) #append the format in the posisiton of the inputted number - 1 to avoid list index out of range to the innerlist
                    break
        except (EOFError, ValueError):
            pass

    while True:
        try:
            publisher = str(input('Publisher: '))
            if (len(publisher) > 2):#checks for a valid length for the title
                innerList.append(publisher)
                break
        except (TypeError, EOFError):
            pass

    while True:
        try:
            cost = float(input('Cost: £ '))
            if (cost > 0):  # checks for a valid cost input
                innerList.append(cost)
                break
        except (TypeError, EOFError, ValueError):#handles any input errors the user may have / makes sure the correct data is inputted.
            pass

    while True:
        try:
            stock = int(input('Stock: '))
            if (stock >= 0):   # checks for a valid stock level input
                innerList.append(stock)
                break  #stop the while loop once the condition above is met
        except (TypeError, EOFError, ValueError):
            pass  #reloops until no exceptions

    while True:
        try:
            availGenres = ['fiction', 'biography', 'science', 'religion']  #available genres to chose from
            genre = int(input('Choose one. 1. Fiction 2. Biography 3. Science 4. Religion '))  #genre input
            if (genre >= 1 and genre <= 4):  #makes sure input is within the range available
                    innerList.append(availGenres[genre - 1])  #append the genre in the posisiton of the inputted number - 1 to avoid list index out of range to the innerlist
                    break
        except (TypeError, EOFError, ValueError):
            pass
    bookList.append(innerList)  #appends innerlist to main bookList
    for book in bookList:
        totalValue += float(book[4]) * float(book[5])
        numOfBooks += int(book[5])
    newAverageCost = float(totalValue) / len(bookList)
    averageCostDif = newAverageCost - originalAverageCost

    print(f'title:{innerList[1]} \nAuthor: {innerList[0]} \nFormat: {innerList[2]} \nPublisher: {innerList[3]} \nCost: '
          f'{innerList[4]} \nStock: {innerList[5]} \nGenre: {innerList[6]}\n\n', 58*'-')  #prints new books details
    print(f'Total Number Of Books In Stock: {numOfBooks} an increase of {innerList[5]}\nOld Average: {originalAverageCost:.2f}\nNew Average: '
          f'{newAverageCost:.2f}\nDifference: {averageCostDif:.2f}', 58*'-')  #prints the new total numofbooks its increase, the old, new averages and the difference between the 2
    menuOrExit()

def queryBook():
    print('-------------------------Option 5-------------------------')
    while True:
        try:
            bookToQuery = input('Title of Book: ')  #title input
            if len(bookToQuery) > 2 and not bookToQuery.isdigit():  #makes sure the input is valid i.e. not numbers and valid length
                break  #stop the while loop once the condition above is met
        except (TypeError, EOFError):  # handles any input errors the user may have / makes sure the correct data is inputted.
            pass  #reloops until no exceptions

    i = 0
    for book in bookList:
        i += 1
        if book[1].lower() == bookToQuery.lower():
            print(f'\n{book[1]} \nAuthor: {book[0]} \nFormat: {book[2]} \nPublisher:{book[3]} \nCost: {book[4]} \nStock:'
                  f' {book[5]} \nGenre: {book[6]} \n\n', 58*'-')  #entity items

            while True:
                try:
                    increaseOrDecrease = int(input('Would you like to 1. Increase Stock 2. Decrease Stock\n'))
                    if increaseOrDecrease >= 1 <= 2:  #makes sure the cor
                        if increaseOrDecrease == 1:  #increase option
                            while True:
                                try:
                                    increaseBy = int(input('How much would you like to increase by: ')) #stock increase input
                                    if increaseBy > 0:  #only executes if decreasinmg the stock by more than 0
                                        stock = int(book[5])  #gets the intial stock level in the list and converts from str to int
                                        stock = stock + increaseBy  #calcs the new stock level
                                        book[5] = stock  #sets new stock level in list
                                        print(f'increased stock by {increaseBy} to {book[5]}\n', 58*'-') #outputs how much the stock level increased and from what

                                    while True:
                                        try:
                                            another = input('Would you like to increase another? (y) or (n)')   #menu or exit choice input
                                            if another.lower() == 'y':
                                                queryBook()  #recalls this function to start again
                                            elif another.lower() == 'n':
                                                menuOrExit()  #option for menu or exit
                                        except (ValueError, EOFError, TypeError):  #handles any input errors the user may have / makes sure the correct data is inputted.
                                            pass  #reloops until no exceptions

                                except (TypeError, EOFError) as error:  #handles any input errors the user may have / makes sure the correct data is inputted.
                                    print(error)  #prints the error codes that occured
                                    pass  #reloops until no exceptions

                        elif increaseOrDecrease == 2:  #decrease choice
                            while True:
                                try:
                                    decreaseBy = int(input('How much would you like to decrease by:'))  #stock decrease input
                                    if decreaseBy > 0:  #only executes if decreasinmg the stock by more than 0
                                        if int(book[5]) > 0:  #only executes if the stock level is more than 0
                                            stock = int(book[5])  #fetches exisiting stock level and converts from str to int
                                            stock = stock - decreaseBy  #calcs new stock level
                                            if stock < 0:  #if new stock is less than 0 it doesn't allow the stock to be decreased as there isn't enough stock available
                                                print(f'Unable to decrease stock by {decreaseBy} not enough stock available')
                                                break  #stop the while loop once the condition above is met
                                            elif stock >= 0:
                                                book[5] = stock  #sets the new stock level in the list
                                                print(f'Decreased stock by {decreaseBy} to {book[5]}\n', 58*'-')
                                            while True:
                                                try:
                                                    another = input('Would you like to decrease another? (y) or (n)\n')  #menu or exit choice input
                                                    if another.lower() == 'y':
                                                        queryBook()  #recalls this function to start again
                                                    elif another.lower() == 'n':
                                                        menuOrExit()  #option for menu or exit
                                                except (ValueError, EOFError, TypeError) as error:  #handles any input errors the user may have / makes sure the correct data is inputted.
                                                    pass  #reloops until no exceptions

                                except (ValueError, EOFError, TypeError) as error:  #handles any input errors the user may have / makes sure the correct data is inputted.
                                    print(error)  #prints the error code that occurs
                                    pass  #reloops until no exceptions

                except (TypeError, EOFError, ValueError) as error:  #handles any input errors the user may have / makes sure the correct data is inputted.
                    print(error)  #prints the error code
                    pass  #reloops until no exceptions

        elif len(bookList) <= i:
            print(f'{bookToQuery} does not exist in list or is out of stock')  #output if title input meets input criteria but doesn't exist in the list
            queryBook()  #recalls function to try again
def orderByTitleGenre():
    print('-------------------------Option 6-------------------------')
    while True: #Loops until the code on the block has been executed
        try:
            titleOrGenre = int(input('Would you like to sort list by 1. Title 2. Genre ')) #input for the titleOrGenre Coice
            if titleOrGenre >= 1 <= 2: #only executes if the conditions are met
                if titleOrGenre == 1:
                    sortedTitleList = sorted(bookList, key= lambda i: i[2]) #Sorts the main list into a new temp list by title of book
                    for book in sortedTitleList:
                        print(f'{book[1]} \nAuthor: {book[0]} \nFormat: {book[2]} \nPublisher:{book[3]} \nCost: {book[4]} \nStock:'
                            f'{book[5]} \nGenre: {book[6]}\n\n', 57 * '-')
                    menuOrExit()
                elif titleOrGenre == 2:
                    sortedGenreList = sorted(bookList, key=lambda i: i[6]) #Sorts the main list into a new temp list by genre of book
                    for book in sortedGenreList:
                        print(f'{book[1]} \nAuthor: {book[0]} \nFormat: {book[2]} \nPublisher:{book[3]} \nCost: {book[4]} \nStock:'
                             f'{book[5]} \nGenre: {book[6]}\n\n', 57 * '-')
                    menuOrExit()
        except (TypeError, EOFError, ValueError) as error:
            pass

def chartGenres():
    genreDict = {}
    for i in range(len(bookList)):      #Code to get the dict keys and values from the bookList genres
        genre = bookList[i]
        if genre[6] in genreDict:
            genreDict[genre[6]] = genreDict[genre[6]] + 1 * int(genre[5])
        else:
            genreDict[genre[6]] = 1 * int(genre[5])
    plt.bar(genreDict.keys(), genreDict.values(), align='center') #plots the bar chart from the values gathered by the above code
    plt.show()  #shows the bar chart

    menuOrExit()

def menu():
    while True:
        try:
            choice = int(input('--------------------Stock Management---------------------\n'     # prints choice for user menu
                               ' 1. Currently Stocked Books \n 2. Average Price of Books\n 3. Genre Report \
                                \n 4. Add New Book \n 5. Query Book \n 6. Order By Title Or Genre \n 7. Genre Bar Chart \n 8. Exit'
                               '\n----------------------------------------------------------\n\n'))  # Menu + menu options
            if choice == 1:
                getBooks()
                break
            elif choice == 2:
                getAverage()
                break
            elif choice == 3:
                getGenreReport()
                break
            elif choice == 4:
                addNewBook()
                break
            elif choice == 5:
                queryBook()
                break
            elif choice == 6:
                orderByTitleGenre()
                break
            elif choice == 7:
                chartGenres()
                break
            elif choice == 8:
                exit()
        except(TypeError, EOFError, ValueError):
            pass

def main():
    try:
        with open('book_data.txt', 'r') as fileData:
            for line in fileData:
                if not line.startswith('#'): #Ignores any comments included in the data file
                    innerList = [i.strip() for i in line.split(',')] #Strips unnescary characters from each line and splits each item by comma into a list
                    bookList.append(innerList) #Appends the inner list to a list of lists
    except (IOError, EOFError) as error:
        print(error)
        exit()
    menu()

main()# calls the main function