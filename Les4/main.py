def getUnion(list1, list2):
    return sorted(list1 + list2)

def getDifference(list1, list2):
    return sorted(list(set(list1) - set(list2)))

def getIntersection(list1, list2):
    return sorted(list(set(list1) & set(list2)))

def readFileToArray(filename):
    file = open(filename,'r')
    str = file.read()
    file.close()
    return str.split(', ')

def writeArrayToFile(filename, array):
    file = open(filename,'w')
    file.write(", ".join(array))



list1 = readFileToArray('input1.txt')
list2 = readFileToArray('input2.txt')

writeArrayToFile('output_union.txt', getUnion(list1, list2))
writeArrayToFile('output_difference_1_2.txt', getDifference(list1, list2))
writeArrayToFile('output_difference_2_1.txt', getDifference(list2, list1))
writeArrayToFile('output_intersection.txt', getIntersection(list1, list2))