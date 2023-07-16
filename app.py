import streamlit as st
import random
import pandas as pd
from langchain.text_splitter import CharacterTextSplitter



def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator='.',
        chunk_size=40,
        chunk_overlap=10,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def sidebar():
    with st.sidebar:
        "# Testimonies"
        def TestimoniesInput(party, placeholderTestimony):
            f"### {party}"
            text = st.text_area(f"Enter the testimony of the case from {party}'s side")
            return text
        
        victimTestimony = TestimoniesInput("Victim", "Enter the testimony of the case from Victim's side")
        accusedTestimony = TestimoniesInput("Accused", "Enter the testimony of the case from Accused's side")
        policeTestimony = TestimoniesInput("Police", "Enter the testimony of the case from Police's side")


        if st.button("Process", type="primary"):
            with st.spinner("Processing"):
                print("Processing")
                st.session_state.victimChunks = victimTestimony.split(".")
                st.session_state.accusedChunks = accusedTestimony.split(".")
                st.session_state.policeChunks = policeTestimony.split(".")
                


def mainpage():
    st.title("Courtroom Testimonies Verifier :scales:")
    st.subheader("Give Courtroom Testimonies and Find AI based truthfulness score with inconsistencies")
    st.write(st.session_state.accusedChunks)
#     df = pd.DataFrame(
#         {
#             "Party": ["Accused", "Victim", "Evidence"],
#             "DoubtFulStatements": [
# f"""
# Original: He said something\n
# Mis-Match: "They said something else

# Original: He said something\n
# Mis-Match: "They said something else
# \n\n
# Original: He said something
# Mis-Match: "They said something else
# """, 
# f"""
# Original: He said something 
# Mis-Match: "They said something else

# Original: He said something 
# Mis-Match: "They said something else

# Original: He said something 
# Mis-Match: "They said something else
# """,
# f"""
# Original: He said something 
# Mis-Match: "They said something else

# Original: He said something 
# Mis-Match: "They said something else

# Original: He said something 
# Mis-Match: "They said something else
# """

#             ],
#             "stars": [random.randint(0, 1000) for _ in range(3)]
#         }
#     )
#     st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Courtroom Testimonies Verifier",page_icon=":scales:")
    sidebar()
    mainpage()



if __name__ == '__main__':
    main()