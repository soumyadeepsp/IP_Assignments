def getComboPrice(p1, p2, p3, comb1, comb2, comb3):
	comboPrice1 = (p1+p2)*(1-comb1)
	comboPrice2 = (p1+p3)*(1-comb2)
	comboPrice3 = (p2+p3)*(1-comb3)
	return [comboPrice1, comboPrice2, comboPrice3]

p1 = float(input("Enter the price per pack of the first item: "))
p2 = float(input("Enter the price per pack of the second item: "))
p3 = float(input("Enter the price per pack of the third item: "))
print ("----------------------------")
print ("----------------------------")
print ("Discount Details")
superComboPrice = (p1+p2+p3)*(1-0.28)
comb1 = float(input("Enter the discount for the 1st saver combo(Items 1 and 2): "))/100
comb2 = float(input("Enter the discount for the 2nd saver combo(Items 1 and 3): "))/100
comb3 = float(input("Enter the discount for the 3rd saver combo(Items 2 and 3): "))/100
print ("----------------------------")
mob = input("Provide your 10-digit contact number: ")
print ("----------------------------")
print()
comboPrice = getComboPrice(p1, p2, p3, comb1, comb2, comb3)
print ("The resulting cataloge is:")
print ("----------------------------")
print ("----------------------------")
print ("Delhi Days")
print ("R-Block, Model Town 3")
print ("Delhi: 110009")
print ("----------------------------")
print ("----------------------------")
print ("Item 			Price(per Pack)")
print ("| 				|")
print ("Item1 			", p1)
print ("Item2 			", p2)
print ("Item3 			", p3)
print ("ComboPack1 		", comboPrice[0])
print ("ComboPack2 		", comboPrice[1])
print ("ComboPack3 		", comboPrice[2])
print ("SuperSaver 		", superComboPrice)
print ("----------------------------")
print ("----------------------------")
print ("For home delivery, contact here:", mob)