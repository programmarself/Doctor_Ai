import streamlit as st

def new_doctor():
    st.title("New Doctor Profile")

    with st.form(key='doctor_form'):
        name = st.text_input("Name")
        credentials = st.text_input("Credentials")
        specialties = st.text_input("Specialties")
        availability = st.text_input("Availability")
        consultation_fee = st.number_input("Consultation Fee", min_value=0)
        photo = st.file_uploader("Upload Photo", type=["jpg", "png"])
        bio = st.text_area("Bio")
        social_media_links = st.text_input("Social Media Links")

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write("Doctor profile submitted!")
            # Handle profile submission here

if __name__ == "__main__":
    new_doctor()
