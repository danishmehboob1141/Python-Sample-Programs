def conv_Slug(weight_in_slug):      # 1 slug = 14.6 kg
    kg = weight_in_slug * 14.594
    gm = kg * 1000
    newton = kg / 10
    print(f"{weight_in_slug}slug = {kg}kg = {gm}gm = {newton}N")
def conv_kg(weight_in_kg):
    gm=weight_in_kg*1000
    slug=weight_in_kg/14.6
    newton=weight_in_kg/10
    print(f"{weight_in_kg}kg = {newton}N = {gm}gm = {slug}slug")
def conv_newton(weight_in_newton):
    kg=weight_in_newton*10
    slug=kg/14.6
    gm=kg*1000
    print(f"{weight_in_newton}N = {kg}kg = {gm}gm = {slug}slug")
def conv_gm(weight_in_gm):
    kg=weight_in_gm/1000
    slug=kg/14.6
    newton=kg/10
    print(f"{weight_in_gm}gm = {kg}kg = {newton}N = {slug}slug")

print("kg, gm, slug, newton")
unit=input("Enter measuring unit you want to enter weight in:")
if unit == 'slug':
    weight = float(input(f"Enter Weight in {unit}: "))
    conv_Slug(weight)
elif unit == 'kg':
    weight = float(input(f"Enter Weight in {unit}: "))
    conv_kg(weight)
elif unit == 'gm':
    weight = float(input(f"Enter Weight in {unit}: "))
    conv_gm(weight)
elif unit == 'newton':
    weight = float(input(f"Enter Weight in {unit}: "))
    conv_newton(weight)


