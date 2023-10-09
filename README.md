
# Biomedical Research Data App

![App Screenshot](screenshot.png)  <!-- Replace with a screenshot of your app if available -->

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Web Scraping with Selenium](#web-scraping-with-selenium)
- [ChatGPT Integration](#chatgpt-integration)
- [Contributing](#contributing)
- [License](#license)

## Description
The Biomedical Research Data App is a multipage web application developed using Streamlit. It provides access to various biomedical research datasets from the NASA Open Data Repository. The app allows users to explore available datasets, perform web scraping using Selenium based on user prompts, and interact with ChatGPT for additional information and explanations.

## Features
- Access and download various biomedical research datasets.
- Perform web scraping with Selenium based on user-specified prompts.
- Interact with ChatGPT for further information and explanations.
- Multipage interface for easy navigation.

## Installation
To run the Biomedical Research Data App on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/biomedical-app.git
   cd biomedical-app
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Install ChromeDriver for Selenium:

Download ChromeDriver: https://sites.google.com/chromium.org/driver/
Move the ChromeDriver executable to a directory in your system's PATH (e.g., /usr/local/bin/).
Usage
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Access the app in your web browser at http://localhost:8501.

Web Scraping with Selenium
Enter a user prompt in the search bar on the "Search and Chat" page.
Click the "Search and Chat" button to initiate web scraping with Selenium.
The app will find HTML tags containing the prompt text and display them.
ChatGPT Integration
The app uses the OpenAI GPT API to interact with ChatGPT.
The "Search and Chat" page allows users to enter prompts and receive responses from ChatGPT.
Contributing
Contributions to the project are welcome. Please follow the contribution guidelines for details on how to contribute.



