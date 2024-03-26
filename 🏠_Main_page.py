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




    st.title("Welcome to My Portfolio Page")
    st.write("This is a webpage about myself, showcasing my description and projects.")

    # About Me Section
    st.header("About Me")
    st.write("""

    I am Nikoloz Shubladze, and my journey spans from the competitive waters of professional water polo to the intricate world of data science. For fifteen years, I dedicated myself to mastering the sport, representing Georgia's national team and esteemed clubs like Dinamo Tbilisi on the European stage. The Champions League was my battleground, where I left my mark with stellar performances.

    My achievements in sports are a testament to my dedication. I clinched the Georgian championship six times, secured third place in the Montenegro championship twice, and garnered numerous accolades including MVP and best goalkeeper titles. With the national team, we achieved remarkable milestones, propelling Georgia to the 8th position in Europe and 10th in the world—an extraordinary feat for our small country.

    Transitioning from the pool to academia, I pursued a Bachelor's degree in Computer Engineering, laying the groundwork for my venture into the world of technology. Over the past two years, I immersed myself in coding, mastering languages like HTML, CSS, JavaScript, Python, and C++. My hunger for knowledge led me to complete an intensive Data Science & AI boot camp, clocking in 400 hours of rigorous training.

    Today, I channel my passion for problem-solving and analytical thinking into my role as a Data Scientist. My diverse background—forged in the crucible of sports and academia—shapes my unique perspective, blending discipline, strategic thinking, and technical expertise.

    In Berlin, amidst a vibrant tech scene, I continue to thrive, embracing new challenges and pushing the boundaries of what's possible in data science. My journey stands as a testament to the transformative power of pursuing one's passions and embracing lifelong learning.
    """)


if __name__ == "__main__":
    main()
