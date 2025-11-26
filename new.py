     def prime_number(self):
         for i in range(2,50):
             for j in range(2,i):
                 if i%j==0:
                     break
                 else:
                     print(i)

num=Numbers()
num.even_odd(10,20)
num.prime_numbers()