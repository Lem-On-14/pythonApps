
if __name__ == '__main__':
    result = ''
    for i in range(1,10):
        for j in range(1,10):

            timesValue = '{:0=2}'.format(i * j)

            if 1 <= j < 9:
                result = result + timesValue + ' '

            if i == 9 and j == 9:
                result = result +  timesValue
            elif i < 9 and j == 9:
                 result = result +  timesValue + '\n'
    print(result)