def menu():
    
    print("Make a choice - write 1 to 3: ")
    MENU = (
    'Check your current balance',
    'Withdraw',
    'Deposit'
    )
    
    for i, choice in enumerate(MENU, start=1):
        print(f"{i}.  {choice}")
        
    

menu()