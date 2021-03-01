import streamlit as st

def help():
    st.title("Data dictionary")

    st.header("Loan")
    st.subheader("Term")
    st.write("0: Long term  1: Short term")
    st.subheader("Years in current job")
    st.write("0: 1 year 1: 10+ years")
    st.write("Other years follow its value")
    st.subheader("Home Ownership")
    st.write("0: Home Mortgage  1: Own Home    2: Rent")
