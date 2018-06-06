
n = 16
all_list = range(n+1)[1:]
list1 = [x for x in all_list if (x%7==1) or (x%7==2) ]
list2 = [x for x in all_list if (x%7==3) or (x%7==4) ]
list3 = [x for x in all_list if (x%7==5) or (x%7==6) ]
list4 = [x for x in all_list if (x%7==7)  ]

print list1, list2, list3, list4