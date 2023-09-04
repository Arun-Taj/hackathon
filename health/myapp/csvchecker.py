
import csv

csv_file="../medicine.csv"
def csvcheck(symptoms):
    data_list=[]
    with open(csv_file,'r') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            csv_symptoms=row['symptoms'].lower()
            input_symptoms=[symptom.lower() for symptom in symptoms]
            data_list.append(row['symptoms'])
            exists=any(item in csv_symptoms for item in input_symptoms)
            if exists:
                return True
                
    print(data_list)
    return False
