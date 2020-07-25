# Search the name from the list of names
- **Write a function that searches a list of names (unsorted) for the names.**
- **And Print the location in the list.** 
- **If is not in the List, print Name Not Found**
## Sample Code For Search the name from the list of names
```
print('The List Of Names:',name)
c=str(input('Enter The Search Name:'))
for i in name:
   if i==c:
       print(i,'index is:',name.index(c))
       break
else:
   print('Name Not Found') 
```
## Example Output For Search the name from the list of names
```
The List Of Names: ['Raj', 'Mani', 'Ram', 'Priya', 'Hema']
Enter The Search Name:Priya
Priya index is: 3
```
