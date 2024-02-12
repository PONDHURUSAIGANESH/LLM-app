import streamlit as st

st.set_page_config(
    page_title="LLM app",
    page_icon="✍",
)

st.title("Hey Viewers!")
st.write(""" Unveiling the Hidden: Master both Text and Image with the Powerful Search Engine!

Tired of sifting through endless text or blurry images? Craving a search engine that understands your every nuance, whether you whisper a phrase or upload a picture? Look no further! I've harnessed the power of cutting-edge LLM (Large Language Model) technology to bring you a revolutionary dual-faceted search experience.

**Textual Sleuth:**

* **Unleash the wordsmith within:** Craft your query with precision, be it a simple keyword or an intricate sentence. This LLM model delves deep into the vast ocean of text, unearthing the information you seek with uncanny accuracy. 
* **Navigate the semantic labyrinth:** Don't just find the needle in the haystack, understand its context. This model deciphers the relationships between words, concepts, and entities, ensuring you grasp the true meaning behind every result.

**Visual Detective:**

* **Speak the language of pictures:** Forget clumsy keyword descriptions. Upload an image, any image, and this LLM model will decipher its visual elements, from objects and colors to scenes and emotions.
* **Find the needle in the image haystack:** Lost in a sea of similar visuals? This model goes beyond basic image recognition, understanding the relationships and context within the image to deliver relevant results.
* **Reverse image search:** Can't place that intriguing picture? Upload it, and model will scour the web to find its origin, similar visuals, and any associated information.

**A World of Knowledge Awaits:**

But wait, there's more! Seamlessly navigate between my dedicated text and image search pages, accessible right from this very interface. Each page is designed to empower your specific search inquiries, providing a tailored experience for both textual and visual exploration.

**Ready to embark on a journey of discovery?** Click the "TEXT" button to delve into the written word, or choose "IMAGE" to unlock the secrets hidden within pixels. This LLM-powered engine awaits, eager to serve as your guide through the boundless realms of information.


**I have attached the contact form, if you have any queries then write a message and send to me!!**
* **Credits to GoogleGenerativeAI** 

""")
st.sidebar.success("select a page above")

st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/pondhurusaiganesh@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/styles.css")