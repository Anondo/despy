def getBinary(content):
    return "".join([bin(int(bit , 16))[2:].zfill(4) for bit in content])
def getHexa(content):
    hexa = hex(int(content , 2))
    return hexa[2:len(hexa)-1]

def makeHalf(content):
    return content[:(len(content)/2)] , content[(len(content)/2):]

def getTable(tableName):
    import os
    script_dir = os.path.dirname(__file__)
    rel_path = "tables/" + tableName + ".txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    return [map(int , line.split()) for line in open(abs_file_path , 'r').readlines()]

def applyTable(content , tableName):
    ipTable = getTable(tableName)
    flatIpTable = [item for sublist in ipTable for item in sublist]

    ipApplied = "".join([content[term-1] for term in flatIpTable])
    return ipApplied

def getShiftTable():
    return {
          1 : 1,
          2 : 1,
          3 : 2,
          4 : 2,
          5 : 2,
          6 : 2,
          7 : 2,
          8 : 2,
          9 : 1,
         10 : 2,
         11 : 2,
         12 : 2,
         13 : 2,
         14 : 2,
         15 : 2,
         16 : 1,
    }

def leftShift(content , index):
    from collections import deque
    inverseContent = list(content[::-1])
    dl = deque(inverseContent)
    dl.rotate(getShiftTable()[index])
    return "".join(list(dl)[::-1])

def applySBox(content , box_no):
    sTable = getTable("s"+str(box_no))
    value = sTable[int(content[0] + content[len(content)-1] , 2)][int(content[1:len(content)-1] , 2)]
    return bin(value)[2:].zfill(4)

def f(rContent , content):

     ERn = applyTable(rContent , 'ebit')
     ern_bin = ERn
     ERn = int(ERn , 2)
     Kn = int(content , 2)
     xorResult = bin(Kn ^ ERn)[2:].zfill(48)
     sbox_result = ""
     upto = 0
     i = 0
     while(i < 8):
         sbox_result += applySBox(xorResult[upto:upto+6] , i+1)
         upto += 6
         i += 1
     finalResult = applyTable(sbox_result , 'p')
     return ern_bin , xorResult , sbox_result , finalResult
