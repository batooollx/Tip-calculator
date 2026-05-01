print("welcome to the tip calculater!")#
bill=float(input("what was the total bill?"))
tip=int(input("how much tip would you like to give? 10,12 or 15?"))
people=int(input("how many people to spilt the bills?"))
perecntage_tip=tip  /100 
totaltip=bill * perecntage_tip
totalbill=totaltip+bill
billper=totalbill / bill
final=round(billper, 2)
print(f"each person shoild pay $ {final}")