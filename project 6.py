s1=int(input("Enter first side of triangle"))
s2=int(input("Enter second side of triangle"))
s3=int(input("Enter third side of triangle"))
if (s1==s2) and (s2==s3):
    print("Equilateral triangle")
elif (s1==s2) and (s1!=s3) or (s2==s3) and (s2!=s1) or (s3==s1) and (s3!=s2):
    print("Isosceles triangle")
elif s1!=s2 and s2!=s3 and s3!=s1:
    print("Scalence triangle")