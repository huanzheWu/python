#! /usr/bin/python
def test_for():

    words = ['a','b','c','d']
    for word in words:
        print(word)

    str = "this is a string for test"
    for let in str :
        print(let)

    sum = 0
    for inter in list(range(100)):
        sum += inter
    print(sum)
    

def test_while():
    i = 0
    sum = 0
    while i<100 :
        sum += i 
        i+=1
    print(sum)
    
def test_break():
    i = 0 
    while i < 10: 
        if i == 5: 
            break
        print(i)
        i+= 1

def test_continue():
    i = 0
    while i <10:
        if i == 5:
            continue
        print(i)
        i+=1


def test_loop_else():
    for i in list(range(10)):
        for j in list(range(5)):
            if i == 3: 
                break
            
        else:
            print("in this loop ,i is ",i)


def test_pass():
    pass 

test_loop_else()

#test_break()
#test_continue()
#test_for()
#test_while()
    

