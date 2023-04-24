def do_fizzbuzz(num:int):
    """
    fizzbuzz: print fizz buzz fizzbuzz
    multiple 3: fizz
    multiple 5: buzz
    multiple 15: fizzbuzz
    etc: num
    """
    for i in range(1,num+1):
        if i%3==0:
            print('fizz')
        else:
            print(f'{i}')


if __name__=='__main__':
    do_fizzbuzz(16)
