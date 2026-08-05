client_portfolio = {}
def portfolio_analytics_repot(client_portfolio):
    while True:
        client = input("Enter the client name ('done' for exit): ")
        if client == 'done':
            break
        else:
            value = int(input("Enter the client revenue: "))
            client_portfolio[client] = value
        
    largest = max(client_portfolio.values())
    average = sum(client_portfolio.values()) / len(client_portfolio)
    total = sum(client_portfolio.values())

    print("  --- PORTFOLIO ANALYTICS REPORT ---  ")
    print("Total Portfolio Value: ", total)
    print("Average Contract Value: ", average)
    print("Highest Contract Value: ", largest)

    print("  --- CLIENT ROSTER ---  ")

    for client, value in client_portfolio.items():
        if value > 10000:
            print("Client : ", client, "| Revenue : ", value, "VIP Tier!")
        else:
            print("Client : ", client, "| Revenue : ", value)   

portfolio_analytics_repot(client_portfolio)
