Data Collection: Collects top posts from specified subreddits using the Reddit API. 
Argument Classification: Classifies posts into categories based on agreement or disagreement. 
Feature Extraction: Extracts key vocabulary features from the posts. 
Visualization: Visualizes the distribution of arguments across the categories.

I used Conda to create a virtual environment pip install -r requirements.txt

Set Up Environment Variables: Create a .env file in the project root and add your Reddit API credentials:
  CLIENT_ID=your_client_id CLIENT_SECRET=your_client_secret USER_AGENT=your_user_agent

Data Collection: python src/data_collection.py

Data Preprocessing: python src/data_preprocessing.py

Feature Extraction: python src/feature_extraction.py

Model Training: python src/model.py

Visualization: python src/visualization.py
