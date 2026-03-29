**Movie Recommendation System using Machine Learning**



OVERVIEW

In today’s digital era, users are overwhelmed with a large number of choices on streaming platforms. Selecting a movie that matches personal interest becomes difficult and time-consuming.

This project presents a simple Movie Recommendation System that suggests movies based on similarity. It uses fundamental machine learning concepts to analyze movie features and recommend similar content.

The main aim of this project is to apply basic AI/ML concepts learned in the course to a real-world problem in an understandable and practical way.


PROBLEM STATEMENT

Choosing what to watch is often confusing due to the availability of numerous options. Many users spend more time searching for a movie than actually watching it.

This project aims to solve this problem by building a recommendation system that suggests movies based on similarity in genre.


OBJECTIVES

- To build a simple recommendation system using machine learning
- To understand how similarity-based models work
- To apply concepts like TF-IDF and cosine similarity
- To create an interactive user interface for better usability


COURSE CONCEPTS USED

This project is based on the following concepts taught in Fundamentals of AI & ML:

**Machine Learning Basics**   
  Understanding how machines can learn patterns from data


- **Supervised / Unsupervised Thinking**  
  Although this is not strictly supervised learning, it involves pattern recognition and similarity measurement

- **Feature Extraction**  
  Converting raw data (text) into meaningful numerical features

- **TF-IDF (Term Frequency – Inverse Document Frequency)**  
  Used to convert textual genre data into numerical vectors

- **Similarity Measures (Cosine Similarity)**  
  Used to calculate similarity between movies

- **Data Preprocessing**  
  Cleaning and preparing dataset for analysis

- **Real-world Application of AI**  
  Applying ML concepts to solve everyday problems


HOW IT WORKS

1 The dataset contains movie titles and their genres
2 The genre column is selected as the main feature
3 TF-IDF vectorization converts text into numerical form
4 Cosine similarity is used to calculate similarity between movies
5 When a user enters a movie name:
   - The system finds that movie
   - Compares it with all others
   - Recommends the top 5 most similar movies


DATASET DESCRIPTION

The dataset is manually created and contains:

- Movie Title
- Genre

Example:Avengers → Action Sci-Fi
        Titanic → Romance Drama


This simplified dataset helps in understanding the core logic of recommendation systems.


TECHNOLOGIES USED

- Python
- Pandas (for data handling)
- Scikit-learn (for ML concepts)
- Streamlit (for UI)


HOW TO RUN THE PROJECT

1. Install required libraries:
pip install pandas scikit-learn streamlit


2. Run the application:
python -m streamlit run app.py


3. Open the browser and enter a movie name to get recommendations


FEATURES

- Simple and user-friendly interface
- Fast and efficient recommendations
- Based on real machine learning concepts
- Easy to understand and implement


LIMITATION

- Works on a small dataset
- Recommendations are based only on genre
- Does not consider user preferences or ratings


FUTURE SCOPE

- Add larger datasets
- Include ratings and reviews
- Implement collaborative filtering
- Use deep learning models for better accuracy


CONCLUSION

This project demonstrates how fundamental AI/ML concepts can be applied to solve real-world problems. It helped in understanding how recommendation systems work and how data can be used to generate meaningful insights.

Overall, this project was a great learning experience in applying theoretical concepts practically.