def BMI_calculation(Patient_infromations):
    import json
    import pandas
    data=json.load(Patient_infromations)
    Weight=[]
    Height=[]
    Gender=[]
    bmi=[]
    Category=[]
    Risk=[]
    try:
        for i in data['patient_list']:
            weight=i['WeightKg']
            Weight.append(weight)
            height=i['HeightCm']
            Height.append(height)
            gender=i['Gender']
            Gender.append(gender)
            try:
                BMI = weight / (height/100)**2
                bmi.append(BMI)
                if (BMI <= 18.4):
                    category="Underweight"
                    risk= "Malnutrition risk"

                elif (BMI >= 18.5 and BMI < 24.9):
                    category = "Normal Weight"
                    risk = "Low risk"

                elif (BMI >= 25 and BMI < 29.9):
                    category = "Overweight"
                    risk = "Enhanced risk"

                elif (BMI >= 30 and BMI < 34.9):
                    category = "Moderately Obsese"
                    risk = "Medium Risk"

                elif (BMI >= 35 and BMI < 39.9):
                    category = "severely Obsese"
                    risk = "High risk"

                elif (BMI >= 40):
                    category = "Very severely obses"
                    risk = "Very High risk"

                Category.append(category)
                Risk.append(risk)
            except:
                    print("No Proper inputs provided")




        report = pandas.DataFrame({'Height': Height, 'Weight': Weight, 'Gender':Gender, 'BMI':bmi, 'BMI_Category':Category, 'HealthRisk':Risk})
        print(report)
        print('Number of Patients are Underweight and at a malnutrition risk =',len(report[report['BMI_Category'] == 'Underweight']))
        print('Number of Patients are Normal Weight  and at a Low risk =',len(report[report['BMI_Category'] == 'Normal Weight']))
        print('Number of Patients are Over Weight and at a Enhanced risk =',len(report[report['BMI_Category'] == 'Overweight']))
        print('Number of Patients are Moderately Obsese and at a Medium risk =', len(report[report['BMI_Category'] == 'Moderately Obsese']))
        print('Number of Patients are Severly obsessed and at a High risk =',len(report[report['BMI_Category'] == 'severely Obsese']) )
        print('Number of Patients are Very Severly Obsessed and at a Very high risk =', len(report[report['BMI_Category'] == 'Very severely obses']))

    except:
        print("No proper inputs provided")

BMI_calculation(open('data.json', ))