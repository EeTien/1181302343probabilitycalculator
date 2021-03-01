#main
import streamlit as st
import credit
import loan
import help

def main():
    page = st.sidebar.selectbox("Choose a page", ["Credit Card", "Loan", "Help"])

    if page == "Credit Card":
        credit.credit()
    elif page == "Loan":
        loan.loan()
    elif page == "Help":
        help.help()
main()