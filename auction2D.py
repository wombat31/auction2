''' An auction company has an interactive auction board at their sales rooms, which
allows buyers to place bids at any time during the auction. Before the auction starts, the sellers
place their items in the sale room with a unique number attached to each item (item number).
The following details about each item need to be set up on the interactive auction board system:
item number, number of bids, description and reserve price. The number of bids is initially set to zero.

During the auction, buyers can look at the items in the sale room and then place a bid on the interactive
auction board at the sale room. Each buyer is given a unique number for identification (buyer number).
All the buyer needs to do is enter their buyer number, the item number and their bid. Their bid must be greater than any existing bids.

At the end of the auction, the company checks all the items and marks those that have bids greater than the reserve as sold. Any items sold will incur a fee of 10% of the final bid to be pad to the auction company. 

Write and test a program of programs for the auction company. 

- Your program or programs must include appropriate prompts for the entry of data, data must be validated on entry. 
- Error messages and other input need to be set out clearly and understandably. 
- All variables, constants and other identifiers must have meaningful names. 

You will have to complete these three tasks. Each must be fully tested. 

Task 1 - Auction set up. 

For every item in the auction the item number, description and the reserve price should be recorded. The number of bids is set to zero. There must be at least 10 items in the auction. 

Task 2 - Buyer bids. 

A buyer should be able to find an item and view the item number, description and the current highest bid. A buyer can then enter their buyer number and bid, which must be higher than any previously recorded bids. Every time a bid is recorded the number of bids for that item is increased by one. Buyers can bid for an item many times and they can bid for many items. 

Task 3 - At the end of the auction. 

Using the results from Task 2, identify items that have reached their reserve price, mark them as sold, calculate 10% of the final bid as the auction company fee and add this to the total fee for all sold items. Display this total fee. Display the item number and final bid for all the items with bids that have not reached their reserve price. Display the item number of any items that have received no bids. Display the number of items sold, the number of items that did not meet the reserve price and the number of items with no bids. 

'''

#DECLARE VARIABLES
#I intend to use a 2D array to store items
# e.g. auctionItems = [[itemNumber,"Description",reservePrice,noBids],[itemNumber,"Description",reservePrice,noBids]]

auctionItems =[]
counter = 0
numberAuctionItems = int(input("How many items are in the Auction?"))

while counter < numberAuctionItems:
    #create item array
    
    itemArray = []
    #input the individual item details
    itemNumber = counter
    itemDescription = input("Please input the description :")
    itemReserve = float(input("Please input the item Reserve Price :"))
    itemBids = 0
    itemArray.append('{:0>3}'.format(counter))
    itemArray.append(itemDescription)
    itemArray.append(itemReserve)
    itemArray.append(itemBids)
    #append the individual item to the 2D array
    auctionItems.append(itemArray)
    print(auctionItems)
    counter+=1