#Self Assessment Questions

# The first bug that I spotted was on line 10, it was missing a colon at the end of the line. I got it from the traceback when I ran the script as it was the first time. It tells me about my current debugging instincts that I first look at how the code runs and where it crashes before I get to fixing things.
# apply_discount(price, tier) function is used to apply a different discount depending on the tier of the customer. The input would be the tier or membership of the customer and the output would be the specific discount that is given to said customer. Most likely, a colleague would be able to use the code without having to understand indepth what exactly is happening.
#AI was used to check for mistakes and any possible errors in the code.At first, I was a bit confused on where the error was, but when it explained exactly why I messed up where I did, there was no need for me to ask it to fix it and I managed to figure it out on my own after the advice.

#DExericse 1
def calculate_tax(price, rate):
    return price * rate

tax1= calculate_tax(100, 0.07)
tax2= calculate_tax(250, 0.08)

print(f"tax for $100 at 7% is: ${tax1:.2f}")
print(f"tax for $250 at 8% is: ${tax2:.2f}")
print(f"Tax for $350 at 5% is: ${calculate_tax(350, 0.05):.2f}")

#Exercise 2
def apply_discount(price, tier):
    if tier =="gold":
        return price *0.85
    elif tier =="silver":
        return price *0.90
    elif tier =="bronze":
        return price *0.95
    else:
        return price


#Calling function with different tiers 

original_price= 200

for tier in ["gold", "silver", "bronze", "none"]:
        print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3
def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount

#Calling the final_price function
print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

#Exercise 4
orders= [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate=0.07
for price, tier in orders:
    total= final_price(price, tier, rate)
    print(f"Price: ${price} | Tier: {tier} | Final Price: ${total:.2f}")

#Exercise 6

x=100 #global x

def double_it():
    x=999 #local x
    return x *2

print(x)
print(double_it())
print(x)