import openpyxl as op 

workbook = op.Workbook()
sheet = workbook.active

sheet["A1"] = "ID"
sheet["B1"] = "First Name"
sheet["C1"] = "Last Name"
sheet["D1"] = "Birth Year"
sheet["E1"] = "Age"

for gela in range(1, 4):
    print("\nList your favorite people")
    print(f"Person {gela}")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    birth = int(input("Enter birth year: "))
    
    age = 2026 - birth

    sheet[f"A{gela+1}"] = gela
    sheet[f"B{gela+1}"] = fname
    sheet[f"C{gela+1}"] = lname
    sheet[f"D{gela+1}"] = birth
    sheet[f"E{gela+1}"] = age
    
workbook.save("favorite_people.xlsx")

print("\nFavorite people saved successfully!")

print("\n======FAVORITE PEOPLE LIST======")

for row in sheet.iter_rows(values_only=True):
    print(row)


    

    