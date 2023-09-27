import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# read csv file to dataframe

df = pd.read_csv('uhsdatanew.csv',sep=';', usecols=['q1_1','q1_2','q1_3','q1_4','q1_5','q1_23','q1_24','q1_25','q1_26','q2','q8a','q8b','q9a','q9b','q13','q14','q15_22','q15_24','q15_25','q15_26','q18','q25','q34','q35','q36_2','q37','q41_1','q43','q49_1','q49_2','q49_4','q49_5','q49_7','q54','q90','q92_1','q92_2','q110','sukupuol'])

#cleaning the data
df1 = df[df['q1_1'] == '0']
df2 = df1[df1['q1_2'] == '0']
df3 = df2[df2['q1_3'] == '0']
df4 = df3[df3['q1_4'] == '0']
df5 = df4[df4['q1_5'] == '0']
df6 = df5[df5['q1_23'] == '0']
df7 = df6[df6['q1_24'] == '0']
df8 = df7[df7['q1_25'] == '0']
df9 = df8[df8['q1_26'] == '0']

df9 = df9.replace({None: -1})
df9 = df9.replace({' ': -1})
df9['sukupuol']=df9['sukupuol'].astype("category")

#Histogram of distribution of sexes
hist = df9.sukupuol.value_counts().plot(kind='bar',title="Sukupuoli")
plt.show()

#Taking only rows with all questions we need answers to, are answered
df10 = df9[df9['q2'] != -1]
df11 = df10[df10['q13'] != -1]
df12 = df11[df11['q14'] != -1]
df13 = df12[df12['q15_22'] != -1]
df14 = df13[df13['q15_24'] != -1]
df15 = df14[df14['q15_25'] != -1]
df16 = df15[df15['q15_26'] != -1]
df17 = df16[df16['q18'] != -1]
df18 = df17[df17['q25'] != -1]
df19 = df18[df18['q34'] != -1]
df20 = df19[df19['q35'] != -1]
df21 = df20[df20['q36_2'] != -1]
df22 = df20[df20['q37'] != -1]
df23 = df22[df22['q41_1'] != -1]
df24 = df23[df23['q43'] != -1]
df25 = df24[df24['q49_1'] != -1]
df26 = df25[df25['q49_2'] != -1]
df27 = df26[df26['q49_4'] != -1]
df28 = df27[df27['q49_5'] != -1]
df29 = df28[df28['q49_7'] != -1]
df30 = df29[df29['q54'] != -1]
df31 = df30[df30['q90'] != -1]
df32 = df31[df31['q92_1'] != -1]
df33 = df32[df32['q92_2'] != -1]
df34 = df33[df33['q110'] != -1]

#separating to men and women
df34['sukupuol']=df34['sukupuol'].astype("int64")
mendf = df34[df34['sukupuol'] == 1]
womendf = df34[df34['sukupuol'] == 2]

print("Shape of men df: ",mendf.shape)
print("Shape of women df: ",womendf.shape)

#Dropping columns that have been used and are specified by sex
mendf1 = mendf.drop(['q1_1','q1_2','q1_3','q1_4','q1_5','q1_23','q1_24','q1_25','q1_26','q9b','q8b','sukupuol'],axis=1)
womendf1 = womendf.drop(['q1_1','q1_2','q1_3','q1_4','q1_5','q1_23','q1_24','q1_25','q1_26','q8a','q9a','sukupuol'],axis=1)

#Now we are left with columns ['q2','q8a','q8b','q9a','q9b','q13','q14','q15_22','q15_24','q15_25','q15_26','q18','q25','q34','q35','q36_2','q37','q41_1','q43','q49_1','q49_2','q49_4','q49_5','q49_7','q54','q90','q92_1','q92_2','q110']

#Calculating bmi
def bmi(heightcm,weight):
    height = heightcm/100
    return weight/height**2

mendf1['q8a']=mendf1['q8a'].astype('float64')
womendf1['q8b']=womendf1['q8b'].astype('float64')

mendf1['q9a']=mendf1['q9a'].astype('float64')
womendf1['q9b']=womendf1['q9b'].astype('float64')

bmilistmen = []
for i in range(0,len(mendf1['q8a'])):
    bmilasku = bmi(mendf1['q8a'].iloc[i],mendf1['q9a'].iloc[i])
    bmilistmen.append(bmilasku)

bmilistwomen = []
for i in range(0,len(womendf1['q8b'])):
    bmilaskuwomen = bmi(womendf1['q8b'].iloc[i],womendf1['q9b'].iloc[i])
    bmilistwomen.append(bmilaskuwomen)

#Adding column with bmi into dataframe
mendf1['bmi'] = bmilistmen
womendf1['bmi'] = bmilistwomen

#Dropping weight and height columns
womendffinal = womendf1.drop(['q8b','q9b'],axis=1)
mendffinal = mendf1.drop(['q8a','q9a'],axis=1)

print(womendffinal.head())
print(mendffinal.head())

#How students in general describe their health
womendffinal['q2']=womendffinal['q2'].astype("category")
mendffinal['q2']=mendffinal['q2'].astype("category")

womendffinal.rename(columns = {'q2':'ylterv'}, inplace = True)
mendffinal.rename(columns = {'q2':'ylterv'}, inplace = True)

histwo = womendffinal.ylterv.value_counts().plot(kind='bar',title="How would you describe your health in general?(Women)")
plt.show()

histmen = mendffinal.ylterv.value_counts().plot(kind='bar',title="How would you describe your health in general?(Men)")
plt.show()

#Setting all to correct categories or int/float values
womendffinal.rename(columns = {'q13':'unih'}, inplace = True)
womendffinal['unih']=womendffinal['unih'].astype("float64")

mendffinal.rename(columns = {'q13':'unih'}, inplace = True)
mendffinal['unih']=mendffinal['unih'].astype("float64")

womendffinal.unih.hist(color='hotpink',alpha=0.5,label='Women',bins=12).set_title("Sleep per night in hours")
mendffinal.unih.hist(label='Men',alpha=0.5,bins=12)
plt.legend()
plt.show()

womendffinal.rename(columns = {'q14':'riituni'}, inplace = True)
womendffinal['riituni']=womendffinal['riituni'].astype("category")

mendffinal.rename(columns = {'q14':'riituni'}, inplace = True)
mendffinal['riituni']=mendffinal['riituni'].astype("category")

womendffinal.riituni.value_counts().plot(kind='bar',alpha=0.5,color='hotpink',title="Do you feel you sleep enough?")
mendffinal.riituni.value_counts().plot(kind='bar',alpha=0.5)
plt.show()

womendffinal.rename(columns={'q34':'liikunta'}, inplace = True)
womendffinal['liikunta']=womendffinal['liikunta'].astype("category")

mendffinal.rename(columns={'q34':'liikunta'}, inplace = True)
mendffinal['liikunta']=mendffinal['liikunta'].astype("category")

plt.plot(womendffinal['unih'],womendffinal['liikunta'],linestyle='', marker='o',markersize=3, alpha=0.1, color="purple",label="Women")
plt.plot(mendffinal['unih'],mendffinal['liikunta'],linestyle='', marker='o',markersize=3, alpha=0.1, color="g",label="Men")
plt.legend()
plt.xlabel("Uni tunteina/yö")
plt.ylabel("Liikunta asteikolla 0-5, 0 ei ollenkaan, 5 päivittäin")
plt.show()

womendffinal['liikunta']=womendffinal['liikunta'].astype("int64")
mendffinal['liikunta']=mendffinal['liikunta'].astype("int64")
sb.regplot(data = womendffinal, x = 'unih', y = 'liikunta', fit_reg = False,x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 1/3})
sb.regplot(data = mendffinal, x = 'unih', y = 'liikunta', fit_reg = False,x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 1/3},color='purple')
plt.show()

#['q15_22','q15_24','q15_25','q15_26','q18','q25','q34','q35','q36_2','q37','q41_1','q43','q49_1','q49_2','q49_4','q49_5','q49_7','q54','q90','q92_1','q92_2','q110']
