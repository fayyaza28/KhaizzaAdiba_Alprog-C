# komparasi (true false)
# > < >= <= == != is is-not
x = 25
y = 83

print ("========== lebih dari (>)")
hasil = x > 83
print (x, ">" , 83, "=", hasil)


print ("========== lebih dari (>)")
hasil = 25 > y
print (25, ">", y, "=", hasil)


print ("========== kurang dari (<)")
hasil = y < 25
print (y, "<", 25, "=", hasil)
         
print ("========== kurang dari (<)")
hasil = 25 < y 
print (25, "<", y, "=", hasil)


print ("========== lebih dari sama dengan (>=)")
hasil = x >= 83
print (x, ">=", 83, "=", hasil)
  
  
print ("========== kurang dari sama dengan (<=)")
hasil = y <= 25
print(y, "<=", 25, "=", hasil)

print ("========= sama dangan sama dengan (==)")
hasil = x == 83
print (x, "==", 83, "=", hasil)

print ("========== tidak sama dengan (!=)")
hasil = y != 25
print(y, "!=", 25, "=", hasil)

print ("========== is (is)")
hasil = x is 83
print(x, "is", 83, "=", hasil)

print ("========== is-not (is not)")
hasil = 25 is not y
print(25, "is-not", y, "is not", hasil)

