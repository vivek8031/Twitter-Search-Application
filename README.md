# 🐦 Twitter Search Application 🚀

[![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vivek7208/Twitter-Search-Application/blob/main/src/datastore/data_insertion_v2.ipynb)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![Preview in nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/vivek7208/Twitter-Search-Application/blob/main/src/datastore/data_insertion_v2.ipynb)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vivek7208/Twitter-Search-Application/blob/main/src/datastore/data_insertion_v2.ipynb)

## 🎯 Project Overview

This project is a comprehensive Twitter data search application that allows users to search through tweets, retweets, quoted tweets, replies, and user data. The application fetches Twitter data, stores it into MySQL and MongoDB databases, and provides a user-friendly interface to perform and display search results. 

The project requires storing the tweets' information in at least two datastores: one relational (MySQL) and another non-relational (MongoDB). An LRU (Least Recently Used) cache is designed and implemented for frequently accessed data to enhance data retrieval speed. The cache is periodically saved to disk, and stale entries are removed to maintain the efficiency of the system.

The search application provides several search options such as search by string, hashtag, and user, and several drill-down search features.

## 🎥 Application in Action

[![Twitter Search Application in Action](http://img.youtube.com/vi/7CfPOnk_0zQ/0.jpg)](http://www.youtube.com/watch?v=7CfPOnk_0zQ "Twitter Search Application in Action")

## 🗂 Repository Structure

This repository has the following structure:

```
├── data/
│   └── ...
├── docs/
│   ├── InterimReport.md
│   ├── FinalReport.md
│   └── ...
├── presentation/
│   └── ...
└── src/
    ├── cache/
    ├── datastore/
    ├── search/
    ├── tests/
    └── ...
```

- The `data` folder contains any data files used in the project.
- The `docs` folder contains the interim report, final report, and any other project documentation.
- The `presentation` folder contains the slides for the project presentation.
- The `src` folder contains the source code for the project.

## ⭐ Features

- **Data Collection and Storage:** Fetches Twitter data using the Twitter API and stores the data into MySQL and MongoDB databases.
- **User-Friendly Search Interface:** Provides a Streamlit web application to search through the stored data with the flexibility of using various parameters such as usernames, hashtags, and date ranges.
- **LRU Cache:** Implements an LRU cache to enhance data retrieval speed. The cache is periodically saved to disk and stale entries are removed to maintain the efficiency of the system.

## 📁 File Structure

- `data_insertion_v2.ipynb`: A Jupyter notebook responsible for fetching Twitter data using the Twitter API and inserting the data into MySQL and MongoDB databases.
- `search_app.py`: The main Streamlit application file that provides the interface for searching through the stored data and displaying the results.
- `lru_cache.py`: A Python script implementing the LRU cache used for efficient data retrieval in the Streamlit application.

## 💻 Installation and Setup

### Prerequisites

- Python 3.6 or above
- MySQL
- MongoDB

### Steps

1. **Clone the repository:** Clone this repository to your local machine using `git clone`.

    ```bash
    git clone https://github.com/vivek7208/Twitter-Search-Application.git
    ```

2. **Install Python dependencies:** Navigate to the project directory and install the required Python packages. It's recommended to do this in a virtual environment.

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the data insertion notebook:** Run `data_insertion_v2.ipynb` to fetch and store the Twitter data.

    ```bash
    jupyter notebook data_insertion_v2.ipynb
    ```

4. **Run the Streamlit application:** Finally, launch the Streamlit application.

    ```bash
    streamlit run search_app.py
    ```

    Open the provided local URL in your browser to interact with the application.

## 🤝 Contributing

Contributions are always welcome!

## 📄 License

This project is licensed under the terms of the MIT license.
