# Importing required modules
import pandas as pd

# Error handling in reading the csv files
try: 
    name = "gender_data.csv"
    country_codes = "codes.csv"
    
    gender_data = pd.read_csv(name, sep = ";")
    countries = pd.read_csv(country_codes, sep = ",")
                             
except FileNotFoundError: 
    print("Sorry, file is not found")

except Exception as msg: 
    print(msg)
    
# Cleaning the data

# Changing the country codes into their respective name
for i in range(len(countries)): 
    gender_data["Countries"].replace([countries.loc[i,"Country_codes"]], countries.loc[i,"Name"], inplace = True)

# Changing the name of the head of the columns
gender_data.rename(columns = {"UnitedNations_16": 'Trust_UN_Percentage', \
                        "EuropeanParliament_15": 'Trust_EP_Percentage', \
                        "Parliament_13": 'Trust_Parliament_Percentage', \
                        "UnitedNations_8": 'Trust_UN_Score', \
                        "EuropeanParliament_7": "Trust_EP_Score", \
                        "Parliament_5": "Trust_Parliament_Score", 
                        "PersonalCharacteristics": "Gender"}, inplace = True)

# Changing the personal characteristics code to their respective gender
for i in gender_data["Gender"]: 
    if i == 3000: 
        gender_data["Gender"].replace([3000], "Male", inplace = True)
    elif i == 4000: 
        gender_data["Gender"].replace([4000], "Female", inplace = True)

# Changing the year to make it reader-friendly
gender_data["Periods"].replace(["2016JJ00"], '2016', inplace = True)
    
# Separating the male and female data
male_data = gender_data.loc[(gender_data['Gender'] == "Male")][['Countries', 
             'Trust_Parliament_Percentage', 'Trust_EP_Percentage', 
             'Trust_UN_Percentage']]
    
female_data = gender_data.loc[(gender_data['Gender'] == "Female")][['Countries', 
              'Trust_Parliament_Percentage', 'Trust_EP_Percentage', 
             'Trust_UN_Percentage']]  
