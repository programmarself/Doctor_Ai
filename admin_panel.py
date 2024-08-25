import streamlit as st

def admin_panel():
    st.title("Admin Panel")

    menu = st.sidebar.radio("Menu", ["Manage Doctors", "Monitor Appointments", "Billing and Payments", "Update Content"])

    if menu == "Manage Doctors":
        st.subheader("Manage Doctors")
        st.write("Add, edit, or delete doctor profiles here.")

    elif menu == "Monitor Appointments":
        st.subheader("Monitor Appointments")
        st.write("View and manage appointments.")

    elif menu == "Billing and Payments":
        st.subheader("Billing and Payments")
        st.write("Handle billing and payments here.")

    elif menu == "Update Content":
        st.subheader("Update Website Content")
        st.write("Update the content on the website.")

if __name__ == "__main__":
    admin_panel()
