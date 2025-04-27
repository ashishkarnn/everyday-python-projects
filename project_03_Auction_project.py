print("""
                         ___________
                                  /
                          )_______(
                          |\"\"\"\"\"\"\"|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )\"\"\"\"\"\"\"(
                         /_________\\
                       .-------------.
                      /_______________\\
""")


bids = {}

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: "))
    bids[name] = bid

    more = input("Are there other bidders? Type 'yes' or 'no': ").lower()
    if more == "no":
        break

# Find the highest bidder
highest_bid = max(bids, key=bids.get)
print(f"The winner is {highest_bid} with a bid of ${bids[highest_bid]}")
