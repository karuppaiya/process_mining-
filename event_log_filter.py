#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("trace.csv")


# In[3]:


df.columns


# In[4]:


df.shape


# In[35]:


len(df['concept:name'].unique())


# In[27]:


first_last_event = []
for i in df['case:concept:name'].unique():
    sub = df[df['case:concept:name']==i]
    sub = sub.reset_index(drop=True)
    first_event = sub.iloc[:,1][0]
    last_event = sub.iloc[:,1][sub.shape[0]-1]
    
    if first_event not in first_last_event:
        first_last_event.append(first_event)
    
    if last_event not in first_last_event:
        first_last_event.append(last_event)


# In[29]:


# In[42]:


activity_counts_500 = activity_counts[activity_counts.values<500]


# In[44]:


event_to_remove = [ i for i in activity_counts_300.index if i not in first_last_event]


# In[61]:


len(event_to_remove)


# In[82]:


filtered_df = pd.DataFrame()

for i in df['case:concept:name'].unique():
    sub = df[df['case:concept:name']==i]
    sub = sub.reset_index(drop=True)
    
    events = []
    for e in list(sub['concept:name'].values):
        if e not in event_to_remove:
            events.append(True)
        else:
            events.append(False)

    final_sub = sub[events]

    filtered_df = filtered_df.append(final_sub)


# In[83]:


filtered_df.shape


# In[84]:


len(filtered_df['concept:name'].unique())


# In[86]:


filtered_df.to_csv('traces_updated.csv',index=False)


# In[89]:


filtered_df_dead = pd.DataFrame()
filtered_df_discharge = pd.DataFrame()

for i in filtered_df['case:concept:name'].unique():
    sub = filtered_df[filtered_df['case:concept:name']==i]
    sub = sub.reset_index(drop=True)
    last_event = sub.iloc[:,1][sub.shape[0]-1]
    
    if last_event == 'disch':
        filtered_df_discharge = filtered_df_discharge.append(sub)
    elif last_event == 'death':
        filtered_df_dead = filtered_df_dead.append(sub)
    else:
        print(i)
        break


# In[91]:


filtered_df_dead.to_csv('death.csv',index=False)


# In[92]:


filtered_df_discharge.to_csv('disch.csv',index=False)

