import streamlit as st

def client_interface():
    st.title("Client Interface")

    menu = st.sidebar.radio("Menu", ["Search Doctors", "Book Appointment", "Medical History", "Notifications"])

    if menu == "Search Doctors":
        st.subheader("Search for Doctors")
        specialty = st.text_input("Specialty")
        location = st.text_input("Location")
        availability = st.text_input("Availability")
        st.button("Search")

    elif menu == "Book Appointment":
        st.subheader("Book an Appointment")
        doctor_name = st.text_input("Doctor's Name")
        appointment_date = st.date_input("Appointment Date")
        st.button("Book Appointment")

    elif menu == "Medical History":
        st.subheader("Medical History")
        st.write("Access your medical history here.")

    elif menu == "Notifications":
        st.subheader("Notifications")
        st.write("View your notifications and reminders.")

if __name__ == "__main__":
    client_interface()
