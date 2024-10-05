import requests
import pandas as pd



def preprocessdata(topics, Api_Key):
    base_url = 'https://api.github.com'
    finaldf=[]
    for i in topics:

        url = f'{base_url}/search/repositories?q={i}&sort=stars&order=desc'

        headers = {'Authorization': f'token {Api_Key}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            out = response.json().get('items', [])

        df = pd.DataFrame(out)
        print(df)
        print(df.columns)
        print(df.info())

        df_new = df[['name', 'owner', 'description', 'url', 'language', 'created_at', 'updated_at', 'stargazers_count',
                     'forks_count', 'open_issues_count', 'private']]

        print(df_new)
        print(df_new.isna().sum())

        df_new['name'] = df_new['name'].fillna(df_new['name'].mode()[0])
        df_new['owner'] = df_new['owner'].fillna(df_new['owner'].mode()[0])
        df_new['description'] = df_new['description'].fillna("No description available")
        df_new['url'] = df_new['url'].fillna(df_new['url'].mode()[0])
        df_new['created_at'] = df_new['created_at'].fillna(df_new['created_at'].mode()[0])
        df_new['updated_at'] = df_new['updated_at'].fillna(df_new['updated_at'].mode()[0])
        df_new['stargazers_count'] = df_new['stargazers_count'].fillna(df_new['stargazers_count'].mode()[0])
        df_new['forks_count'] = df_new['forks_count'].fillna(df_new['forks_count'].mode()[0])
        df_new['open_issues_count'] = df_new['open_issues_count'].fillna(df_new['open_issues_count'].mode()[0])
        df_new['language'] = df_new['language'].fillna(df_new['language'].mode()[0])

        print(df_new.isna().sum())

        print(df_new)

        df_owner = list(df_new['owner'])
        df_owner = pd.DataFrame(df_owner)

        print(df_owner)
        print(df_owner.columns)

        df_new['Owner'] = df_owner['login']
        df_new['License Type'] = df_owner['type']
        df_new.drop(columns=['private', 'owner'], inplace=True)

        print(df_new)
        print(df_new.isna().sum())

        df_final = df_new[
            ['name', 'Owner', 'description', 'url', 'language', 'created_at', 'updated_at', 'stargazers_count',
             'forks_count', 'open_issues_count', 'License Type']]
        df_final.columns = ['Repository Name',
                            'Owner',
                            'Description',
                            'URL',
                            'Programming Language',
                            'Creation Date',
                            'Last Updated Date',
                            'Number of Stars',
                            'Number of Forks',
                            'Number of Open Issues',
                            'License Type']

        df_final['Description'] = df_final['Description'].str.lower().str.strip()
        df_final['Owner'] = df_final['Owner'].str.lower().str.strip()

        df_final['Number of Stars'] = df_final['Number of Stars'].astype(int)
        df_final['Number of Forks'] = df_final['Number of Forks'].astype(int)
        df_final['Number of Open Issues'] = df_final['Number of Open Issues'].astype(int)
        df_final['Creation Date'] = pd.to_datetime(df_final['Creation Date'])
        df_final['Last Updated Date'] = pd.to_datetime(df_final['Last Updated Date'])

        current_time = pd.Timestamp.now(tz='UTC')
        df_final['Repository Age (days)'] = (current_time - df_final['Creation Date']).dt.days
        df_final['Created Year'] = df_final['Creation Date'].dt.year
        finaldf.append(df_final)
        dffinal=pd.concat(finaldf, ignore_index=True)

    return (dffinal)