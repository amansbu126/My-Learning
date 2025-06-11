import openpyxl

# Step 1: Read line from notepad file
with open("C:/Users/Aman Kumar/OneDrive/문서/New folder/product table.txt", "r") as file:
    line = file.readline()

# Step 2: Split and clean values
values = [item.strip() for item in line.split("|") if item.strip()]

# Step 3: Create Excel workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sheet1"

# Step 4: Write values to Excel row
for col, value in enumerate(values, start=1):
    ws.cell(row=1, column=col).value = value

# Step 5: Save to Excel
wb.save("C:/Users/Aman Kumar/OneDrive/문서/New folder/prodduct_table_ready.xlsx")

print("Excel file 'output.xlsx' created successfully.")
