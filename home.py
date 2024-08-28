import streamlit as st

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

# Display the same content for all pages
st.title("Welcome to the Universal Page")
st.write("""
    No matter what option you choose, this is the content you'll see.
    You can customize this page to display whatever information you want to show.
""")

# Example content you can show on this page
st.subheader("Some Universal Information")
st.write("This could be a dashboard, a report, or any other content you'd like to present universally.")

# Placeholder for additional features
st.write("Here, you could add any other features that you want all users to have access to.")
