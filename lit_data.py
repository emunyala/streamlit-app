# Data visualization with StreamLit

# By : ELiud Munyala

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt



data = pd.read_csv(r'/home/eliud_luda/Desktop/Moringa_Prep/W5_prep/final_data.csv')

df = pd.DataFrame(data)

"""

Our data works on the following premises:
##### Age groups 10-19
##### Years 2010 to 2020
##### Countries : Kenya,Uganda,Tanzania
##### Residence: Rural or Urban
==========================================
"""


df


variables = st.sidebar.multiselect("Columns", df.columns)
st.write("You selected these columns", variables)

# Countries = st.sidebar.multiselect("Countries", df['Country'])
# st.write("You selected these countries", Countries)

# residence = st.sidebar.multiselect("Residence", df['DISAGG'])
# st.write("You selected these regions", residence)



fig = px.pie(df, values=df['Total_Living'], names=df['Country'], title='Total Confirmed People living With HIV IN East Africa')
st.plotly_chart(fig)

fig_1 = px.pie(df, values=df['Total_Mortality'], names=df['Country'], title='Total HIV Mortality in East Africa')
st.plotly_chart(fig_1)

fig_2 = px.pie(df, values=df['Percent_of_Educated'], names=df['Country'], title='HIV Education level East Africa')
st.plotly_chart(fig_2)


fig_3 = px.pie(df, values=df['Percent_in_Rural_Urban'], names=df['Country'], title='HIV Education level East Africa')
st.plotly_chart(fig_3)


fig_4 = px.bar(df, x="Country", y=["Total_Living","Total_Mortality","Total_of_new_Infect","Total"],title="Total for People livind with HIV, and Mortality", barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig_4)



fig_5 = px.bar(df, x="Country", y=["%_living_educated","%_mortality_educated","%_new_educated","%_new_infected_educated"],title="Total percentage of People educated on and living with HIV, and Mortality", barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig_5)