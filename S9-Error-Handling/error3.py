while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you!')
    finally:
        print('ok, i am finally done')
    print('Csn you hear me?')