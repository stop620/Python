def loadValue(addr): #해당 주소안의 값을 리턴함
    if memory[int(addr, 2)] != '':
        return memory[int(addr, 2)]

def storeValue(addr, DR_value): #주소 안에 값을 저장함
    #if (memory[int(addr, 2)] == '') or (memory[int(addr, 2)] == '0000'):
    memory[int(addr, 2)] = DR_value

def push(value): #스택에 추가
    stack.append(value)

def pop(): #스택에서 반환
    value = stack.pop()
    return value

memory = [''] * 16
stack = []
DR = ''

read_path = 'C:/PythonStudy/code2.bi' #파일 경로

text = open(read_path, 'r') #파일 읽기
lines = text.readlines()
line = text.readline()

for line in lines:
    line = line.replace(',', ' ')
    line_token = []
    line_token = line.split() #tokenize
  
    print(line_token)
    opcode = line_token[0]
    if len(line_token) == 2:
        opr = line_token[1]

    if opcode == '0000': # [0000] LOAD num
        DR = opr

    elif opcode == '0001': # [0001] LOAD [addr]
        temp = loadValue(opr)
        DR = temp

    elif opcode == '0010': # [0010] STORE [addr]
        storeValue(opr, DR)

    elif opcode == '0011': # [0011] PUSH num
        push(opr)

    elif opcode == '0100': # [0100] PUSH 
        push(DR)

    elif opcode == '0101': # [0101] POP
        DR = pop()

    elif opcode == '0110': # [0110] ADD
        temp = pop()
        result = format((int(temp, 2) + int(DR, 2)), 'b').zfill(4)
        push(result)

    elif opcode == '0111': # [0111] SUB
        temp = pop()
        result = format((int(temp, 2) - int(DR, 2)), 'b').zfill(4)
        push(result)

    elif opcode == '1000': # [1000] WRITE
        temp = pop()
        storeValue(opr, temp)
        push(temp)

    elif opcode == '1001': # [1001] PRINT
        print('RESULT: ',memory[int(opr, 2)])
    
    #print('memory>>', memory)
    #print('stack>>', stack)
    #print('After DR>> '+DR+'\n')
print('END')
text.close #파일 닫기