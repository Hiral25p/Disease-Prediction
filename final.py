#hiral patel

from tkinter import *
import numpy as np
import pandas as pd

l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
      'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
      'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
      'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
      'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
      'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
      'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
      'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
      'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
      'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
      'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
      'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
      'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
      'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
      'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
      'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
      'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
      'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
      'yellow_crust_ooze']

disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           ' Migraine', 'Cervical spondylosis',
           'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
           'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
           'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
           'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
           'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
           'Impetigo']
l2 = []

for i in range(0, len(l1)):
    l2.append(0)

df = pd.read_csv("Prototype.csv") #test
df.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9, 'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16, 'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23, 'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29, 'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38, 'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)

X = df[l1]  # print df head
y = df[["prognosis"]]
np.ravel(y)

tr = pd.read_csv("Prototype.csv") #training
tr.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9, 'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16, 'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23, 'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29, 'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38, 'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)

X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    alg = RandomForestClassifier()
    alg = alg.fit(X, np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = alg.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get()]
    for k in range(0, len(l1)):
        for z in psymptoms:
            if(z == l1[k]):
                l2[k] = 1
    inputtest = [l2]
    predict = alg.predict(inputtest)
    predicted = predict[0]
    h = 'no'
    for a in range(0, len(disease)):
        if(predicted == a):
            h = 'yes'
            break
    if (h == 'yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")

root = Tk()
root.configure(background = 'cornflower blue')
Symptom1 = StringVar()
Symptom1.set("Select Here")
Symptom2 = StringVar()
Symptom2.set("Select Here")
Symptom3 = StringVar()
Symptom3.set("Select Here")
Name = StringVar()
NameLb = Label(root, text = "NAME:", fg = "green yellow", bg = "cornflower blue")
NameLb.config(font=("Times", 24, "bold"))
NameLb.grid(row = 6, column = 0, pady  = 15, sticky = W)
S1Lb = Label(root, text = "SYMPTOM 1:", fg = "green yellow", bg = "cornflower blue")
S1Lb.config(font=("Times", 24, "bold"))
S1Lb.grid(row=7, column = 0, pady = 15, sticky = W)
S2Lb = Label(root, text = "SYMPTOM 2:", fg = "green yellow", bg = "cornflower blue")
S2Lb.config(font = ("Times", 24, "bold"))
S2Lb.grid(row = 8, column = 0, pady = 15, sticky = W)
S3Lb = Label(root, text = "SYMPTOM 3:", fg = "green yellow", bg = "cornflower blue")
S3Lb.config(font=("Times", 24, "bold"))
S3Lb.grid(row = 9, column = 0, pady = 10, sticky = W)
destreeLb = Label(root, text = "PROBABLE DISEASE:", fg = "green yellow", bg = "cornflower blue")
destreeLb.config(font = ("Times", 22, "bold"))
destreeLb.grid(row = 20, column = 0, pady = 10, sticky = W)
OPTIONS = sorted(l1)
NameEn = Entry(root, textvariable = Name)
NameEn.grid(row = 6, column = 1)
S1 = OptionMenu(root, Symptom1, *OPTIONS)
S1.grid(row = 7, column = 1)
S2 = OptionMenu(root, Symptom2, *OPTIONS)
S2.grid(row = 8, column = 1)
S3 = OptionMenu(root, Symptom3, *OPTIONS)
S3.grid(row = 9, column = 1)
rnf = Button(root, text = "CHECK", command = randomforest, bg = "cornflower blue", fg = "green yellow")
rnf.config(font = ("Times", 20, "bold"))
rnf.grid(row = 9, column = 3, padx = 15)
t1 = Text(root, height = 1, width = 30, bg = "white", fg = "black")
t1.config(font = ("Times", 24, "bold"))
t1.grid(row = 20, column = 1, padx = 15)
root.mainloop()