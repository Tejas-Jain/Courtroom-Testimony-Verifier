import streamlit as st
import random
import pandas as pd
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


def mainpage():
    st.title("Courtroom Testimonies Verifier :scales:")
    st.subheader("Give Courtroom Testimonies and Find AI based truthfulness score with inconsistencies")
    
    # col1, col2 = st.columns([4, 1])

    # def inconsistencies():

    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )

    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True,
    )

def main():
    st.set_page_config(page_title="Courtroom Testimonies Verifier",page_icon=":scales:")
    sidebar()
    mainpage()



if __name__ == '__main__':
    main()