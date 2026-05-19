tasks =[]
while True:
    task = input("Enter your tasks:")
    tasks.append(task)
    
    choice = input("add more yes/no:")
    
    if choice=="yes":
        tasks.append(task)
  
    else:
        print("complete remaining tasks")
        break
    if task not in tasks:
        tasks.append(task)
    else:
        tasks.remove(task)
print("Total Tasks are:",tasks)