#Edwin Zheng
#SoftDev CW1 -- Class Names (Prints first and last names of Period 1 and 2)

pd1 = ["Zheng, Edwin", "Zhang, Angela", "Zheng, Reng"]
pd2 = ["Creative, Name","Doe, John","Smith, John"]

pd_num = input("What period?")
name_index = input("What index? (0 base)")
pd_num = int(pd_num)
name_index = int(name_index)
if pd_num == 1:
    print (pd1[name_index])
if pd_num == 2:
    print (pd2[name_index])
