#!/usr/bin/env python
# coding: utf-8

# In[1]:

import PySimpleGUI as pg
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import sys




# In[2]:


Profits = pd.read_excel('Profit_list.xlsx')


# In[3]:





# In[4]:





# In[5]:





# In[8]:


X = Profits[['Marketing Spend', 'Administration', 'Transport', 'Last qrtr', 'Last 4 qrtr', 'Last 8 qrtr', 'Employee', 'Emp cost', 'Other cost', 'Taxes', 'New eqp']]
y = Profits[['Prof qrtr', 'Prof 4 qrtr', 'Prof change', 'Avg emp']]


# In[9]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101) 


# In[10]:


from sklearn.linear_model import LinearRegression 

lm = LinearRegression() 

lm.fit(X_train,y_train) 


# In[12]:





# In[19]:





# In[20]:





# In[21]:





# In[38]:
pg.theme("SandyBeach")
pg.set_options(font=('Courier 12'))
layout = [
    [pg.Text("Enter Marketing Spend", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Administration Cost", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Transport Cost", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Total Revenue in Last Quarter", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Total Revenue in Last 4 Quarters", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Total Revenue in Last 8 Quarters", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Number of Employees", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Employee Cost", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Other Costs", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter Taxes", size=(40,1)),
     pg.InputText()
    ],
    [pg.Text("Enter New Equipment Costs", size=(40,1)),
     pg.InputText()
    ],
    [pg.Button("ok", font=('Helvetica', 14),button_color=('white', 'brown'), size=(4,0), border_width=0,), pg.Button("cancel", font=('Helvetica', 14),button_color = 'Purple', border_width=0)],
    [pg.Text("Profit Next Quarter: ", size=(0, 1), key='OUTPUT1')],
    [pg.Text("Profit Next 4 Quarters: ", size=(0, 1), key='OUTPUT2')],
    [pg.Text("Profit change: ", size=(0, 1), key='OUTPUT3')],
    [pg.Text("Mean cost per employee: ", size=(0, 1), key='OUTPUT4')],
    [pg.Image('nditc.png', size=(600,100), expand_x=True)]
   ]
window = pg.Window("NDITC PROFIT PREDICTOR", layout, size=(850,600))
while True:
    event, values = window.read()
    if event == "cancel" or event == pg.WIN_CLOSED:
        break
    elif event == "ok":
        Marketing_Spend = values[0]
        Administration = values[1]
        Transport = values[2]
        Last_qrtr = values[3]
        Last_4_qrtr = values[4]
        Last_8_qrtr = values[5]
        Employees = values[6]
        Employee_Cost = values[7]
        Others = values[8]
        Taxes = values[9]
        New_eqp = values[10]        
        data = {'Marketing Spend':[float(Marketing_Spend)], 'Administration':[float(Administration)], 'Transport':[float(Transport)], 'Last qrtr':[float(Last_qrtr)], 'Last 4 qrtr':[float(Last_4_qrtr)], 'Last 8 qrtr':[float(Last_8_qrtr)], 'Employee':[float(Employees)], 'Emp cost':[float(Employee_Cost)], 'Other cost':[float(Others)], 'Taxes':[float(Taxes)], 'New eqp':[(New_eqp)]}
        predict_data = pd.DataFrame(data)
        print(lm.predict(predict_data))
        window['OUTPUT1'].update(value="Profit Next Quarter: " + str(lm.predict(predict_data)[0][0]))
        window['OUTPUT2'].update(value="Profit Next 4 Quarters: " + str(lm.predict(predict_data)[0][1]))
        window['OUTPUT3'].update(value="Profit change: " + str(lm.predict(predict_data)[0][2]) + "%")
        window['OUTPUT4'].update(value="Mean cost per employee: " + str(lm.predict(predict_data)[0][3]))
    print(values)

window.close()




# In[39]:





# In[40]:





# In[ ]:





# In[ ]:




