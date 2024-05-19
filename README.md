# Data Science Bootcamp Project

Welcome to the repository for the Data Science Bootcamp project. This project is structured into three phases, each focusing on different aspects of data science.

## Phase 1: Data Collection, Storage, and Analysis

### Overview

In this phase, you will work on a project involving smartphone data, divided into four main stages:

1. **Data Extraction**: Collect data from the internet using web scraping.
2. **Database Design**: Store the extracted data in a database.
3. **Statistical Analysis**: Analyze the data using statistical methods and visualizations.
4. **Power BI Dashboard**: Create a dashboard to visualize insights using Power BI.

### Stage 1: Data Extraction

You will gather data about smartphones from the website [GSMArena](https://www.gsmarena.com). The goal is to extract data for smartphones from 2010 to 2024 for brands such as Samsung, Apple, Xiaomi, Huawei, Alcatel, Sony, LG, Lenovo, ZTE, Nokia, BLU, Infinix, HTC, and Asus. The data points to collect include:

- **Network**: Types of communication networks (e.g., 5G, LTE).
- **Launch**: Information about the product release date and availability.
- **Body**: Dimensions, weight, etc.
- **Display**: Screen size, type, resolution, etc.
- **Platform**: Operating system, chipset, CPU, and GPU.
- **Memory**: Internal and external memory details.
- **Main Camera**: Specifications of the main camera.
- **Selfie Camera**: Specifications of the front camera.
- **Sound**: Audio features.
- **Comms**: Communication features like Wi-Fi and Bluetooth.
- **Features**: Additional features like sensors.
- **Battery**: Battery type and charging details.
- **Misc**: Miscellaneous information like color, model, and price.

### Stage 2: Database Design

Design and create a database to store the extracted data, including:

- Identifying main entities (e.g., brands, models).
- Determining relationships between entities.
- Specifying attributes for each entity.
- Normalizing the database to eliminate data redundancy and ensure data integrity.

### Stage 3: Statistical Analysis

**Focus: Data Analysis**

Use statistical techniques to analyze the data and answer questions such as:

- Distribution of mobile devices among different network technologies (2G, 3G, 4G).
- Correlation matrix for dimensions, weight, pixel density, screen-to-body ratio, battery capacity, and ppi.
- Most common SIM card type used in mobile devices (visualized with a chart).
- Top 10 Android versions based on usage frequency.
- Comparison of the top 50 most expensive phones by operating system (Android, iOS).
- Distribution of phones by brand.
- Scatter plot of ppi density by year for Samsung, Apple, and Xiaomi.
- Distribution of quantitative data columns.
- Estimation of mean prices for 2023 for Apple, Samsung, Huawei, Xiaomi, and Nokia, with a 98% confidence interval.

Perform hypothesis testing, such as:

- Comparing prices of phones with different SIM card types.
- Analyzing the relationship between screen size and resolution.
- Comparing the weights of phones based on their operating system (Android vs. iOS).
- ANOVA tests for battery capacity and prices across different screen sizes and brands.

### Stage 4: Power BI Dashboard

Create visualizations and dashboards using Power BI, including:

- Price distribution of phones for the top 5 brands.
- Average battery capacity by brand over the years.
- Most commonly used sensors in smartphones.
- Pie chart of SIM card types.
- Relationship and trend between phone weight and size.
- Trend of screen size to phone area ratio over the years by brand.
- Configurable dashboard showing brand market share based on CPU cores, screen size, memory, and RAM.
- Word cloud of network technologies for Xiaomi and Huawei.
- Trend of the number of phones produced by each brand from 2010 to the present.

## Phase 2: Machine Learning

### Overview

In this phase, you will focus on clustering, classification, and regression problems using the smartphone data collected in Phase 1.

### Problem 1: Clustering

#### Task 1: K-means Clustering

- Perform K-means clustering on the dataset using battery capacity and price with 5 clusters.
- Visualize the clusters on a scatter plot, showing cluster centers and appropriately labeled axes.

#### Task 2: Optimal K Selection

- Run K-means for K values from 1 to 10 and determine the optimal K using the Within-Cluster Sum of Squares (WCSS) method.
- Provide a detailed explanation of the chosen K value.

#### Task 3: DBScan Clustering

- Use DBScan for clustering based on battery capacity and price to produce 3 meaningful clusters.
- Visualize the clusters and explain the effect of different hyperparameters.

### Problem 2: Operating System Classification

**Focus: Machine Learning**

- Train a model to predict the operating system of a phone based on its features.
- Use the battery capacity as a numerical feature in the first model.
- Convert battery capacity to a categorical feature in the second model and compare the results.
- Evaluate the model using accuracy, precision, recall, F1 score, and AUC, and provide a confusion matrix.

### Problem 3: Price Prediction

- Train a model to predict the price of a phone based on its features.
- Determine the most influential features affecting the price.
- Use any machine learning algorithm learned in the bootcamp.
- Evaluate the model using R^2 and loss charts, and provide a detailed analysis of the results.

## Phase 3: Deep Learning - Image Classification and NLP

### Overview

In this phase, you will work on two main problems involving image and text data: food classification and news classification.

### Problem 1: Food Classification

**Focus: Deep Learning Image Classification**

#### Task 1: Data Preparation

- Load and preprocess images using libraries like Keras or PyTorch.
- Split the data into training and validation sets.

#### Task 2: Model Selection

- Use any deep learning model or architecture such as AlexNet, ResNet, VGG, Inception, MobileNet, or custom models.
- Utilize pre-trained weights and fine-tune the models for better performance.
- Experiment with different hyperparameters like learning rate, batch size, and epochs.

#### Task 3: Model Evaluation

- Save and load the trained model for testing.
- Use techniques like data augmentation to prevent overfitting.
- Visualize some images with their true and predicted labels to assess model performance.
- Evaluate the model using F1 score (micro averaging) and provide a CSV file with predictions.

### Problem 2: News Classification

**Focus: Natural Language Processing (NLP)**

#### Task 1: Data Collection

- Collect data from sources such as news websites, social media, blogs, and online magazines.
- Ensure the data covers categories like Business, Sport, Tech, and Politics.

#### Task 2: Model Development

- Develop a model to classify news articles based on their headlines and descriptions.
- Use models like transformers, fine-tuned for the specific domain.

#### Task 3: Model Evaluation

- Create a main.py file to load the trained model and predict categories for a given CSV file.
- Ensure the file prints accuracy based on predictions and true labels.

