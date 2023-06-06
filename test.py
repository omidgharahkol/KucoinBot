while True:
    with open("file.txt") as file_in:
        lines = []
        for line in file_in:
            if line == 'EndSpread':
                break
            else:
                symbol , target_price = line.strip('\n').split(',')
                print(symbol,target_price)






file_to_delete = open("file.txt",'w')
file_to_delete.close()