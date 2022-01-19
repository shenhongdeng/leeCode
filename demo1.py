
'''
第一题，卡片问题
'''
def taskA(no = 9):
    remaingNumber = [2021 for i in range(10)]
    print()
    result = 1
    flag = True
    while(flag):
        tempList =splitNo(result)
        for i in tempList:
            if remaingNumber[i] >= 1:
                remaingNumber[i] -= 1
            else:
                print(result)
                flag = False
                break
        result += 1


def splitNo(number):
    tempList = []
    while number != 0:
        tempList.append(number % 10)
        number = int(number / 10)
    return tempList

taskA(3)
