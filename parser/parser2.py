import scanner
import os
from graphviz import Digraph
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
Tree = Digraph('G', filename='syntaxTree.gv')

input_file = open("F:\compilers\parserInput", "r")

currentToken = scanner.token()
count ='1'
def get_token():
    temp = input_file.readline()
    if temp:
        WholeToken = temp.split()
        currentToken.set_Token(WholeToken[0], WholeToken[2])


def match(expectedToken,prevCount):
    global count
    currentCount = count
    if expectedToken == "number" or expectedToken == "identifier":
        if expectedToken == currentToken.tokenType:
            Tree.node(currentCount, currentToken.print_token())
            count = count + '1'
            Tree.edge(prevCount, currentCount)
            get_token()
            return True
    else:
        if expectedToken == currentToken.tokenValue:
            Tree.node(currentCount, currentToken.print_token())
            count = count + '1'
            Tree.edge(prevCount, currentCount)
            get_token()
            return True
    return False



def program():
    global count
    currentCount = count
    Tree.node(currentCount,"program")
    count = count+'1'
    stmt_sequence(currentCount)


def stmt_sequence(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "stmt_sequence")
    count = count + '1'
    Tree.edge(prevCount,currentCount)
    statement(currentCount)
    while currentToken.tokenValue == ";":
        match(";",currentCount)
        statement(currentCount)


def statement(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "statement")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    if currentToken.tokenType == "identifier":
        assign_stmt(currentCount)
    elif currentToken.tokenValue == "if":
        if_stmt(currentCount)
    elif currentToken.tokenValue == "repeat":
        repeat_stmt(currentCount)


def if_stmt(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "if_stmt")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    match("if",currentCount)
    match("(",currentCount)
    exp(currentCount)
    match(")",currentCount)
    match("then",currentCount)
    stmt_sequence(currentCount)
    if currentToken.tokenValue == "else":
        match("else",currentCount)
        stmt_sequence(currentCount)
    end_stmt(currentCount)


def repeat_stmt(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "repeat_stmt")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    match("repeat",currentCount)
    stmt_sequence(currentCount)
    match("until",currentCount)
    exp(currentCount)


def end_stmt(prevCount):
    match("end",prevCount)


def assign_stmt(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "assign_stmt")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    match("identifier",currentCount)
    match("*=",currentCount)
    simple_exp(currentCount)


def exp(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "exp")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    simple_exp(currentCount)
    compare_op(currentCount)
    simple_exp(currentCount)


def compare_op(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "compare_op")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    if currentToken.tokenValue ==  "<":
        match("<",currentCount)
    elif currentToken.tokenValue == ">":
        match(">",currentCount)
    elif currentToken.tokenValue == "=":
        match("=",currentCount)


def simple_exp(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "simple_exp")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    term(currentCount)
    while currentToken.tokenValue == "+" or currentToken.tokenValue == "-":
        ADD(currentCount)
        term(currentCount)


def term(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "term")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    factor(currentCount)
    while currentToken.tokenValue == "*" or currentToken.tokenValue == "/":
        MUL(currentCount)
        factor(currentCount)


def factor(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "factor")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    if currentToken.tokenValue =="(":
        match("(",currentCount)
        exp(currentCount)
        match(")",currentCount)
    elif currentToken.tokenType == "identifier":
        match("identifier",currentCount)
    else:
        match("number",currentCount)


def ADD(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "ADD")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    if currentToken.tokenValue =="+":
        match("+",currentCount)
    else:
        match("-",currentCount)


def MUL(prevCount):
    global count
    currentCount = count
    Tree.node(currentCount, "MUL")
    count = count + '1'
    Tree.edge(prevCount, currentCount)
    if currentToken.tokenValue =="*":
        match("*",currentCount)
    else:
        match("/",currentCount)




get_token()
program()
Tree.view()