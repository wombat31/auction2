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
#Extending the array for task 2, the highest bid and bidder details will also be appended along with the auction item descriptions
# e.g. auctionsItems = [[itemNumber, "Description", reservePrice, noBids, currentBid,[bidderDetails]]......[etc]]

auctionItems =[]
bidderDetails = []
counter = 0
bidderCounter = 0
numberAuctionItems = int(input("How many items are in the Auction?"))
auctionRunning = True

while counter < numberAuctionItems:
    #create item array
    
    itemArray = []
    #input the individual item details
    itemNumber = counter
    itemDescription = input("Please input the description of item number:" + ('{:0>3}'.format(counter + 1)) + "")
    itemReserve = float(input("Please input the item Reserve Price :"))
    itemBids = 0
    currentBid = 0 #added for task 2
    itemArray.append('{:0>3}'.format(counter + 1))
    itemArray.append(itemDescription)
    itemArray.append(itemReserve)
    itemArray.append(itemBids)
    itemArray.append(currentBid) #added for task 2
    #append the individual item to the 2D array
    auctionItems.append(itemArray)
    print(auctionItems)
    counter+=1

#Task 2
#I intend to use a 2D array to store the bidder details
numberOfBidders = int(input("How many bidders are at the auction today?"))
while bidderCounter < numberOfBidders:
    bidderArray = []
    bidderName = input("Please enter the name of bidder number "  + ('{:0>3}'.format(bidderCounter + 1)))
    bidderArray.append('{:0>3}'.format(bidderCounter + 1))
    bidderArray.append(bidderName)
    #append the individual bidder details to the 2D array
    bidderDetails.append(bidderArray)
    print(bidderDetails)
    bidderCounter +=1

#print out auction items and details
print("IT IS TIME TO COMMENCE THE AUCTION")
#print out the auction items.
print("Today we are delighted to offer for sale")
for i in range(len(auctionItems)):
    print(auctionItems[i])

while auctionRunning:
    
    toBidOn = int(input("Which item number would you like to bid on?"))
   
    print("How much would you like to bid for the" , auctionItems[toBidOn-1][1] , "? ")
    print("The current highest bid is :$",auctionItems[toBidOn-1][4])
    bid = float(input("How much would you like to bid?"))
    if bid > auctionItems[toBidOn-1][4]:
        tempBidID = int(input(print("Your bid is acceptable, what is your bidder identification number? : ")))
        auctionItems[toBidOn-1][4] = bid
        #Append all bidder details to auctionItems ie. [001,"Charles"]
        if len(auctionItems)== 4:
            auctionItems.append(bidderDetails[tempBidID-1])
        else:
            auctionItems.append(bidderDetails[tempBidID-1])

    else:
        print("Your bid must be higher than the current highest bid")
