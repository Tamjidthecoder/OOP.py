class employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructor called")
    
def create_obj():
    print("obj created")
    obj=employee()
    print("function ...end")
    return obj
obj=create_obj()
print('program..end')