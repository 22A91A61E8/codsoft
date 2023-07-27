import random
lower="abcdeMNOPQRSTUVWXYZfghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="~!@#$%^&*()"
numbers="1234567890"
string=lower+upper+symbols+numbers
length=10
password="".join(random.sample(string,length))
print("your new password is:"+password)
                 
