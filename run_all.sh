#!/bin/bash

# Step 1: Data Preprocessing
python src/data_preprocessing.py

# Step 2: Feature Extraction (if needed, depending on your model script)
python src/feature_extraction.py

# Step 3: Model Training
python src/model.py

# Step 4: Visualization
python src/visualization.py
