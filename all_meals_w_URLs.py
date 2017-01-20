import csv
with open('diabetes_meals.csv','r') as f:
	csv_reader = csv.reader(f)
	header = next(csv_reader)
header.append('Record_URL')

####### all data for patient 25
with open('diabetes_meals.csv','r') as file:
    file.readline()
    reader = csv.reader(file)
    mealyzer = [header]
    for line in reader:
        if int(line[1]) == 25:
             id = line[0]
             link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' %id
             line.append(link)
             mealyzer.append(line)

with open('25_all_meals.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(mealyzer)


####### all data for patient 58
with open('diabetes_meals.csv','r') as file:
    file.readline()
    reader = csv.reader(file)
    mealyzer = [header]
    for line in reader:
        if int(line[1]) == 58:
             id = line[0]
             link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' %id
             line.append(link)
             mealyzer.append(line)

with open('58_all_meals.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(mealyzer)



#### all data for patient 57
with open('diabetes_meals.csv','r') as file:
    file.readline()
    reader = csv.reader(file)
    mealyzer = [header]
    for line in reader:
        if int(line[1]) == 57:
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            mealyzer.append(line)

with open('57_all_meals.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(mealyzer)

##### all data for patient 56
with open('diabetes_meals.csv','r') as file:
    file.readline()
    reader = csv.reader(file)
    mealyzer = [header]
    for line in reader:
        if int(line[1]) == 56:
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            mealyzer.append(line)

with open('56_all_meals.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(mealyzer)