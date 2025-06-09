def getDepBase(prompt):
    while True:
        try:
            dep_base = float(input(prompt))
            if dep_base > 0:
                return dep_base
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a number.")

def getSalvageValue(prompt):
    while True:
        try:
            salvage_value = float(input(prompt))
            if salvage_value >= 0:
                return salvage_value
            else:
                print("Salvage value cannot be negative.")
        except ValueError:
            print("Please enter a number.")

def getUsefulLife(prompt):
    while True:
        try:
            useful_life = int(input(prompt))
            if useful_life > 0:
                return useful_life
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a number.")

def getMonth(prompt):
    while True:
        try:
            month = int(input(prompt))
            if month >= 1 and month <= 12:
                return month
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Please enter a number.")

def getFactor(prompt):
    while True:
        try:
            factor = float(input(prompt))
            if factor > 1:
                return factor
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Please enter a number.")

def askContinue(prompt):
    while True:
        selector = input(prompt)
        if selector.upper() == "Y":
            break
        elif selector.upper() == "N":
            running = False
        else:
            print("Please enter Y or N.")



running = True
while running == True:
    keycode = input("Welcome to the Depreciator!\nEnter 1 for straight line\n2 for declining balance\n3 for sum of the years' digits ")
    if keycode == "1":
        dep_base = getDepBase("Type in your asset's depreciation base. Remember to subtract the salvage value! ")
        salvage_value = getSalvageValue("Type in your asset's salvage value. ")
        useful_life = getUsefulLife("Type in your asset's useful life. ")
        month = getMonth("Type in the number of the month in which you started depreciating the asset. ")
        dep_amount = dep_base / useful_life
        dep_amount = float(dep_amount)
        basis = dep_base + salvage_value
        acc_dep = float(0)
        counter = 0
        while counter < useful_life + 1:
            counter += 1
            if month == 1 and counter > useful_life:
                break
            if counter == 1:
                acc_dep += dep_amount * (12 - month + 1)/12
            elif counter == useful_life + 1:
                acc_dep += dep_amount * ((month - 1)/12)
            else:
                acc_dep += dep_amount
            book_value = basis - acc_dep
            print(f"Year {counter}: Accumulated depreciation = {acc_dep:.2f}, book value = {book_value:.2f}, depreciation/year = {dep_amount:.2f}")
        askContinue("Do you want to continue? Y/N ")
    elif keycode == "2":
        dep_base = getDepBase("Type in your asset's depreciation base. Include the salvage value. ")
        salvage_value = getSalvageValue("Type which portion is allocated to salvage value. ")
        useful_life = getUsefulLife("Type in your asset's useful life. ")
        month = getMonth("Type in the number of the month in which you started depreciating the asset. ")
        factor = getFactor("Type the factor by which you'd like to multiply the declining balance. ")
        book_value = dep_base
        acc_dep = float(0)
        for year in range(1,useful_life + 2):
            if month == 1 and year > useful_life:
                break
            dep_amount = (book_value / useful_life * factor)
            if year == 1:
                dep_amount *= (12 - month + 1)/12
            if year == useful_life + 1:
                dep_amount *= ((month - 1)/12)
            if (book_value - dep_amount) < salvage_value:
                dep_amount = book_value - salvage_value
            acc_dep += dep_amount
            book_value -= dep_amount
            if book_value < salvage_value:
                book_value = salvage_value
            print(f"Year {year}: Accumulated depreciation = {acc_dep:.2f}, book value = {book_value:.2f}, depreciation/year = {dep_amount:.2f}")
            if book_value == salvage_value:
                break
            askContinue("Do you want to continue? Y/N ")
    elif keycode == "3":
        dep_base = getDepBase("Type in your asset's depreciation base. Remember to subtract the salvage value! ")
        salvage_value = getSalvageValue("Type in your asset's salvage value. ")
        useful_life = getUsefulLife("Type in your asset's useful life. ")
        month = getMonth("Type in the number of the month in which you started depreciating the asset. ")
        denominator = useful_life * (useful_life + 1)/2
        basis = dep_base + salvage_value
        counter = 0
        acc_dep = float(0)
        dep_amounts = [0]
        for year in range(1, useful_life + 1):
            dep_amount = dep_base * ((useful_life - (year - 1)) / denominator)
            dep_amounts.append(dep_amount)
        while counter < useful_life + 1:
            counter += 1
            if month == 1 and counter > useful_life:
                break
            if counter == 1:
                new_dep = dep_amounts[1] * (12 - month + 1)/12
                acc_dep += new_dep
            elif counter == useful_life + 1:
                new_dep = dep_amounts[useful_life] * ((month - 1)/12)
                acc_dep += new_dep
            else:
                new_dep = (dep_amounts[counter - 1] * ((month - 1)/12) + (dep_amounts[counter] * (12 - month + 1)/12))
                acc_dep += new_dep
            book_value = basis - acc_dep
            print(f"Year {counter}: Accumulated depreciation = {acc_dep:.2f}, book value = {book_value:.2f}, depreciation/year = {new_dep:.2f}")
        askContinue("Do you want to continue? Y/N ")
    else:
        print("Please enter 1, 2, or 3. ")
