### KONVERSI SUHU 
### SOAL 4


#Celcius ke suhu lain
print("\n"+"celcius ke suhu lain".center(40,"="))
suhu = int(input("masukkan suhu dalam celcius : ")) 

reamur = (4/5) * suhu
fahrenheit = (9/5) * suhu + 32
kelvin = suhu + 273

print(f"{suhu}\u00B0C = {fahrenheit:.1f}\u00B0F")
print(f"{suhu}\u00B0C = {reamur:.1f}\u00B0R")
print(f"{suhu}\u00B0C = {kelvin:.1f} K")


#reamur ke suhu lain
print("\n"+"reamur ke suhu lain".center(40,"="))

suhu = int(input("masukkan suhu dalam reamur : "))

celcius = (5/4) * suhu
fahrenheit = (9/4) * suhu + 32
kelvin = (5/4) * suhu + 273

print(f"{suhu}\u00B0R = {fahrenheit:.1f}\u00B0F")
print(f"{suhu}\u00B0R = {celcius:.1f}\u00B0C")
print(f"{suhu}\u00B0R = {kelvin:.1f} K")


#fahrenheit ke suhu lain
print("\n"+"fahrenheit ke suhu lain".center(40,"="))

suhu = int(input("masukkan suhu dalam fahrenheit : "))

celcius = (5/9) * (suhu - 32)
reamur = (4/9) * (suhu - 32)
kelvin = celcius + 273

print(f"{suhu}\u00B0F = {reamur:.1f}\u00B0R")
print(f"{suhu}\u00B0F = {celcius:.1f}\u00B0C")
print(f"{suhu}\u00B0F = {kelvin:.1f} K")


#kelvin ke suhu lain
print("\n"+"kelvin ke suhu lain".center(40,"="))

suhu = int(input("masukkan suhu dalam kelvin : "))

celcius = suhu - 273
reamur = (4/5) * (suhu - 273)
fahrenheit = (9/5) * celcius + 32

print(f"{suhu} K = {reamur:.1f}\u00B0R")
print(f"{suhu} K = {celcius:.1f}\u00B0C")
print(f"{suhu} K = {fahrenheit:.1f}\u00B0F")







