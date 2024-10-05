import streamlit as st

def portfolio():
    st.markdown('''
        <div style="background: linear-gradient(to left, #800080, #ff69b4); padding: 0px; border-radius: 50px; width:50%"  display: flex; align-items: center;>
            <h1 style="color:#FFF; text-align: center;">Vinoth Palanivel's Portfolio</h1>
        </div><br>
        ''',
        unsafe_allow_html=True)
    st.subheader("Welcome to my personal portfolio!")

    st.header("About Me")
    st.write("""
    Hello! I'm Vinoth Palanivel, a Data Scientist based in Chennai. 
    I have a passion for Data Science, Machine Learning.
    """)


    st.header("Skills")
    st.write("<h5>Technical:</h5>", unsafe_allow_html=True)
    skills = ["Python", "Data Analysis", "Web Development", "Machine Learning", "Deep Learning", "Java"]
    st.write(", ".join(skills))

    st.write("<h5>Databases:</h5>", unsafe_allow_html=True)
    skills = ["MySql", "MongoDB", "CosmosDB"]
    st.write(", ".join(skills))


    st.write("<h5>Framework:</h5>", unsafe_allow_html=True)
    skills = ["Pandas", "Numpy", "Matplotlib","Seaborn","Scikit-Lear","TensorFlow","Streamlit", "Django", "PLotly" ]
    st.write(", ".join(skills))

    st.header("Contact Me")
    st.write("""
    Feel free to reach out to me via:
    - Email: [Gmail](vinothchennai97@gmail.com)
    - Mobile: 7904197698 
    """)

    st.header("Connect with Me")
    st.write("""
    [GitHub](https://github.com/Vinoth0208/) |
    [LinkedIn](https://linkedin.com/in/vinoth-palanivel-265293211)
    """)

