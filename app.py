import streamlit as st

def main():
    st.set_page_config(page_title="Courtroom Testimonies Verifier",
                       page_icon=":scales:")
    st.title("Courtroom Testimonies Verifier :scales:")
    st.subheader("Give Courtroom Testimonies and Find AI based truthfulness score with inconsistencies")

    with st.sidebar:
        "# Testimonies"
        def TestimoniesInput(party, placeholderTestimony):
            f"### {party}"
            text = st.text_area(f"Enter the testimony of the case from {party}'s side")
            return text
        
        victimTestimony = TestimoniesInput("Victim", "Enter the testimony of the case from Victim's side")
        accusedTestimony = TestimoniesInput("Accused", "Enter the testimony of the case from Accused's side")
        policeTestimony = TestimoniesInput("Police", "Enter the testimony of the case from Police's side")
        
        # #Witness Button [ Hiding to simplify the UI and Primary Logic]
        # if "button" not in st.session_state:
        #         st.session_state.button = False
        # witnessTestimonies = ""          
        # if st.button("Add Witness", key="witnessBtn", disabled=st.session_state.button): 
        #     st.session_state.button = True
        #     witnessTestimonies = TestimoniesInput("Witness", "Enter the testimony of the case from Witness 1's side")
        
        # if st.button("Process", type="primary"):
        #     with st.spinner("Processing"):
        #         print("Processing")



if __name__ == '__main__':
    main()