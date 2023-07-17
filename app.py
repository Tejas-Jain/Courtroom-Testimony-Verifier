import streamlit as st
import random
import pandas as pd
from langchain.text_splitter import CharacterTextSplitter
from backend import mis_matches

accusedSample = "I want to provide the facts regarding the car accident. At the time of the incident, I was driving a red SUV, traveling in the westbound direction. The other vehicle involved was a blue sedan. I want to emphasize that I was following the traffic rules and driving within the speed limit. I did not engage in any reckless behavior that could have caused the collision. The collision was an unfortunate event, and I believe a thorough investigation will reveal the true cause."
victimSample = "I want to present the factual details of the car accident. I was driving a blue sedan, traveling in the northbound direction. The other driver's vehicle was a red SUV. I had the right of way and was adhering to the traffic signals. The collision occurred when the red SUV, driven by the accused, collided with the side of my vehicle. I want to stress that I was driving cautiously and responsibly at the time of the accident."
policeSample = "According to the available evidence, the car accident involved a collision between a red SUV and a blue sedan at the intersection. The red SUV, driven by the accused, was traveling westbound, while the blue sedan was heading northbound. The impact of the collision resulted in visible damage to both vehicles. We will conduct a thorough investigation to determine the exact cause of the accident, taking into account all the hard facts and supporting evidence."

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
            text = st.text_area(f"Enter {party}'s testimony:", value=placeholderTestimony)
            
            return text
        
        def split_text(text):
            return [sentence for sentence in text.split(".") if sentence.strip()]
        
        st.session_state.victimChunks = split_text(TestimoniesInput("Victim 🤕", victimSample))
        st.session_state.accusedChunks = split_text(TestimoniesInput("Accused 😡", accusedSample))
        st.session_state.policeChunks = split_text(TestimoniesInput("Police 👮", policeSample))
        st.session_state.tolerance = st.number_input("Enter the tolerance in contradictions:", value=70, min_value=0, max_value=100, step=1)

        def clickProcess():
            with st.spinner("Un-believably Complex Computation Going On! Hold On Tight..."):
                st.session_state.process_clicked = True
                st.session_state.accused_doubts = mis_matches(st.session_state.policeChunks, st.session_state.accusedChunks, st.session_state.tolerance/100)
                st.session_state.victim_doubts = mis_matches(st.session_state.policeChunks, st.session_state.victimChunks, st.session_state.tolerance/100)
                st.balloons()
                
        

        st.button("Process", type="primary", on_click=clickProcess)
                

 
                


def mainpage():
    st.title("Courtroom Testimonies Verifier :scales:")
    st.subheader("Give Courtroom Testimonies and Find AI based truthfulness score with inconsistencies")

    def get_mismatch_string(party_name, party_chunks, evid_chunks, doubts):
        return ("").join([
            f"<b>{party_name}:</b> {party_chunks[doubt[0]]} <br> <b>👮:</b> <i>{evid_chunks[doubt[1]]}</i> <br><br>" 
            for doubt in doubts
        ])
    def calculate_truth(doubts):
        sum = 0.0
        for doubt in doubts:
            sum += doubt[2]
        ans = round(sum/len(doubts)*100, 2)
        if ans==0:
            return
        return ans

    if st.session_state.process_clicked:
        df = pd.DataFrame(
            {
                "<th><strong>Parties</strong></th>": ["<b>Accused</b>", "<b>Victim</b>"],
                "<th><b>DoubtFulStatements</b></th>": [
                    get_mismatch_string("😡", st.session_state.victimChunks, st.session_state.policeChunks, st.session_state.victim_doubts),
                    get_mismatch_string("🤕", st.session_state.accusedChunks, st.session_state.policeChunks, st.session_state.accused_doubts)
                ],
                "<th><b>Truthfulness %<br> (Based on AI Semantic Analysis)</th>": [
                    calculate_truth(st.session_state.victim_doubts), 
                    calculate_truth(st.session_state.accused_doubts)
                ]
            }
        )
        html_table = df.to_html(classes='table', escape=False, index=False)
        styled_html_table = html_table.replace('<table', '<table style="text-align: left"')
        st.write(styled_html_table, unsafe_allow_html=True)
    else:
        "## 👈Enter the Testimonies"
        "## OR ##"
        "## Try A Sample Case... ##"

def main():
    st.set_page_config(page_title="Courtroom Testimonies Verifier",page_icon=":scales:")
    if "process_clicked" not in st.session_state:
        st.session_state.process_clicked = False
    sidebar()
    mainpage()



if __name__ == '__main__':
    main()