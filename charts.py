import pandas as pd
import plotly.express as px
import streamlit as st
from matplotlib.pyplot import title


def charts():
    data=pd.read_csv(r"C:\Users\Vinoth\Documents\GitHub\Github_Data_dive\All.csv")
    data.drop('Unnamed: 0', axis=1, inplace=True)
    x=data['Programming Language'].value_counts()
    language_counts_df = x.reset_index()
    language_counts_df.columns = ['Programming_Language', 'Frequency']
    img=px.bar(language_counts_df, language_counts_df['Programming_Language'],
               language_counts_df['Frequency'], title="Popular Programming Language",
               color='Programming_Language')
    st.plotly_chart(img, use_container_width=True)

    img = px.bar(data, x='Programming Language',
                 y=['Number of Stars','Number of Forks'],
                 barmode='group', title='Stars and Forks by Programming Language',
             labels={'value': 'Count', 'variable': 'Metrics'},
             color_discrete_sequence=['#636EFA', '#EF553B'])
    st.plotly_chart(img, use_container_width=True)

    yearly_counts = data.groupby('Created Year').size().reset_index(name='Count')

    img=px.line(yearly_counts, x='Created Year', y='Count', title='Repository Creation Over Time')

    st.plotly_chart(img, use_container_width=True)

    img=px.scatter(data, x='Number of Stars', y='Number of Open Issues', text='Repository Name', title='Open Issues vs. Stars')
    img.update_traces(textposition='top right')
    st.plotly_chart(img, use_container_width=True)

    License_counts = data.groupby('License Type').size().reset_index(name='Count')
    img=px.pie(License_counts, names='License Type', values='Count', title='License Type Distribution', color_discrete_sequence=['#636EFA', '#EF553B'])
    st.plotly_chart(img, use_container_width=True)

    img=px.bar(data.sort_values('Number of Stars', ascending=False),
           x='Number of Stars',
           y='Repository Name',
           title='Top Repositories by Stars',
           orientation='h',
           labels={'Number of Stars': 'Number of Stars', 'Repository Name': 'Repository Name'},
           color='Number of Stars',
           color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(img, use_container_width=True)

    df=data[['Number of Stars','Number of Forks', 'Number of Open Issues']]
    corr_matrix = df.corr()
    img = px.imshow(
        corr_matrix,
        labels=dict(color="Correlation"),
        color_continuous_scale='Viridis',
        title='Correlation Heatmap'
    )
    st.plotly_chart(img, use_container_width=True)



