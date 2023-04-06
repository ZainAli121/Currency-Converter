with open('data.txt') as f:
  lines = f.readlines()

currencyDict = {}
for line in lines:
  parsed = line.split("\t")
  currencyDict[parsed[0]] = parsed[2]

amount = int(input("Enter the amount in Pkr:\n"))
print(
  "Enter the name of the currency you want to convert this amount to? Available Options:\n"
)
[print(item) for item in currencyDict.keys()]
currency = input("Please Enter one of these Currencies: \n")
print("===================================================")
print("---------------------------------------------------")
print(
  f"{amount} Pkr is equal to {amount /float(currencyDict[currency])} {currency}"
)
print("===================================================")
print("---------------------------------------------------")