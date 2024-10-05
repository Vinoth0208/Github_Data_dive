import streamlit as st
def insights():
    st.markdown(
        '''
        <div style="background: linear-gradient(to left, #a3d68e, #ff1493); padding: 20px; border-radius: 5px;">
            <h1 style="color:#FFF; text-align: center;">Insights from The Github Data Dive</h1>
        </div><br>
        ''',
        unsafe_allow_html=True
    )

    st.title('1. Popular Repositories')
    st.write("""* awesome (sindresorhus)

Description: A comprehensive collection of curated lists on various topics. \n
License Type: User \n
Age: 3738 days (created in 2014)\n
Insight: This repository is a go-to for developers looking for curated resources across many fields, indicating a strong community and consistent relevance.""")

    st.write("""* system-design-primer (donnemartin)

Description: Focuses on teaching system design for large-scale applications.\n
Age: 2777 days (created in 2017)\n
Insight: This is valuable for software engineers preparing for technical interviews, showing a niche but significant user base.""")

    st.title('2. Popular Programming Languages')

    st.write("""* Python: Notable for its implementation of algorithms, making it a top choice for education and practical applications in data science and software development.""")
    st.write("""* JavaScript: Notable for creating dynamic, interactive web pages, enhancing user experience, and enabling real-time content updates without reloading the page in web development.""")

    st.title('3. Number of Stars and Forks for Popular programming language')

    st.write("""* Python leads the open-source landscape with over 2 million stars and nearly half a million forks, highlighting its vast community and versatility.""")
    st.write("""* while JavaScript follows with over half a million stars and 20,000 forks, underscoring its crucial role in web development.""")

    st.title('4. Repositories Count')
    st.write("* In 2016, the number of created repositories surged compared to previous years, driven by the rise of cloud computing, popular programming languages, and enhanced developer tools, reflecting a growing enthusiasm for collaborative open-source development.")

    st.title('5. Open issues vs Stars')
    st.write("* With nearly 186,000 stars and around 5,000 open issues, TensorFlow demonstrates strong community engagement and popularity, while also highlighting ongoing development and the need for improvements in its extensive ecosystem")

    st.title('6. License Type')
    st.write("* Approximately 65% of repositories are licensed under various types of licenses are organizations, while the remaining 35% are contributed by individual users, indicating a strong presence of institutional backing in the open-source community.")

    st.title('7. Correlation')
    st.write("* The correlation data reveals significant relationships among the three metrics. The strong correlation between stars and forks (0.79) suggests that repositories with higher visibility and popularity are frequently cloned by users, reflecting active engagement and interest. Conversely, the lower correlation with open issues (0.25 for stars and 0.36 for forks) indicates that while popular projects attract attention, they may not necessarily have a high volume of unresolved issues, suggesting effective management or community responsiveness in addressing concerns. Overall, this analysis underscores the dynamics of user engagement in the open-source ecosystem.")