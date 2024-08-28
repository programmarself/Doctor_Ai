import streamlit as st
import pandas as pd
import numpy as np

# Placeholder for API keys and sensitive data
API_KEY = 'your_api_key_here'  # Replace with your actual API key

# Function to simulate a chatbot response
def chatbot_response(query):
    if 'symptom' in query.lower():
        return "Based on your symptoms, you may need to consult a doctor for a precise diagnosis."
    elif 'medication' in query.lower():
        return "Please consult a healthcare professional for personalized medication recommendations."
    else:
        return "I'm not sure how to help with that. Please contact a doctor for more information."

# Create a Top Navigation Bar
st.markdown("""
    <style>
        .navbar {
            overflow: hidden;
            background-color: #333;
            font-family: Arial, Helvetica, sans-serif;
        }

        .navbar a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }

        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }

        .navbar a.active {
            background-color: #04AA6D;
            color: white;
        }

        .container {
            padding: 20px;
        }
    </style>
    <div class="navbar">
        <a class="active" href="?page=home">Home</a>
        <a href="?page=about_us">About Us</a>
        <a href="?page=services">Services</a>
        <a href="?page=contact">Contact</a>
        <a href="?page=health_blog">Health Blog</a>
        <a href="?page=client_interface">Client Interface</a>
        <a href="?page=admin_panel">Admin Panel</a>
        <a href="?page=chatbot">Chatbot</a>
        <a href="?page=new_doctor_profiles">New Doctor Profiles</a>
        <a href="?page=admin_management">Admin Management</a>
    </div>
    """, unsafe_allow_html=True)

# Function to handle navigation
def get_page():
    query_params = st.experimental_get_query_params()
    if "page" in query_params:
        return query_params["page"][0]
    else:
        return "home"

# Fetch the selected page
page = get_page()

# Home Page
if page == "home":
    st.title("Welcome to HealthCare Center")
    st.image("doctor ai.png")
    st.write("Providing the best healthcare services for you and your family.")

# About Us Page
elif page == "about_us":
    st.title("About Us")
    st.write("We are committed to providing excellent healthcare services with a team of experienced professionals dedicated to your well-being.")

# Services Page
elif page == "services":
    st.title("Our Services")
    st.write("We offer a range of medical services including general consultations, specialist care, emergency services, and more.")

# Contact Page
elif page == "contact":
    st.title("Contact Us")
    st.write("Get in touch with us through email, phone, or visit our office.")
    st.write("Email: contact@healthcare.com")
    st.write("Phone: +1 234 567 890")
    st.write("Address: 123 Health St, Wellness City")

# Health Blog Page
elif page == "health_blog":
    st.title("Health Blog")
    st.write("Read our latest articles on health and wellness. Stay informed with expert advice and tips for a healthier lifestyle.")

# Client Interface Page
elif page == "client_interface":
    st.title("Client Interface")
    
    # Search for Doctors
    st.subheader("Search for Doctors")
    search_term = st.text_input("Search for doctors based on specialty, location, or availability")
    if search_term:
        st.write(f"Searching for doctors with the term: {search_term}")
        # Here you would implement actual search logic with backend

    # Book an Appointment
    st.subheader("Book an Appointment")
    st.write("To book an appointment, please select a doctor and choose a time slot.")
    doctor_name = st.selectbox("Select Doctor", ["Dr. Smith", "Dr. Johnson", "Dr. Lee"])  # Replace with dynamic list
    appointment_date = st.date_input("Select Date")
    appointment_time = st.time_input("Select Time")
    if st.button("Book Appointment"):
        st.write(f"Appointment booked with {doctor_name} on {appointment_date} at {appointment_time}.")
        # Here you would integrate actual booking logic with backend

    # Access Medical History and Prescriptions
    st.subheader("Access Medical History and Prescriptions")
    st.write("Please log in to securely view your medical history and prescriptions.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        st.write("Login successful. Displaying your medical history and prescriptions.")
        # Here you would integrate actual login and data fetching logic with backend

    # Receive Notifications and Reminders
    st.subheader("Receive Notifications and Reminders")
    st.write("Manage your notifications and reminders for upcoming appointments and medication.")
    st.write("To receive notifications, ensure your contact details are up-to-date in your profile.")
    # Here you would integrate actual notification management with backend

# Admin Panel Page
elif page == "admin_panel":
    st.title("Admin Panel")
    st.write("Welcome to the admin dashboard.")
    admin_action = st.selectbox("Select Action", [
        "Manage Doctors", "Monitor Appointments", "Handle Billing", "Update Content"
    ])
    
    if admin_action == "Manage Doctors":
        st.write("Add, edit, or delete doctor profiles here.")
        # Implement functionality to manage doctors

    elif admin_action == "Monitor Appointments":
        st.write("View and manage appointments.")
        # Implement functionality to monitor appointments

    elif admin_action == "Handle Billing":
        st.write("Manage billing and payments.")
        # Implement functionality for billing and payments

    elif admin_action == "Update Content":
        st.write("Update website content.")
        # Implement functionality to update content

# Chatbot Page
elif page == "chatbot":
    st.title("Chatbot for Medication Suggestions")
    user_query = st.text_input("Ask the chatbot:")
    if user_query:
        response = chatbot_response(user_query)
        st.write(f"Chatbot: {response}")

# New Doctor Profiles Page
elif page == "new_doctor_profiles":
    st.title("New Doctor Profiles")
    doctor_name = st.text_input("Doctor's Name")
    doctor_specialty = st.text_input("Specialty")
    doctor_availability = st.text_input("Availability")
    doctor_fee = st.number_input("Consultation Fee")
    doctor_photo = st.file_uploader("Upload Photo", type=["jpg", "png"])
    doctor_bio = st.text_area("Bio")
    doctor_social_media = st.text_input("Social Media Links")
    
    if st.button("Submit Profile"):
        st.write("Doctor profile submitted for approval.")
        # You would typically save this information to a database

# Admin Management Page
elif page == "admin_management":
    st.title("Admin Management")
    st.write("Manage doctor profiles, monitor interactions, handle disputes, and ensure compliance.")
    st.write("This section is restricted to authorized admins.")
    
    st.subheader("Approve New Doctor Profiles")
    st.write("Review and approve or reject new doctor profiles submitted.")

    st.subheader("Monitor Doctor-Patient Interactions")
    st.write("Oversee interactions between doctors and patients to ensure quality and compliance.")

    st.subheader("Handle Disputes or Issues")
    st.write("Address and resolve any disputes or issues that arise.")

    st.subheader("Ensure Compliance")
    st.write("Ensure all practices are in line with medical regulations and standards.")
