class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.isempty:
            
          return self.stack.pop()

    def peek(self):
        if self.isempty:
            return None
        return self.stack[-1]

    def isempty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

class Browser:
    def __init__(self):
        self.current_page = None
        self.back_stack = Stack()
        self.forward_stack = Stack()

    def visit(self,url):
        if self.current_page is not None:
            self.back_stack.push(self.current_page)

        self.current_page = url

        while not self.forward_stack.isempty():
            self.forward_stack.pop()

        print("current page:", self.current_page)

    def back(self):
        if self.back_stack.isempty():
            print("no previous page availble")
        else:
            self.forward_stack.push(self.current_page)
            self.current_page=self.back_stack.pop()

        print("Navigated back.")
        self.show_current_page()

    def forward(self):
        if self.forward_stack.isempty():
            print("no forward page availble")
        else:
            self.back_stack.push(self.current_page)
            self.current_page=self.forward_stack.pop()

        print("Navigated forward.")
        self.show_current_page()

    def show_current_page(self):
        if self.current_page is None:
            print("no page is currently open.")
        else:
            print("current page :",self.current_page)


browser=Browser()

choice =""
while choice !=5:
    print("1. Visit a webpage")
    print("2. Back")
    print("3. Forward")
    print("4. Show current page")
    print("5. Exit")

    choice = input ("Choice:")

    if choice =="1":
        url = input("Enter URL :")
        browser.visit(url)
        print("----------------------------------------")

    elif choice =="2":
        browser.back()
        print("----------------------------------------")
    elif choice =="3":
        browser.forward()
        print("----------------------------------------")

    elif choice =="4":
        browser.show_current_page()
        print("----------------------------------------")

    elif choice =="5":
        print("Exit")
        print("----------------------------------------")

    else:
        print("wrong choice")