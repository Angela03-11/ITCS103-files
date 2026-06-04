import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet["A1"] = "ID"
sheet["B1"] = "Name"
sheet["C1"] = "Room"
sheet["D1"] = "Date"
sheet["E1"] = "Start Time"
sheet["F1"] = "Duration (Hours)"
sheet["G1"] = "Total Cost"

workbook.save("Quejano_Database.xlsx")