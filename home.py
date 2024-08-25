import streamlit as st

def home():
    st.title("Healthcare Service")
    st.header("Welcome to Our Health Portal")
    st.write("Explore our services, meet our doctors, and stay updated with our health blog.")

    menu = st.sidebar.radio("Menu", ["Home", "About Us", "Services", "Contact", "Health Blog"])

    if menu == "Home":
        st.subheader("Home")
        st.write("Information about our healthcare services and mission.")
    elif menu == "About Us":
        st.subheader("About Us")
        st.write("Learn more about our organization and values.")
    elif menu == "Services":
        st.subheader("Services")
        st.write("Detailed information about the services we offer.")
    elif menu == "Contact":
        st.subheader("Contact Us")
        st.write("How to get in touch with us.")
    elif menu == "Health Blog":
        st.subheader("Health Blog")
        st.write("Read our latest health-related articles.")

if __name__ == "__main__":
    home()
