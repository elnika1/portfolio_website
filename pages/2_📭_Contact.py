import streamlit as st

person =  {"name": "Nikoloz",
           "surname": "Shubladze",
           "picture_url": "https://media.licdn.com/dms/image/D4E03AQE1j5QUNY5uJw/profile-displayphoto-shrink_800_800/0/1708612775913?e=1715817600&v=beta&t=VCKmLPnPcKP2CGPoC5npaKT5TdYgoDaemh5pYgGingM",
           "title": "Data Scientist",
           "linkedin_url": "https://www.linkedin.com/in/nikolozshubladze/",
           "github_url": "https://github.com/elnika1"}

def main():

    st.sidebar.markdown(f'<img src="{person["picture_url"]}" alt="{person["name"]} {person["surname"]}" style="width: 200px; height: 200px; border-radius: 50%;">', unsafe_allow_html=True)
    st.sidebar.markdown(f"<h2>{person['name']} {person['surname']}</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(f'<p> {person["title"]}</p>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<p><a href="{person["linkedin_url"]}" target="_blank">LinkedIn</a></p>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<p><a href="{person["github_url"]}" target="_blank">GitHub</a></p>', unsafe_allow_html=True)


    # Contact Information
    st.header("Contact Information")
    st.write("Feel free to reach out to me via email at shubnika1@gmail.com ")




if __name__ == "__main__":
    main()
