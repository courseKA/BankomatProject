data = {'Kalin': 123, 'Ivan': 456 }
balance = {'Kalin': 500, 'Ivan': 4500 }

def check_name_pin():
    name = input('Enter your name: ')
    if name in data.keys():
        print('Your name is accepted')

        print('Your balance is:', balance[name])
    else:
        print('Wrong name')
        quit()

    for i in range(3):
        pin_input = int(input('Enter your pin: '))
        pin1 = int(data[name])
        if pin1 == pin_input:
            print('Login Successful')
            import menu

            while True:
                try:
                    choice = int(input('Enter your choice:'))

                    if choice == 1:
                        print('Your balance is: ', balance[name])
                        break
                    elif choice == 2:
                        withdraw_sum = int(input('Please write withdraw sum: '))
                        balance1 = balance[name] - withdraw_sum
                        print('Your current balance is: ', balance1 )
                        break
                    elif choice == 3:
                        deposit_sum = int(input('Please write deposit_sum: '))
                        balance2 = balance[name] + deposit_sum
                        print('Your current balance is: ', balance2 )                                    
                        break

                    else:
                        print('Wrong choice. Try again. Thank you for banking with us!')
                        break                 
                except:
                    print('Wrong input. Try again')  
                    break                        
            break
        elif pin_input != pin1:
            print('Wrong pin code.')
            i += 1

        else:
            print('Pin code not accepted')
            quit()
                
check_name_pin()
