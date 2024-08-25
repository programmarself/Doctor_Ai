import streamlit as st

def admin_management():
    st.title("Admin Management")

    menu = st.sidebar.radio("Menu", ["Approve New Doctor Profiles", "Monitor Interactions", "Handle Disputes", "Compliance"])

    if menu == "Approve New Doctor Profiles":
        st.subheader("Approve New Doctor Profiles")
        st.write("Approve or reject new doctor profiles here.")

    elif menu == "Monitor Interactions":
        st.subheader("Monitor Doctor-Patient Interactions")
        st.write("Monitor interactions between doctors and patients.")

    elif menu == "Handle Disputes":
        st.subheader("Handle Disputes")
        st.write("Manage any disputes or issues.")

    elif menu == "Compliance":
        st.subheader("Compliance")
        st.write("Ensure compliance with medical regulations.")

if __name__ == "__main__":
    admin_management()
