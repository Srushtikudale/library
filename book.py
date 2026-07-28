n=int(input("enter a number of member"))
borrow=[]
for i in range (n):
     book=int(input("book borowed by member"+str(i+1)))
     borrow.append(book)
     total=sum(borrow)
     average=total/n
     print("average",average)
     print("highest",max(borrow))
     print("lowest",min(borrow))
     zero=0
     for i in borrow:
      if i==0:
          zero+=1
          print("member with no books",zero)
          mode=borrow[0]
          max.count=0
          for i in borrow:
           count=borrow.count(i)
          max.count=count
          mode=i
          print("mode",mode)