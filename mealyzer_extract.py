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

with open('mealyzer25.csv','wb') as f:
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

with open('mealyzer58.csv','wb') as f:
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

with open('mealyzer57.csv','wb') as f:
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

with open('mealyzer56.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(mealyzer)

######################################

###### all breakfast for patient 25
with open ('mealyzer25.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "breakfast":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('25_breakfast.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)


###### all breakfast for patient 58
with open ('mealyzer58.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "breakfast":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('58_breakfast.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all breakfast for patient 57

with open ('mealyzer57.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "breakfast":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('57_breakfast.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all breakfast for patient 56
with open ('mealyzer56.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "breakfast":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('56_breakfast.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)




######################################

###### all lunch for patient 25
with open ('mealyzer25.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "lunch":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('25_lunch.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

###### all lunch for patient 58
with open ('mealyzer58.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "lunch":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('58_lunch.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all lunch for patient 57

with open ('mealyzer57.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "lunch":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('57_lunch.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all lunch for patient 56
with open ('mealyzer56.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "lunch":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('56_lunch.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)



######################################

###### all dinner for patient 25
with open ('mealyzer25.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "dinner":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('25_dinner.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)


###### all dinner for patient 58
with open ('mealyzer58.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "dinner":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('58_dinner.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all dinner for patient 57

with open ('mealyzer57.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "dinner":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('57_dinner.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all dinner for patient 56
with open ('mealyzer56.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "dinner":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('56_dinner.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)


######################################
###### all dinner for patient 58
with open ('mealyzer58.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "dinner":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('58_dinner.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all dinner for patient 57

with open ('mealyzer57.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "dinner":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('57_dinner.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all dinner for patient 56
with open ('mealyzer56.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "dinner":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('56_dinner.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)


######################################
###### all after_dinner_snack for patient 58
with open ('mealyzer58.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "after_dinner_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('58_dinner_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all after_dinner_snack for patient 57

with open ('mealyzer57.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "after_dinner_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('57_dinner_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all after_dinner_snack for patient 56
with open ('mealyzer56.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "after_dinner_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('56_dinner_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)



######################################
###### all afternoon_snack for patient 58
with open ('mealyzer58.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "afternoon_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('58_after_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all afternoon_snack for patient 57

with open ('mealyzer57.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "afternoon_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('57_after_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all afternoon_snack for patient 56
with open ('mealyzer56.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "afternoon_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('56_after_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)


######################################
###### all morning_snack for patient 58
with open ('mealyzer58.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "morning_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('58_morn_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all morning_snack for patient 57

with open ('mealyzer57.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "morning_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('57_morn_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)

##### all morning_snack for patient 56
with open ('mealyzer56.csv','r') as f:
    reader = csv.reader(f)
    meals = [header]
    for line in reader:
        if line[2] == "morning_snack":
            id = line[0]
            link = 'https://github.com/mlhwang/mealyzer/blob/master/meals/%s/original/pic.jpg' % id
            line.append(link)
            meals.append(line)

with open ('56_morn_sn.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(meals)





