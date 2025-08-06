def bubble_sort():
    n=int(input("Enter how many numbers: "))
    nums=[]
    temp=0
    for i in range(n):
        value=int(input(f"Enter value{i+1} : "))
        nums.append(value)
    print("Original list: ",nums)
    for i in range(n):
        for j in range(0, n - i - 1):  # The element at index 0 to n-i-1 is compared with its very next. 
            if nums[j]<nums[j+1]:      #if smaller it is moved to the next index.Or they are swaped.
                temp=nums[j+1]         #This process pushes the larger nos to the front.
                nums[j+1]=nums[j]      #Thereby sorting the nums in descending order.
                nums[j]=temp
    print("Descending order: ",nums)
    
bubble_sort()
