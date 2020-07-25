def a(name):
    print('The List Of Names:',name)
    c=str(input('Enter The Search Name:'))
    for i in name:
        if i==c:
           print(i,'index is:',name.index(c))
           break
    else:
        print('Name Not Found')           
b=(['Raj','Mani','Ram','Priya','Hema'])
a(b)