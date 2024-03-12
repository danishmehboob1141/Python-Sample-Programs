def conv_Kelvin(temp_in_kelvin):
    celcius = temp_in_kelvin-273
    farenheit = (9/5)*(temp_in_kelvin-273.15)+32
    print(f"{temp_in_kelvin}K = {celcius}C = {farenheit}F")
def conv_celcius(temp_in_celcius):
    farenheit = (9/5)*(temp_in_celcius)+32
    kelvin = temp_in_celcius + 273.15
    print(f"{temp_in_celcius}C = {farenheit}F = {kelvin}K")
def conv_farenheit(temp_in_farenheit):
    kelvin = (5/9)*(temp_in_farenheit-32)+273.15
    celcius = (5/9)*(temp_in_farenheit-32)
    print(f"{temp_in_farenheit}F = {celcius}C = {kelvin}K")

print("Convert F ---- (1) \nConvert C ---- (2) \nConvert K ---- (3)")
choice = int(input("Enter your choice: "))
if choice == 1:     # F
    temp = float(input(f"Enter temperature in Farenheit:"))
    conv_farenheit(temp)
elif choice == 2:   # C
    temp = float(input(f"Enter temperature in Celcius:"))
    conv_celcius(temp)
elif choice == 3:  # K
    temp = float(input(f"Enter temperature in Kelvin:"))
    conv_Kelvin(temp)
else:
    print("Choice Not Present!")


