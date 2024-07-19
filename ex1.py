one_biriyani=100
one_dhosa=30
one_idly=10
menus=["biriyani","dhosa","idly"]

your_order=input("enter your order:")

if your_order in menus:
    print(f"yes {your_order} is available")
    quantity=int(input(f"how many {your_order} you want:"))
    if your_order=="biriyani":
        total=one_biriyani*quantity
        if total>=1000:
            offer_total=total-200
            print(f"you are eating more than 1000 rupees so offer 200 final bill is {offer_total}")
        else:
            print(f"your total bill is {total}")
       
    elif your_order=="dhosa":
        total=one_dhosa*quantity
        if total>=1000:
            offer_total=total-200
            print(f"you are eating more than 1000 rupees so offer 200 final bill is {offer_total}")
        else:
            print(f"your total bill is {total}")
    elif your_order=="idly":
        total=one_idly*quantity
        if total>=1000:
            offer_total=total-200
            print(f"you are eating more than 1000 rupees so offer 200 final bill is {offer_total}")
        else:
            print(f"your total bill is {total}")
        
else:
    print(f"sorry {your_order} is not available")