# Custom Search Engine with Hybrid Relevance Model - Detailed Overview

## Project Concept

This project aims to create a personalized search engine that learns from user interactions to provide increasingly relevant results. It combines traditional search algorithms with advanced machine learning techniques to understand and predict result relevance.

## Key Components

1. **Search Engine Core**
   - Utilizes external APIs for initial result fetching
   - Implements basic result ranking and filtering

2. **Data Collection System**
   - Logs search queries and returned results
   - Captures user feedback on result relevance

3. **Hybrid Relevance Model (In Progress)**
   - Combines TF-IDF, Word2Vec, and BERT for text analysis
   - Uses Random Forest and Neural Network for relevance prediction

4. **Web Interface**
   - Provides a simple search interface
   - Allows users to rate the relevance of search results

## Current Development Status

- Basic search functionality is operational
- Data collection system is active and storing user interactions
- Machine learning model structure is defined but not yet trained or integrated

## Planned Features

- Integration of the trained Hybrid Relevance Model for result ranking
- Personalized search results based on user history
- Advanced analytics dashboard for search patterns and model performance

## Technical Stack

- Backend: Python, Flask
- Database: SQLite
- Machine Learning: Scikit-learn, TensorFlow, Gensim
- Frontend: HTML, JavaScript

## Challenges and Future Work

- Collecting sufficient diverse data for model training
- Balancing personalization with general relevance
- Optimizing model performance for real-time result ranking

## Experimentation Opportunities

While the project is still in development, users can:
- Perform searches and observe current ranking methods
- Provide relevance feedback to contribute to the training dataset
- Explore logged data to understand search patterns

Note: As this is a work in progress, expect frequent updates and potential instability in certain features.
