running = True
while running == True:
    keycode = input("Welcome to the Depreciator!\nEnter 1 for straight line\n2 for declining balance\n3 for sum of the years' digits ")
    if keycode == "1":
        while running == True:
            dep_base = float(input("Type in your asset's depreciation base or X to exit. Remember to subtract the salvage value! "))
            if dep_base <= 0:
                dep_base = 1
            salvage_value = float(input("Type in your asset's salvage value. "))
            if salvage_value < 0:
                salvage_value = 0
            useful_life = int(input("Type in your asset's useful life. "))
            if useful_life <= 0:
                useful_life = 1
            month = int(input("Type in the number of the month in which you started depreciating the asset. "))
            if month < 1:
                month = 1
            if month > 12:
                month = 12
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
                print(f"Year {counter}: Accumulated depreciation = {acc_dep:.2f}, book value = {book_value:.2f}")
            selector = input("Do you want to continue? Y/N ")
            if selector.upper() == "Y":
                pass
            elif selector.upper() == "N":
                running = False
    elif keycode == "2":
        while running == True:
            dep_base = float(input("Type in your asset's depreciation base. Include the salvage value. "))
            if dep_base <= 0:
                dep_base = 1
            salvage_value = float(input("Type which portion is allocated to salvage value. "))
            if salvage_value < 0:
                salvage_value = 0
            useful_life = int(input("Type in your asset's useful life. "))
            if useful_life <= 0:
                useful_life = 0
            month = int(input("Type in the number of the month in which you started depreciating the asset. "))
            if month < 1:
                month = 1
            if month > 12:
                month = 12
            factor = float(input("Type the factor by which you'd like to multiply the declining balance. "))
            if factor <= 1:
                factor = 2
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
                print(f"Year {year}: Accumulated depreciation = {acc_dep:.2f}, book value = {book_value:.2f}")
                if book_value == salvage_value:
                    break
            selector = input("Do you want to continue? Y/N ")
            if selector.upper() == "Y":
                pass
            elif selector.upper() == "N":
                running = False
    elif keycode == "3":
        while running == True:
            dep_base = float(input("Type in your asset's depreciation base. Remember to subtract the salvage value! "))
            if dep_base <= 0:
                dep_base = 1
            salvage_value = float(input("Type in your asset's salvage value. "))
            if salvage_value < 0:
                salvage_value = 0
            useful_life = int(input("Type in your asset's useful life. "))
            if useful_life <= 0:
                useful_life = 1
            month = int(input("Type in the number of the month in which you started depreciating the asset. "))
            if month < 1:
                month = 1
            if month > 12:
                month = 12
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
                    acc_dep += dep_amounts[1] * (12 - month + 1)/12
                elif counter == useful_life + 1:
                    acc_dep += dep_amounts[useful_life] * ((month - 1)/12)
                else:
                    acc_dep += (dep_amounts[counter - 1] * ((month - 1)/12) + (dep_amounts[counter] * (12 - month + 1)/12))
                book_value = basis - acc_dep
                print(f"Year {counter}: Accumulated depreciation = {acc_dep:.2f}, book value = {book_value:.2f}")
            selector = input("Do you want to continue? Y/N ")
            if selector.upper() == "Y":
                pass
            elif selector.upper() == "N":
                running = False
    else:
        print("Please enter 1, 2, or 3. ")
