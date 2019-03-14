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

print("TO END THE AUCTION AT ANY TIME - TYPE (-1)")

while auctionRunning:
    
    print(auctionItems)
    #Print out the auction items

    toBidOn = int(input("Which item number would you like to bid on?"))
    if toBidOn != -1:
        #Question which item to bid on
        print("How much would you like to bid for the" , auctionItems[toBidOn-1][1] , "? ")
        print("The current highest bid is :$",auctionItems[toBidOn-1][4])
        bid = float(input("How much would you like to bid?"))
        #Test if new bid is greater than the current bid
        if bid > auctionItems[toBidOn-1][4]:
            #if the bid is greater than the current bid accept bid and swap the current bid value.
            tempBidID = int(input(print("Your bid is acceptable, what is your bidder identification number?")))
            auctionItems[toBidOn-1][4] = bid
            #Append all bidder details to auctionItems ie. [001,"Charles"]
            #THIS PART DEALS WITH FIRST ASSIGNMENT OF BIDDER DETAILS TO AUCTIONITEMSARRAY
            #It tests the length of the auction Items array
            #If it is 5 in length, it means a bid has not been placed on the item 
            #as it does not have an appended bidder within auctionItems
            if len(auctionItems[toBidOn-1]) == 5:
                auctionItems[toBidOn-1].append(bidderDetails[tempBidID-1])
                #No of bids is stored in the 3rd index of the auctionItems array.
                print("DELETE ME:The current number of bids is before first assignment", auctionItems[toBidOn-1][3])
            
                auctionItems[toBidOn-1][3] += 1

                print("DELETE ME:The current number of bids is after first assignment", auctionItems[toBidOn-1][3])
            #THIS PART DEALS WITH SECOND AND FURTHER ASSIGNMENTS OF BIDDER DETAILS TO AUCTIONITEMSARRAY
            #i.e. if a bidder is already appended to auctionItems, it will replace the bidder should the bid
            #be higher
            else:
                print("Im in the swap part")
                auctionItems[toBidOn-1][5] = (bidderDetails[tempBidID-1])
                ######NEED TO INCREASE THE ITEM BIDS +1#########
                #No of bids is stored in the 3rd index of the auctionItems array.
                print("DELETE ME:The current number of bids is before further assignment", auctionItems[toBidOn-1][3])
            
                auctionItems[toBidOn-1][3] += 1

                print("DELETE ME:The current number of bids is after further assignment", auctionItems[toBidOn-1][3])

        else:
            print("Your bid must be higher than the current highest bid")
    else:
        print("THAT IS IT FOR TODAY FOLKS - NOW TO WORK OUT THE NUMBERS")
        auctionRunning = False

#########TASK 3###########
#Search through arrays and mark items as sold
#To do this, I will append a further indexed item within the auction items
#It will be a boolean - True or False

print("WE ARE NOW READY FOR TASK 3")
for i in range(len(auctionItems)):
    if auctionItems[i][2] > auctionItems[i][4]:
        auctionItems[i].append(False)
    else:
        auctionItems[i].append(True)

print(auctionItems)

#Search through arrays and if sold indicator is True
#append 10% of the sold price to the auctionItems array

for i in range(len(auctionItems)):
    if auctionItems[i][6] == True:
        auctionItems[i].append(auctionItems[i][4]*.1)

print(auctionItems)