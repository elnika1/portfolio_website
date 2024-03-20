import streamlit as st

person =  {"name": "Nikoloz", "surname": "Shubladze", "picture_url": "https://media.licdn.com/dms/image/D4E03AQE1j5QUNY5uJw/profile-displayphoto-shrink_800_800/0/1708612775913?e=1715817600&v=beta&t=VCKmLPnPcKP2CGPoC5npaKT5TdYgoDaemh5pYgGingM", "title": "Data Scientist", "linkedin_url": "https://www.linkedin.com/in/nikolozshubladze/", "github_url": "https://github.com/elnika1"}

def main():
    st.sidebar.markdown('<div style="display: inline-block; margin: 20px; text-align: center;">', unsafe_allow_html=True)
    st.sidebar.markdown(f'<img src="{person["picture_url"]}" alt="{person["name"]} {person["surname"]}" style="width: 150px; height: 150px; border-radius: 50%;">', unsafe_allow_html=True)
    st.sidebar.markdown(f'<p><b>Title:</b> {person["title"]}</p>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<p><a href="{person["linkedin_url"]}" target="_blank">LinkedIn</a></p>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<p><a href="{person["github_url"]}" target="_blank">GitHub</a></p>', unsafe_allow_html=True)
    st.sidebar.markdown('</div>', unsafe_allow_html=True)

    st.title("Welcome to My Streamlit Page")
    st.write("This is a streaming webpage about myself, showcasing my description and projects.")

    # About Me Section
    st.header("About Me")
    st.write("""
    Hi there! I'm [Your Name], a passionate [Your Profession/Hobby] based in [Your Location].
    [Add more details about yourself here]
    """)

    # Projects Section
    st.header("Projects")
    st.subheader("Project 1: [Project Name]")
    st.write("""
    Description: [Brief description of your project]
    [Add images, videos, or links to your project here]
    """)

    st.subheader("Project 2: [Project Name]")
    st.write("""
    Description: [Brief description of your project]
    [Add images, videos, or links to your project here]
    """)

    # Streaming Schedule
    st.header("Streaming Schedule")
    st.write("Join me for live streams on [Days of the week] at [Time].")

    # Contact Information
    st.header("Contact Information")
    st.write("Feel free to reach out to me via email at [Your Email Address] or connect with me on [Social Media Platforms].")

if __name__ == "__main__":
    main()
