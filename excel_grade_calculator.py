import openpyxl

# Loading the Excel workbook
workbook = openpyxl.load_workbook("./student_grades.xlsx")
sheet = workbook["grades"]

# Writing the header for the average calculation column
sheet.cell(row=1, column=4, value="average")

total_rows = sheet.max_row

# Iterating through rows to calculate the weighted average
for row in range(2, total_rows + 1):
    midterm = sheet.cell(row=row, column=2).value
    final = sheet.cell(row=row, column=3).value
    
    if midterm is not None and final is not None:
        average = (midterm * 0.4) + (final * 0.6)
        sheet.cell(row=row, column=4, value=average)

# Exporting into updated file name
workbook.save("./student_grades_updated.xlsx")
print("Excel grade automation completed successfully! Clean data saved.")

# Keeping the terminal open until the user presses Enter
input("\nProcess finished! Press Enter to close this window...")

