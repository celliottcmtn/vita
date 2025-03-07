import streamlit as st
import pandas as pd

# Minimal test app
def main():
    st.title("Vitamin & Supplement Advisor")
    st.write("This is a test version to troubleshoot deployment issues.")
    
    st.subheader("Basic Information")
    age_group = st.selectbox("Select your age group:", ["20s", "30s", "40s", "50s", "60s", "70plus"])
    gender = st.selectbox("Select your gender:", ["female", "male"])
    
    st.write(f"You selected: Age group: {age_group}, Gender: {gender}")
    
    if st.button("Generate Test Recommendation"):
        st.success("This is a test recommendation. The full app would provide personalized supplement advice.")

if __name__ == "__main__":
    main()
