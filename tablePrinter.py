tableData = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol', 'David'], ['dogs', 'cats','moose','goose']]

def printTable():
    colWidths = [0]* len(tableData)
    one = []
    two = []
    three = []


    for i in range(len(tableData)):
        colWidths[i] = tableData[i]
        place = tableData[i]
        for x in range(len(tableData[i])):
            spot = colWidths
            if len(one) < len(place):
                one.append(colWidths[i][x])
            elif len(two) < len(place):
                two.append(colWidths[i][x])
            elif len(three) < len(place):
                three.append(colWidths[i][x])

    for i in range(len(one)):
        print((one[i]+'  ' +two[i]+ '  ' +three[i]).center(20,))


printTable()