import pandas as pd

df = pd.read_csv("hospital_data.csv")
df.head()
df['AdmissionDate'] = pd.to_datetime(df['AdmissionDate'])
df['DischargeDate'] = pd.to_datetime(df['DischargeDate'])
df['LengthOfStay'] = (df['DischargeDate'] - df['AdmissionDate']).dt.days
readmission_rate = df['Readmitted'].value_counts(normalize=True) * 100
print(readmission_rate)
dept_analysis = df.groupby("Department")["LengthOfStay"].mean()
print(dept_analysis)
import matplotlib.pyplot as plt

dept_analysis.plot(kind='bar')
plt.title("Avg Length of Stay by Department")
plt.show()