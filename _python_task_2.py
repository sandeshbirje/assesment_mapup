#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np

# Question 1: Distance Matrix Calculation
def calculate_distance_matrix(df):
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance')
    np.fill_diagonal(distance_matrix.values, 0)
    distance_matrix = distance_matrix.add(distance_matrix.T, fill_value=0)
    return distance_matrix

# Question 2: Unroll Distance Matrix
def unroll_distance_matrix(df):
    df_unrolled = df.stack().reset_index()
    df_unrolled.columns = ['id_start', 'id_end', 'distance']
    df_unrolled = df_unrolled[df_unrolled['id_start'] != df_unrolled['id_end']]
    return df_unrolled

# Question 3: Finding IDs within Percentage Threshold
def find_ids_within_ten_percentage_threshold(df, ref_id):
    ref_avg = df[df['id_start'] == ref_id]['distance'].mean()
    threshold_ids = df[(df['distance'] >= 0.9 * ref_avg) & (df['distance'] <= 1.1 * ref_avg)]['id_start'].unique()
    return sorted(list(threshold_ids))

# Question 4: Calculate Toll Rate
def calculate_toll_rate(df):
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}
    for vehicle, rate in rate_coefficients.items():
        df[vehicle] = df['distance'] * rate
    return df


# In[6]:


df = pd.read_csv('assesment_2.csv')
df.head()


# In[8]:


distance_matrix = calculate_distance_matrix(df)
df_unrolled = unroll_distance_matrix(distance_matrix)
threshold_ids = find_ids_within_ten_percentage_threshold(df_unrolled, 1001400)
df_with_rates = calculate_toll_rate(df_unrolled)


# In[10]:


distance_matrix.head()


# In[11]:


df_unrolled.head()


# In[13]:


threshold_ids


# In[14]:


df_with_rates


# In[ ]:




