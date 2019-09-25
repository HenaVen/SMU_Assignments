#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data

# Read the Mouse and Drug Data and the Clinical Trial Data
df=pd.read_csv(mouse_drug_data_to_load)
df2=pd.read_csv(clinical_trial_data_to_load)
# Combine the data into a single dataset-merge

fullDF=pd.merge(df,df2 on='Mouse ID', how='left')
# Display the data table for preview

fullDF.head



# In[11]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data

# Read the Mouse and Drug Data and the Clinical Trial Data
df=pd.read_csv(mouse_drug_data_to_load)
df.head

df2=pd.read_csv(clinical_trial_data_to_load)
df2.head
# Combine the data into a single dataset-merge

fullDF=pd.merge(df,df2, how ='left',on='Mouse ID')
# Display the data table for preview

fullDF.head


# ## Tumor Response to Treatment

# In[ ]:





# In[34]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 

# Convert to DataFrame
#meanTumor=fullDF.groupby(["Drug","Timepoint"]).mean()
# Preview DataFrame

# Convert to DataFrame
meanTumor=fullDF.groupby(["Drug","Timepoint"]).mean()["Tumor Volume (mm3)"]
meanTumor.head
# Preview DataFrame
#type(meanTumor) Series
meanTumorDF=pd.DataFrame(meanTumor)
type(meanTumorDF)
meanTumorDF.head
meanTumorDF=pd.DataFrame(meanTumor).reset_index()


# In[ ]:





# In[2]:





# In[33]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint

# Convert to DataFrame

# Preview DataFrame
# Convert to DataFrame
#meanTumor=fullDF.groupby(["Drug","Timepoint"]).mean()
# Preview DataFrame

# Convert to DataFrame
semTumor=fullDF.groupby(["Drug","Timepoint"]).sem()["Tumor Volume (mm3)"]
semTumor.head
# Preview DataFrame
#type(semTumor) Series
semTumorDF=pd.DataFrame(semTumor)
type(semTumorDF)
semTumorDF.head
semTumorDF=pd.DataFrame(semTumor).reset_index()


# In[3]:





# In[41]:


# Minor Data Munging to Re-Format the Data Frames

# Preview that Reformatting worked
# Minor Data Munging to Re-Format the Data Frames
countMousePivot=meanTumorDF.pivot(index='Timepoint' , columns='Drug',values='Tumor Volume (mm3)')
countMousePivot.head

countMouseSemPivot=semTumorDF.pivot(index='Timepoint' , columns='Drug',values='Tumor Volume (mm3)')
countMouseSemPivot.head


# In[ ]:





# In[4]:





# In[42]:


# Generate the Plot (with Error Bars)

# Save the Figure
# Plot sample means with error bars
fig, ax = plt.subplots()

ax.plot(countMousePivot.index.values, (countMousePivot.Ketapril.values/countMousePivot.Ketapril.values[0] * 100), marker="s", color="g",
            alpha=0.5, label="Ketapril", ls="--")

ax.plot(countMousePivot.index.values, (countMousePivot.Capomulin.values/countMousePivot.Capomulin.values[0] * 100), marker="o", color="r",
            alpha=0.5, label="Capomulin", ls="--")

ax.plot(countMousePivot.index.values, (countMousePivot.Infubinol.values/countMousePivot.Infubinol.values[0] * 100), marker="^", color="b",
            alpha=0.5, label="Infubinol", ls="--")

ax.plot(countMousePivot.index.values, (countMousePivot.Placebo.values/countMousePivot.Placebo.values[0] * 100), marker="D", color="k",
            alpha=0.5, label="Placebo", ls="--")

ax.set_xlim(-0.5, 47)

ax.set_title("Survival During Treatment")

ax.set_xlabel("Time (days)")
ax.set_ylabel("Survival Rate (%)")

plt.legend(loc="best", fontsize="small", fancybox=True)

plt.grid(axis='both')

plt.show()


# In[ ]:


# Show the Figure
plt.show()


# ![Tumor Response to Treatment](../Images/treatment.png)

# ## Metastatic Response to Treatment

# In[47]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 

# Convert to DataFrame

# Preview DataFrame
meanmetaTumor=fullDF.groupby(["Drug","Timepoint"]).mean()["Metastatic Sites"]
meanmetaTumor.head
# Preview DataFrame
#type(meanTumor) Series
meanmetaTumorDF=pd.DataFrame(meanmetaTumor)
type(meanmetaTumorDF)
meanmetaTumorDF.head
meanmetaTumorDF=pd.DataFrame(meanmetaTumor).reset_index()


# In[6]:





# In[48]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 

# Convert to DataFrame

# Preview DataFrame
semmetaTumor=fullDF.groupby(["Drug","Timepoint"]).sem()["Metastatic Sites"]
semmetaTumor.head
# Preview DataFrame
#type(meanTumor) Series
semmetaTumorDF=pd.DataFrame(semmetaTumor)
type(semmetaTumorDF)
semmetaTumorDF.head
semmetaTumorDF=pd.DataFrame(semmetaTumor).reset_index()


# In[7]:





# In[49]:


# Minor Data Munging to Re-Format the Data Frames

# Preview that Reformatting worked
countMousemetaPivot=meanmetaTumorDF.pivot(index='Timepoint' , columns='Drug',values='Metastatic Sites')
countMousemetaPivot.head

countMouseSemPivot=semmetaTumorDF.pivot(index='Timepoint' , columns='Drug',values='Metastatic Sites')
countMouseSemPivot.head


# In[8]:





# In[50]:


# Generate the Plot (with Error Bars)

# Save the Figure

# Show the Figure
fig, ax = plt.subplots()

ax.plot(countMousemetaPivot.index.values, (countMousemetaPivot.Ketapril.values/countMousemetaPivot.Ketapril.values[0] * 100), marker="s", color="g",
            alpha=0.5, label="Ketapril", ls="--")

ax.plot(countMousemetaPivot.index.values, (countMousemetaPivot.Capomulin.values/countMousemetaPivot.Capomulin.values[0] * 100), marker="o", color="r",
            alpha=0.5, label="Capomulin", ls="--")

ax.plot(countMousemetaPivot.index.values, (countMousemetaPivot.Infubinol.values/countMousemetaPivot.Infubinol.values[0] * 100), marker="^", color="b",
            alpha=0.5, label="Infubinol", ls="--")

ax.plot(countMousemetaPivot.index.values, (countMousemetaPivot.Placebo.values/countMousemetaPivot.Placebo.values[0] * 100), marker="D", color="k",
            alpha=0.5, label="Placebo", ls="--")

ax.set_xlim(-0.5, 47)

ax.set_title("Metastatic Spread During Treatment")

ax.set_xlabel("Treatment Duration (days)")
ax.set_ylabel("Met.Sites")

plt.legend(loc="best", fontsize="small", fancybox=True)

plt.grid(axis='both')

plt.show()


# In[ ]:





# ![Metastatic Spread During Treatment](../Images/spread.png)

# ## Survival Rates

# In[ ]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)

# Convert to DataFrame

# Preview DataFrame


# In[10]:





# In[ ]:


# Minor Data Munging to Re-Format the Data Frames

# Preview the Data Frame


# In[11]:





# In[ ]:


# Generate the Plot (Accounting for percentages)

# Save the Figure

# Show the Figure
plt.show()


# ![Metastatic Spread During Treatment](../Images/survival.png)

# ## Summary Bar Graph

# In[ ]:


# Calculate the percent changes for each drug

# Display the data to confirm


# In[13]:





# In[ ]:


# Store all Relevant Percent Changes into a Tuple


# Splice the data between passing and failing drugs


# Orient widths. Add labels, tick marks, etc. 


# Use functions to label the percentages of changes


# Call functions to implement the function calls


# Save the Figure


# Show the Figure
fig.show()


# ![Metastatic Spread During Treatment](../Images/change.png)

# In[ ]:




