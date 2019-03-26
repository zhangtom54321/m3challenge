import xlrd
print("Here")
import matplotlib.pyplot as plt


def getPercentages(filename, gradeIndex, smokeIndex, vapeIndex):
    loc = (filename)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    smokeCount = 0
    vapeCount = 0

    for row in range(1, sheet.nrows):
        #print(sheet.row_values(row))
        if sheet.row_values(row)[gradeIndex] != '' and sheet.row_values(row)[gradeIndex] != '*' and int(sheet.row_values(row)[gradeIndex]) >= 4 and int(sheet.row_values(row)[gradeIndex]) <= 7:
            if sheet.row_values(row)[smokeIndex] != '' and sheet.row_values(row)[smokeIndex] != '*' and int(sheet.row_values(row)[smokeIndex]) == 1:
                smokeCount+=1
            if sheet.row_values(row)[vapeIndex] != '' and sheet.row_values(row)[vapeIndex] != '*' and int(sheet.row_values(row)[vapeIndex]) == 1:
                vapeCount+=1
    #print(str(float(smokeCount)/sheet.nrows) + " " + str(float(vapeCount)/sheet.nrows))
    return float(smokeCount)/sheet.nrows, float(vapeCount)/sheet.nrows

print("Here")
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017]
smokeArr = []
vapeArr = []

# 2011
smoke, vape = getPercentages("./2011.xlsx", 9, 17, 95)
smokeArr.append(smoke)
vapeArr.append(vape)

# 2012
smoke, vape = getPercentages("./2012.xlsx", 9, 17, 103)
smokeArr.append(smoke)
vapeArr.append(vape)

# 2013
smoke, vape = getPercentages("./2013.xlsx", 9, 23, 110)
smokeArr.append(smoke)
vapeArr.append(vape)

# 2014
smoke, vape = getPercentages("./2014.xlsx", 9, 21, 45)
smokeArr.append(smoke)
vapeArr.append(vape)

# 2015
smoke, vape = getPercentages("./2015.xlsx", 11, 22, 44)
smokeArr.append(smoke)
vapeArr.append(vape)

# 2016
smoke, vape = getPercentages("./2016.xlsx", 12, 24, 43)
smokeArr.append(smoke)
vapeArr.append(vape)

# 2017
smoke, vape = getPercentages("./2017.xlsx", 13, 25, 46)
smokeArr.append(smoke)
vapeArr.append(vape)

print("Here")
plt.plot(years, smokeArr, 'ro', label='Smoke')
plt.plot(years, vapeArr, label='Vape')
plt.xlabel('Year')
plt.ylabel('Percentage of High School Students Who Use Product')
plt.show()
