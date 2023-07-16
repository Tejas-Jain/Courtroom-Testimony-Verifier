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

    df = pd.DataFrame(
        {
            "Party": ["Accused", "Victim", "Evidence"],
            "DoubtFulStatements": [
f"""
Original: He said something\n
Mis-Match: "They said something else

Original: He said something\n
Mis-Match: "They said something else
\n\n
Original: He said something
Mis-Match: "They said something else
""", 
f"""
Original: He said something 
Mis-Match: "They said something else

Original: He said something 
Mis-Match: "They said something else

Original: He said something 
Mis-Match: "They said something else
""",
f"""
Original: He said something 
Mis-Match: "They said something else

Original: He said something 
Mis-Match: "They said something else

Original: He said something 
Mis-Match: "They said something else
"""

            ],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            # "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    # pd.set_option('display.max_colwidth', None)
# [
#                 {
#                     "Original Statement1: ": "He said something",
#                     "Mis-Match1": "They said something else"
#                 }, 
#                 {
#                     "Original Statement2: ": "He said something",
#                     "Mis-Match2": "They said something else"
#                 }, 
#                 {
#                     "Original Statement3: ": "He said something",
#                     "Mis-Match3": "They said something else"
#                 }, 
#             ]

    # # Create a DataFrame with a multiline string
    # data = {
    #     'Name': ['Alice', 'Bob'],
    #     'Description': ['This is a<br>multiline\nstring.', 'Another\nmultiline\nstring.']
    # }
    
    # df = pd.DataFrame(data)
    # pd.set_option('display.max_colwidth', None)
    # print(df)
    # # # Display the DataFrame with multiline strings
    # st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    # data = {
    #     'Name': ['Alice', 'Bob'],
    #     'Description': ['This is a\nmultiline\nstring.', 'Another\nmultiline\nstring.']
    # }

    # df = pd.DataFrame(data)

    # # Adjust display options
    # pd.set_option('display.max_colwidth', None)  # Display full contents of each cell

    # # Print the DataFrame
    # print(df)
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐"
            ),
            # "url": st.column_config.LinkColumn("App URL"),
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