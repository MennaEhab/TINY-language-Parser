from enum import Enum
def is_symbol(c):
    if c == '+' or c == '-' or c == '*' or c == '/' or c == '=' or\
            c == '<' or c == '>' or c == '(' or c == ')' or c == ';' or c == ':':
        return True
    return False


class STATE (Enum):
    START = 0
    INNUM = 1
    INID = 2
    SYMBOL = 3
    DONE = 4
    COMMENT = 5


class token:
    tokenValue: str
    tokenType: str

    def __init__(self):
        self.tokenType = " "
        self.tokenValue = " "

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def set_Token(self,type,value):
        self.tokenValue=value
        self.tokenType=type


    def print_token(self):
        #print(self.tokenType+' , '+self.tokenValue)
        return self.tokenType + " , " + self.tokenValue


input_file = open("F:\\compilers\\input.txt", "r")
output_file = open("F:\\compilers\\output.txt", "w+")
temp = input_file.read(1)
temp1: str
while 1:
    if not temp:
        break
    state = STATE.START
    currentToken = token()
    while state != STATE.DONE:
        if state == STATE.START:
            if temp.isdigit():
                currentToken.tokenType = "number"
                currentToken.tokenValue += temp
                state = STATE.INNUM

            elif temp.isalpha():
                currentToken.tokenType = "identifier"
                currentToken.tokenValue += temp
                state = STATE.INID

            elif is_symbol(temp):
                currentToken.tokenType = "symbol"
                currentToken.tokenValue += temp
                state = STATE.SYMBOL

            elif temp == '{':
                state = STATE.COMMENT

        elif state == STATE.INNUM:
            if temp.isdigit():
                currentToken.tokenValue += temp
                state = STATE.INNUM
            else:
                state = STATE.DONE
                temp1 = temp

        elif state == STATE.INID:
            if temp.isalpha() or temp.isdigit():
                currentToken.tokenValue += temp
                state = STATE.INID
            else:
                temp1 = temp
                state = STATE.DONE

        elif state == STATE.SYMBOL:
            if temp == "=":
                currentToken.tokenValue += temp
                temp = input_file.read(1)
            state = STATE.DONE
            temp1 = temp

        elif state == STATE.COMMENT:
            if temp == '}':
                state = STATE.START

        if state != STATE.DONE:
            temp = input_file.read(1)
        else:
            temp = temp1

    output_file.write(currentToken.tokenType)
    output_file.write(" ,")
    output_file.write(currentToken.tokenValue+'\n')

output_file.close()



