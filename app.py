import requests
import streamlit as st
from streamlit_lottie import st_lottie

# find more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(ur1) :
    r = requests.get(ur1)
    if r.status_code != 200 :
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_az0MhjvO6G.json")

 # ----HEADER SECTION ----
with st.container():
    st.title("Hi, I am Janvi :wink:")
    st.title("A student from India")
    st.write("I am passionate about finding ways to use python and learning new things")
    st.write("[Learn More >](https://thefirstwebjv.netlify.app/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column :
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Hello! :wave: 

            My friends :blue_heart:

            My name's Janvi and I'm a student I study in 9th standard this is my first website using my favrioute language (PYTHON) this is soo friendly language. By the way I love to code and making somthing new.I love to learning new things.

            
            
            I have many friends, and they are so special for me. And this people are fucking nice. :sweat_smile: :joy: below I have named my friends and there's special emoji with it :
           
            Aarti (aarti uutaru) :innocent: 

            Akshat (Akshu) :turtle::stuck_out_tongue: 

            Heena (MD, bano ji) :heartpulse::kissing:

            Kartik (KK) :grinning:

            Manya (elnino) :relieved:

            Muskan (madem ji) :mouse::ear: :grimacing::

            Rajnish ? :neutral_face:

            Nishita (niki) :heartbeat::two_women_holding_hands: 

            shivani (shanu) :two_hearts::two_women_holding_hands:

            Yuvraj (yuvi) :wink: :v:
            """
             )

    with right_column :
        st_lottie(lottie_coding, height=300, key="coding")


 

     


    
