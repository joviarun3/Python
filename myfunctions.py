class multiplefunctions():
    def Subfields():
        list=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics',  'Speech Processing', 'Natural Language Processing']
        print("Sub-fields in AI are:") 
        for i in list:
            print (i)

    def OddEven():
        num1=int(input("Enter a number:"))
        if num1%2==0:
            print(num1,"is Even number")
        else:
            print(num1,"is Odd number")

    def Eligible():
        Gen=input("Your Gender:")
        age=int(input("Your Age:"))
        if Gen == "Male" and age>=21:
            print("ELIGIBLE")
        elif Gen == "Female" and age>=18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        Total = sub1+sub2+sub3+sub4+sub5
        print("Total : ",sub1+sub2+sub3+sub4+sub5)
        print("Percentage : ",((Total / 500) * 100))


    def triangle():
        h=int(input("Height:"))
        b=int(input("breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=(h*b)/2
        print("Area of Triangle:",area)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",h1+h2+b1)
