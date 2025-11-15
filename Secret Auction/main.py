from art import logo
print(logo + "\n\n")
auction_entry = {}
while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    auction_entry[name] = bid
    if input("Are there more bids? (yes/no): ").lower() == "no":
        break
    print("\n" * 100)
if auction_entry:
    winner = max(auction_entry, key=auction_entry.get)
    print(f"\nThe winner is {winner} with a bid of ${auction_entry[winner]}")
else:
    print("\nNo bids were placed.")