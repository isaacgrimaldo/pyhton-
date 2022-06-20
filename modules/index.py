
def getInfo(message):
    data = input(message)
    
    while len(data) - 1 < 0 :
        print('insert again the info')
        data = input(message)

    return data;        