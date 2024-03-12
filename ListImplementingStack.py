def size(list):
    count=0
    for item in list:
        count+=1
    return count

stack=[]
stackHistory=[]
print("Operations : Push, Pop, Top, End")
while True:
    operation = input("Operation: ")
    if operation.lower() == 'end':
        break
    elif operation.lower() == 'push':
        push=input("PUSH : ")
        stack.append(push)
        stackHistory.append(f"Pushed : {push}")
    elif operation.lower() == 'pop':
        if size(stack)==0:
            stackHistory.append("Pop Request")
            print("Invalid Request: The stack is empty!")
        else:
            print(f"{stack[size(stack)-1]} popped!")
            stackHistory.append(f"Popped : {stack[size(stack) - 1]}")
            stack.remove(stack[size(stack)-1])
    elif operation.lower() == 'top':
        if size(stack) == 0:
            stackHistory.append(f"Access Request : Top")
            print("Invalid Request: The stack is empty!")
        else:
            stackHistory.append(f"Access Request : Top")
            print(f"Top : {stack[size(stack) - 1]}")

print("\n-----------STACK HISTORY-----------")
for event in stackHistory:
    print(event)
print("-----------------------------------")

