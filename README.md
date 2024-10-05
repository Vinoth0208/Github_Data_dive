# Github_Data_dive
 Career-fair guvi Data analysis project


## Skills Taken Away From This Project
* Python
* GitHub API
* Pandas
* SQL
* Streamlit
* Data Analysis
* Data Visualization
## Domain
### Open Source Software Analytics

## Problem Statement
In today's rapidly evolving software development landscape, GitHub serves as a pivotal platform for collaboration and innovation within the open-source community. With millions of repositories available, identifying relevant projects and understanding development trends can be challenging for developers, researchers, and organizations alike. This project aims to extract and analyze data from GitHub repositories focused on specific topics to uncover patterns and trends in repository characteristics, popularity, and technology usage.

By leveraging the GitHub API, this project provides a comprehensive overview of repository dynamics, including metrics like stars, forks, programming languages, and creation dates. The ultimate goal is to create a user-friendly Streamlit application that visualizes these insights, enabling users to make informed decisions regarding project collaboration, technology adoption, and educational resource identification in the open-source ecosystem.

Business Use Cases
Developers can find trending repositories for collaboration or inspiration.
Organizations can analyze the popularity and activity of repositories related to their technologies.
Educators and researchers can explore open-source projects for teaching or study materials.

## Approach
* Data Extraction
* Utilize the GitHub API to fetch repository data based on 10 currently trending topics in the data world, such as:

  * Machine Learning
  * Data Visualization
  * Deep Learning


* The following data fields will be extracted:

    Repository Name: Name of the repository.
    Owner: Username of the repository owner.
    Description: Brief description of the repository.
    URL: Link to the repository.
    Programming Language: Primary language used in the repository.
    Creation Date: Date when the repository was created.
    Last Updated Date: Date of the last update to the repository.
    Number of Stars: Count of stars received by the repository.
    Number of Forks: Count of times the repository has been forked.
    Number of Open Issues: Count of open issues in the repository.
    License Type: Type of license under which the repository is released.

## Data Cleaning
Handle missing values and ensure data consistency by standardizing formats.

## Data Storage
Save the cleaned data in a SQL database for efficient access.

## Data Analysis
Analyze the dataset to uncover trends, such as popular programming languages and repository activity.

## Visualization
Build an interactive Streamlit application to display insights visually and allow user interaction.