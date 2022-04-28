#LIST

#List creation
print("\nCreate List :- ")
li_st = ["list",1,2.2,True]
print(li_st)
li_st_con = list("Use constructor")
print(li_st_con)

#Access List
print("\nAccessing list and slice :- ","\n",li_st[0],"\n",    li_st[-1],"\n",  li_st[0:3],"\n",   li_st[0:],"\n",   li_st[:-1],"\n")
print("Access Through for loop : ")
for i in li_st:
   print(i)


#Comprehension :-
print("\nComprehension Loops List :- ")
# n_list = [ x for x in li_st if "i" in x] #int can't iterable only list,tuple,set
# print(n_list)


#Change list :-
print("\nChange Or Update list :- ")
change_list = ["Second List", 1, 2.2, True]
change_list[0] = "THIS" 
print("\nUpdate List Value : ",change_list)


#Add value :-
print("\nAdding Value in list :- ")
change_list.insert(0, "insert value")
sec_list = ["second list"]
change_list.append(sec_list)           #Append use to add item at last we can use any iterable
li_st.extend(change_list)
print(change_list, "\n", li_st)


#Remove value :-
print("\nRemove Value From List :- ")
change_list.pop(2)      #Without index remove from last
change_list.remove(2.2) #Remove element with specific value
print(change_list)


#Copy list :-
print("\nCopy list :- ")
cp_list = change_list.copy()
print("\nCopy List :",cp_list)


#Sort list :-
print("\nSorting list value :- ")
SortList = [10,2,4,5,3]
SortList.sort()
print("Sorted List :",SortList)
SortList.sort(reverse=True)
revList = SortList.reverse()
print("Sorted List In Reverse :",revList)


#Find elements in list :-
print("\nFind elements in list :- ")
xc = SortList.count(10)
print("Return 1 if item availabel :",xc)
xc = SortList.index(10)
print("Return index no where find :",xc)


#Clearlist :-
change_list.clear()
print("Clear eniter list",change_list)


#del list completly
del change_list #after print genrate error
