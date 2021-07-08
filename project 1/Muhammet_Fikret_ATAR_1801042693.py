import pandas as pd
from csv import DictReader

data = pd.read_csv("owid-covid-data.csv")
data.head()

file_object = open('output.txt', 'a')
##-------------------------------------------q1
file_object.write("q1-)")
file_object.write("\n")
file_object.write(str(len(data['location'].unique().tolist())))
file_object.write("\n")
##-------------------------------------------q2
file_object.write("q2-)")
file_object.write("\n")
minum=min(data['date'])
file_object.write(minum)
file_object.write("\n")
# iterate over each line as a ordered dictionary and print only few column by column name
with open('owid-covid-data.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
       if row['date']==minum:
                file_object.write(str(row['location']))
                file_object.write(str('\n'))
read_obj.close()
  
##-------------------------------------------q3
file_object.write("q3-)")
file_object.write("\n")  
data.total_cases=data.total_cases.fillna(0)
column_names = ["location", "total_cases"]
locations = data.location.to_list()
total_cases=data.total_cases.to_list()

loc_cases = zip(locations, total_cases)

q3_frame = {}
for t in loc_cases:
    if t[0] in q3_frame:
        q3_frame[t[0]] = q3_frame[t[0]]+t[1]
    else:
        q3_frame[t[0]] = t[1]

q3_18=q3_frame

for key,value in q3_frame.items():
    file_object.write('{} -> {}'.format(key, value))
    file_object.write("\n")              
##-------------------------------------------q4
file_object.write("q4-)")
file_object.write("\n")  
data.total_deaths=data.total_deaths.fillna(0)
column_names = ["location", "total deaths"]
locations = data.location.to_list()
total_deaths=data.total_deaths.to_list()

loc_cases = zip(locations, total_deaths)

q3_frame = {}
for t in loc_cases:
    if t[0] in q3_frame:
        q3_frame[t[0]] = q3_frame[t[0]]+t[1]
    else:
        q3_frame[t[0]] = t[1]
        
q4_18=q3_frame      

for key,value in q3_frame.items():
    file_object.write('{} -> {}'.format(key, value))
    file_object.write("\n")
##-------------------------------------------q5
file_object.write("q5-)")
file_object.write("\n")  
data.reproduction_rate=data.reproduction_rate.fillna(0)
reproduction_rate = data.reproduction_rate.to_list()

locationss = data.location.to_list()


d = {"location":locationss,"reproduction_rate":reproduction_rate}

dfa = pd.DataFrame(d)
def Average(lst):
    return sum(lst) / len(lst)


minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var().round(3) 

elementss=dfa.reproduction_rate.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()

res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
q18_mini=mini
q18_maxi=maxi
q18_averaGe2=averaGe2
q18_varioo=varioo

        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())  

##-------------------------------------------q6
file_object.write("\n")  
file_object.write("q6-)")
file_object.write("\n")  
data.icu_patients=data.icu_patients.fillna(0)
icu_patients = data.icu_patients.to_list()

locationss = data.location.to_list()


d = {"location":locationss,"icu_patients":icu_patients}

dfa = pd.DataFrame(d)

minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var().round(3) 

elementss=dfa.icu_patients.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()

q18_6mini=mini
q18_6maxi=maxi
q18_6averaGe2=averaGe2
q18_6varioo=varioo


res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())  


    

##-------------------------------------------q7
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q7-)")
file_object.write("\n")  
data.hosp_patients=data. hosp_patients.fillna(0)
hosp_patients = data.hosp_patients.to_list()

locationss = data.location.to_list()


d = {"location":locationss,"hosp_patients":hosp_patients}

dfa = pd.DataFrame(d)


minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var().round(3) 

elementss=dfa.hosp_patients.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()

q18_7mini=mini
q18_7maxi=maxi
q18_7averaGe2=averaGe2
q18_7varioo=varioo


res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())  
##-------------------------------------------q8
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q8-)")
file_object.write("\n")  
data.weekly_icu_admissions=data. weekly_icu_admissions.fillna(0)
weekly_icu_admissions = data.weekly_icu_admissions.to_list()

locationss = data.location.to_list()


d = {"location":locationss,"weekly_icu_admissions":weekly_icu_admissions}

dfa = pd.DataFrame(d)


minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var().round(3) 



elementss=dfa.weekly_icu_admissions.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()

q18_8mini=mini
q18_8maxi=maxi
q18_8averaGe2=averaGe2
q18_8varioo=varioo

res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())  
##-------------------------------------------q9
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q9-)")
file_object.write("\n")  
data.weekly_hosp_admissions=data. weekly_hosp_admissions.fillna(0)
weekly_hosp_admissions = data.weekly_hosp_admissions.to_list()

locationss = data.location.to_list()


d = {"location":locationss,"weekly_hosp_admissions":weekly_hosp_admissions}

dfa = pd.DataFrame(d)


minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var().round(3) 

elementss=dfa.weekly_hosp_admissions.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()

q18_9mini=mini
q18_9maxi=maxi
q18_9averaGe2=averaGe2
q18_9varioo=varioo


res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())
##-------------------------------------------q10
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q10-)")
file_object.write("\n")  
data.new_tests=data. new_tests.fillna(0)
new_tests = data.new_tests.to_list()

locationss = data.location.to_list()


d = {"location":locationss,"new_tests":new_tests}

dfa = pd.DataFrame(d)


minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var().round(3) 

elementss=dfa.new_tests.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()


q18_10mini=mini
q18_10maxi=maxi
q18_10averaGe2=averaGe2
q18_10varioo=varioo

res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())
##-------------------------------------------q11
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q11-)")
file_object.write("\n")  
data.total_tests=data.total_tests.fillna(0)
column_names = ["location", "total_tests"]
locations = data.location.to_list()
total_tests=data.total_tests.to_list()

loc_cases = zip(locations, total_tests)

q3_frame = {}
for t in loc_cases:
    if t[0] in q3_frame:
        q3_frame[t[0]] = q3_frame[t[0]]+t[1]
    else:
        q3_frame[t[0]] = t[1]

q11_18=q3_frame    

for key,value in q3_frame.items():
    file_object.write('{} -> {}'.format(key, value))
    file_object.write("\n")   
##-------------------------------------------q12
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q12-)")
file_object.write("\n")
data.positive_rate=data. positive_rate.fillna(0)
positive_rate = data.positive_rate.to_list()

locationss = data.location.to_list()


d = {"location":locationss,"positive_rate":positive_rate}

dfa = pd.DataFrame(d)


minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var().round(3) 

elementss=dfa.positive_rate.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()


q18_12mini=mini
q18_12maxi=maxi
q18_12averaGe2=averaGe2
q18_12varioo=varioo


res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())
##-------------------------------------------q13

file_object.write("\n")  
file_object.write("\n")  
file_object.write("q13-)")
file_object.write("\n")
data.tests_per_case=data. tests_per_case.fillna(0)
tests_per_case = data.tests_per_case.to_list()

locationss = data.location.to_list()

d = {"location":locationss,"tests_per_case":tests_per_case}

dfa = pd.DataFrame(d)

minmax = dfa.groupby("location").max()
minmax1 = dfa.groupby("location").min()
averaGe = dfa.groupby("location").mean().round(3) 
vario = dfa.groupby("location").var() 

elementss=dfa.tests_per_case.tolist()
# calculate mean
m = sum(elementss) / len(elementss)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in elementss) / len(elementss)

varioo=vario.values.tolist()
averaGe2=averaGe.values.tolist()
maxi=minmax.values.tolist()
mini=minmax1.values.tolist()
caountries=data.location.tolist()

q18_13mini=mini
q18_13maxi=maxi
q18_13averaGe2=averaGe2
q18_13varioo=varioo


res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"minimum":mini,"maximum":maxi,"average":averaGe2,"variation":varioo}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())
##-------------------------------------------q14
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q14-)")
file_object.write("\n")  
data.people_vaccinated=data.people_vaccinated.fillna(0)
column_names = ["location", "people_vaccinated"]
locations = data.location.to_list()
people_vaccinated=data.people_vaccinated.to_list()

loc_cases = zip(locations, people_vaccinated)

q3_frame = {}
for t in loc_cases:
    if t[0] in q3_frame:
        q3_frame[t[0]] = q3_frame[t[0]]+t[1]
    else:
        q3_frame[t[0]] = t[1]

q14_18=q3_frame 


for key,value in q3_frame.items():
    file_object.write('{} -> {}'.format(key, value))
    file_object.write("\n")   
##-------------------------------------------q15
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q15-)")
file_object.write("\n")  
data.people_fully_vaccinated=data.people_fully_vaccinated.fillna(0)
column_names = ["location", "people_fully_vaccinated"]
locations = data.location.to_list()
people_fully_vaccinated=data.people_fully_vaccinated.to_list()

loc_cases = zip(locations, people_fully_vaccinated)

q3_frame = {}
for t in loc_cases:
    if t[0] in q3_frame:
        q3_frame[t[0]] = q3_frame[t[0]]+t[1]
    else:
        q3_frame[t[0]] = t[1]

q15_18=q3_frame

for key,value in q3_frame.items():
    file_object.write('{} -> {}'.format(key, value))
    file_object.write("\n")   


##-------------------------------------------q16
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q16-)")
file_object.write("\n")  
data.total_vaccinations=data.total_vaccinations.fillna(0)
column_names = ["location", "total_vaccinations"]
locations = data.location.to_list()
total_vaccinations=data.total_vaccinations.to_list()

loc_cases = zip(locations, total_vaccinations)

q3_frame = {}
for t in loc_cases:
    if t[0] in q3_frame:
        q3_frame[t[0]] = q3_frame[t[0]]+t[1]
    else:
        q3_frame[t[0]] = t[1]

q16_18=q3_frame


for key,value in q3_frame.items():
    file_object.write('{} -> {}'.format(key, value))
    file_object.write("\n")   
##-------------------------------------------q17
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q17-)")
file_object.write("\n")


data.population=data. population.fillna(0)
population = data.population.to_list()

data.median_age=data. median_age.fillna(0)
median_age = data.median_age.to_list()

data.aged_65_older=data. aged_65_older.fillna(0)
aged_65_older = data.aged_65_older.to_list()

data.aged_70_older=data. aged_70_older.fillna(0)
aged_70_older = data.aged_70_older.to_list()

data.gdp_per_capita=data. gdp_per_capita.fillna(0)
gdp_per_capita = data.gdp_per_capita.to_list()

data.cardiovasc_death_rate=data. cardiovasc_death_rate.fillna(0)
cardiovasc_death_rate = data.cardiovasc_death_rate.to_list()

data.diabetes_prevalence=data. diabetes_prevalence.fillna(0)
diabetes_prevalence = data.diabetes_prevalence.to_list()

data.female_smokers=data. female_smokers.fillna(0)
female_smokers = data.female_smokers.to_list()


data.male_smokers=data. male_smokers.fillna(0)
male_smokers = data.male_smokers.to_list()

data.handwashing_facilities=data. handwashing_facilities.fillna(0)
handwashing_facilities = data.handwashing_facilities.to_list()

data.hospital_beds_per_thousand=data. hospital_beds_per_thousand.fillna(0)
hospital_beds_per_thousand = data.hospital_beds_per_thousand.to_list()

data.life_expectancy=data. life_expectancy.fillna(0)
life_expectancy = data.life_expectancy.to_list()

data.human_development_index=data. human_development_index.fillna(0)
human_development_index = data.human_development_index.to_list()



locationss = data.location.to_list()

d = {"location":locationss,"population":population}
dfa = pd.DataFrame(d)
minmax = dfa.groupby("location").max()

d2 = {"location":locationss,"median_age":median_age}
dfa2 = pd.DataFrame(d2)
median_age2 = dfa2.groupby("location").max()

d3 = {"location":locationss,"aged_65_older":aged_65_older}
dfa3 = pd.DataFrame(d3)
aged_65 = dfa3.groupby("location").max()

d4 = {"location":locationss,"aged_70_older":aged_70_older}
dfa4 = pd.DataFrame(d4)
aged_70 = dfa4.groupby("location").max()

d5 = {"location":locationss,"gdp_per_capita ":gdp_per_capita }
dfa5 = pd.DataFrame(d5)
gdp_per  = dfa2.groupby("location").max()

d6 = {"location":locationss,"cardiovasc_death_rate ":cardiovasc_death_rate  }
dfa6 = pd.DataFrame(d6)
cardiovasc_rate   = dfa6.groupby("location").max()

d7 = {"location":locationss,"diabetes_prevalence  ":diabetes_prevalence  }
dfa7 = pd.DataFrame(d7)
dia_prevalence   = dfa7.groupby("location").max()

d8 = {"location":locationss,"female_smokers  ":female_smokers  }
dfa8 = pd.DataFrame(d8)
female_smokers   = dfa8.groupby("location").max()

d9 = {"location":locationss,"male_smoker  ":male_smokers  }
dfa9 = pd.DataFrame(d9)
male_smoker   = dfa9.groupby("location").max()

d10 = {"location":locationss," handwashing_facilities   ": handwashing_facilities   }
dfa10 = pd.DataFrame(d10)
hand_facilities   = dfa10.groupby("location").max()

d11 = {"location":locationss,"hospital_beds_per_thousand  ":hospital_beds_per_thousand  }
dfa11 = pd.DataFrame(d11)
hospital_thousand   = dfa11.groupby("location").max()

d12 = {"location":locationss,"life_expectancy     ":life_expectancy     }
dfa12 = pd.DataFrame(d12)
life_expec      = dfa12.groupby("location").max()

d13 = {"location":locationss,"human_development_index  ":human_development_index  }
dfa13 = pd.DataFrame(d13)
human_development   = dfa13.groupby("location").max()

median_age2=median_age2.values.tolist()

aged_65=aged_65.values.tolist()

aged_70=aged_70.values.tolist()

gdp_per=gdp_per.values.tolist()

cardiovasc_rate=cardiovasc_rate.values.tolist()

dia_prevalence=dia_prevalence.values.tolist()

female_smoker=female_smokers.values.tolist()

male_smoker=male_smoker.values.tolist()

hand_facilities=hand_facilities.values.tolist()

hospital_thousand=hospital_thousand.values.tolist()

life_expec=life_expec.values.tolist()

human_development=human_development.values.tolist()



populations=minmax.values.tolist()

caountries=data.location.tolist()

res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
   
        
q5table = {"Country":res_caountries,"population":populations," median age": median_age2," # of people aged 65 older ":aged_65,"# of people aged 70 older":aged_70,"economic performance ":gdp_per,"death rates due to heart disease ":cardiovasc_rate,"diabetes prevalence ":dia_prevalence," # of female smokers ":female_smoker,
           "# of male smokers":male_smoker,"handwashing facilities ":hand_facilities," hospital beds per thousand people ":hospital_thousand," life expectancy ":life_expec,"human development index ":human_development}

q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())
##-------------------------------------------q18
file_object.write("\n")  
file_object.write("\n")  
file_object.write("q18-)")
file_object.write("\n")


data.tests_per_case=data. tests_per_case.fillna(0)


q3_frame_list = list(q3_18.values())
q4_frame_list = list(q4_18.values())
q11_frame_list = list(q11_18.values())
q14_frame_list = list(q14_18.values())
q15_frame_list = list(q15_18.values())
q16_frame_list = list(q16_18.values())


locationss = data.location.to_list()


caountries=data.location.tolist()

res_caountries = []
for i in caountries:
    if i not in res_caountries:
        res_caountries.append(i)
  

        
q5table = {"Country":res_caountries,"q#3":q3_frame_list, " q#4": q4_frame_list,"q#5 min": q18_mini,"q#5 max":q18_maxi,"q#5 avg":q18_averaGe2,"q#5 var":q18_varioo,
           "q#6 min":q18_6mini,"q#6 max":q18_6maxi,"q#6 avg":q18_6averaGe2,"q#6 var":q18_6varioo,
           "q#7 min":q18_7mini,"q#7 max":q18_7maxi,"q#7 avg":q18_7averaGe2,"q#7 var":q18_7varioo,
           "q#8 min":q18_8mini,"q#8 max":q18_8maxi,"q#8 avg":q18_8averaGe2,"q#8 var":q18_8varioo,
           "q#9 min":q18_9mini,"q#9 max":q18_9maxi,"q#9 avg":q18_9averaGe2,"q#9 var":q18_9varioo,
           "q#10 min":q18_10mini,"q#10 max":q18_10maxi,"q#10 avg":q18_10averaGe2,"q#10 var":q18_10varioo,
           " q#11": q11_frame_list,
           "q#12 min":q18_12mini,"q#12 max":q18_12maxi,"q#12 avg":q18_12averaGe2,"q#12 var":q18_12varioo,
           "q#13 min":q18_13mini,"q#13 max":q18_13maxi,"q#13 avg":q18_13averaGe2,"q#13 var":q18_13varioo,
           " q#14": q14_frame_list,
           " q#15": q15_frame_list,
           " q#16": q16_frame_list,
           "q#17 population":populations,"q#17  median age": median_age2,"q#17  # of people aged 65 older ":aged_65,"q#17 # of people aged 70 older":aged_70,"q#17 economic performance ":gdp_per,"q#17 death rates due to heart disease ":cardiovasc_rate,"q#17 diabetes prevalence ":dia_prevalence,"q#17  # of female smokers ":female_smoker,
           "q#17 # of male smokers":male_smoker,"q#17 handwashing facilities ":hand_facilities,"q#17  hospital beds per thousand people ":hospital_thousand,"q#17  life expectancy ":life_expec,"q#17 human development index ":human_development}
                
q5table_df = pd.DataFrame(q5table)

file_object.write(q5table_df.to_string())
file_object.close()  