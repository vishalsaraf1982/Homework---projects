print("WELCOME TO THE ATM" )
num=int(input("Enter your withdrawal amount in euros "))

note1=num//500
note2=(num%500)//200
note3=((num%500)%200)//100
note4=(((num%500)%200)%100)//50
note5=((((num%500)%200)%100)%50)//20
note6=(((((num%500)%200)%100)%50)%20)//10
note7=((((((num%500)%200)%100)%50)%20)%10)//5

print ("number of 500 euro notes ",note1)
print ("number of 200 euro notes ",note2)
print ("number of 100 euro notes ",note3)
print ("number of 50 euro notes ",note4)
print ("number of 20 euro notes ",note5)
print ("number of 10 euro notes ",note6)
print ("number of 5 euro notes ",note7)