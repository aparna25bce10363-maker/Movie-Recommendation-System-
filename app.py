import streamlit as st
from model import recommend

st.title(" Movie Recommendation System")

movie = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie:
        results = recommend(movie)
        
        st.write("### Recommended Movies:")
        for r in results:
            st.write("👉", r)
    else:
        st.warning("Please enter a movie name")
