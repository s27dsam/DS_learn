def menu():
    print('[1] compound interest')
    print('[2] market cap')
    print('[3] ROI')
    print('[4] Cash Flow ')
    print('[5] Leverage ratio using income')
    print('[0] exit the program.')

menu()
option = int(input('Enter the number of the program you wish to use: '))

while option != 0:
    if option == 1:
        print('number of years of saving?')
        years = int(input('Enter years: '))
        print('what is your current balance?')
        principal = float(input('Enter current balance: '))
        print('what is your monthly investment?')
        m_invest = float(input('Enter amount: '))
        print('what is the yearly interest rate of the investment?')
        interest = float(input('Enter interest (10% = 0.1): '))

        print(' ')

        m_invest = m_invest * 12
        final_amount = 0

        for i in range(0, years):
            if final_amount == 0:
                final_amount = principal

            final_amount = (final_amount + m_invest) * (1 + interest)
        print(' ')

        print('your final amount is = ', final_amount)

    elif option == 2:
        print('Enter the total number of shares or tokens the company currently has')
        shares = int(input('number of shares/tokens: '))
        print('Enter the current share/token price of the company to at least one decimal place')
        price = float(input('share/token price: '))
        m_cap = shares * price

        print(' ')

        print('The market cap is', m_cap)

    elif option == 3:
        print('Enter the total net return of your investment')
        net = float(input('total net return: '))
        print('Enter the total cost of the investment')
        cost = float(input('Enter total cost: '))
        roi = (net/cost)*100
        print('Your ROI is', roi, 'percent')
    elif option == 4:
        print('Enter your total income')
        incomes = int(input('Income: '))
        print('Enter your total expenses')
        expenses = float(input('Expenses: '))
        cash_flow = incomes - expenses
        print(' ')
        print('your cash flow is', cash_flow)
    elif option == 5:
        print('Enter your total debt payments')
        debt = int(input('Enter debt payments: '))
        print('Enter your your income')
        income = int(input('Income: '))
        ratio = debt/income
        print(' ')
        print('your leverage ratio is', ratio)
    else:
        print('error')

    print()
    menu()
    option = int(input('Enter the number of the program you wish to use: '))


















