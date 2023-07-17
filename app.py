import streamlit as st
import random
import pandas as pd
from langchain.text_splitter import CharacterTextSplitter
from backend import mis_matches

if "processed" not in st.session_state:
    st.session_state.processed = False

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
            f"### {party} ###"
            text = st.text_area(f"Enter the testimony of the case from {party}'s side", value=placeholderTestimony)
            return text
        
        def split_text(text):
            return [sentence for sentence in text.split(".") if sentence.strip()]
        
        st.session_state.victimChunks = split_text(TestimoniesInput("Victim", "Enter the testimony of the case from Victim's side."))
        st.session_state.accusedChunks = split_text(TestimoniesInput("Accused", "Enter the testimony of the case from Accused's side."))
        st.session_state.policeChunks = split_text(TestimoniesInput("Police", "Enter the testimony of the case from Police's side."))


        def clickProcess():
            with st.spinner("Un-believably Complex Computation Going On!!! Please Wait..."):
                st.session_state.process_clicked = True
                st.session_state.accused_doubts = mis_matches(st.session_state.policeChunks, st.session_state.accusedChunks, 0)
                st.session_state.victim_doubts = mis_matches(st.session_state.policeChunks, st.session_state.victimChunks, 0)
                st.balloons()
                
        

        st.button("Process", type="primary", on_click=clickProcess)
                

 
                


def mainpage():
    st.title("Courtroom Testimonies Verifier :scales:")
    st.subheader("Give Courtroom Testimonies and Find AI based truthfulness score with inconsistencies")

    def get_mismatch_string(party_name, party_chunks, evid_chunks, doubts):
        print(doubts)
        return ("").join([
            f"<b>{party_name}:</b> {party_chunks[doubt[0]]} <br> <b>Evidence:</b> <i>{evid_chunks[doubt[1]]}</i> <br><br>" 
            for doubt in doubts
        ])
    
    if st.session_state.process_clicked:
        df = pd.DataFrame(
            {
                "Party": ["Accused", "Victim"],
                "DoubtFulStatements": [
                    get_mismatch_string("Accused", st.session_state.victimChunks, st.session_state.policeChunks, st.session_state.victim_doubts),
                    get_mismatch_string("Victim", st.session_state.accusedChunks, st.session_state.policeChunks, st.session_state.accused_doubts)
                ],
                "stars": [random.randint(0, 1000) for _ in range(2)]
            }
        )
        html_table = df.to_html(classes='table', escape=False, index=False)
        styled_html_table = html_table.replace('<table', '<table style="text-align: left"')
        st.write(styled_html_table, unsafe_allow_html=True)
    else:
        st.header("Enter the Testimonies on Left side panel")

def main():
    st.set_page_config(page_title="Courtroom Testimonies Verifier",page_icon=":scales:")
    if "process_clicked" not in st.session_state:
        st.session_state.process_clicked = False
    sidebar()
    mainpage()



if __name__ == '__main__':
    main()