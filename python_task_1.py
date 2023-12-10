#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

# Question 1: Car Matrix Generation
def generate_car_matrix(df):
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    np.fill_diagonal(car_matrix.values, 0)
    return car_matrix

# Question 2: Car Type Count Calculation
def get_type_count(df):
    df['car_type'] = pd.cut(df['car'], bins=[-np.inf, 15, 25, np.inf], labels=['low', 'medium', 'high'])
    type_count = df['car_type'].value_counts().sort_index().to_dict()
    return type_count

# Question 3: Bus Count Index Retrieval
def get_bus_indexes(df):
    mean_bus = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    return sorted(bus_indexes)

# Question 4: Route Filtering
def filter_routes(df):
    avg_truck = df['truck'].mean()
    filtered_routes = df[df['truck'] > avg_truck]['route'].tolist()
    return filtered_routes


# In[4]:


df = pd.read_csv('assesment_1.csv')
df.head()


# In[5]:


car_matrix = generate_car_matrix(df)
type_count = get_type_count(df)
bus_indexes = get_bus_indexes(df)
filtered_routes = filter_routes(df)


# # Question 1: Car Matrix Generation

# In[7]:


car_matrix.head()


# # Question 2: Car Type Count Calculation

# In[9]:


type_count


# # Question 3: Bus Count Index Retrieval

# In[10]:


bus_indexes


# # Question 4: Route Filtering

# In[11]:


filtered_routes


# # Question 5: Matrix Value Modification

# In[13]:


# Question 5: Matrix Value Modification
def multiply_matrix(df):
    df = df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    return df.round(1)

modified_matrix = multiply_matrix(car_matrix)
modified_matrix.head()


# # Question 6: Time Check

# In[14]:


# Question 6: Time Check
def check_timestamps(df):
    df['timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    df = df.set_index(['id', 'id_2'])
    result = df.groupby(level=[0, 1]).apply(lambda x: (x['timestamp'].dt.hour.min() == 0) & 
                                                (x['timestamp'].dt.hour.max() == 23) & 
                                                (x['timestamp'].dt.dayofweek.nunique() == 7) &
                                                (x['end_timestamp'].dt.hour.min() == 0) & 
                                                (x['end_timestamp'].dt.hour.max() == 23) & 
                                                (x['end_timestamp'].dt.dayofweek.nunique() == 7
                                                 

incorrect_timestamps = check_timestamps(df2)
    


# In[ ]:




