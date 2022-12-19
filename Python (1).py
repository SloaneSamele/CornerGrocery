import re
import string


def Menu():
    print("1: A List of items purchased and the Number of purchases")
    print("2: Displays the number of times a certain item was purchased")
    print("3: Produces a histogram Text file with a representation of the number of times purchased")
    print("4: Exit")
/*Creates a list of items purchased with the number of times purchased
  Example:
  Potatoes 4
  Pumpkins 5
  Onions 3
*/
def Itemized_list():
    
    f = ("project_three_input_file.txt","r")
    products = f.read().split()
    f.close()
    item_purchased = sort(set(products))
    
    for item in item_purchased:
        print(item,products.count(item))
// Creates a file Frequency.dat with the same format as ItemizedList

def histogram_list():
    f = ("project_three_input_file.txt","r")
    products = f.read().split()
    f.close()

    item_purchased = sort(set(products))
   list = ""
    new_file = open("frequency.dat","w")
    for items in item_purchased:
        list = items + " " product.count(items)
        for x in product.count(items):
           list = list + "*"
        new_file.write(list)
    new_file.close()
/*Calculates frequency a item was purchase
  returns 0 if item was not purchase
*/
def frequency_of_Item(item):
   f = ("project_three_input_file.txt","r")
    products = f.read().split()
    item_purchased = set(products)
    f.close()

    total_purchases = len(products)
   if(item in item_purchased){
      return total_purchases /products.count(item)
   else
	return 0