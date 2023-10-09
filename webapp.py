import streamlit as st
from selenium import webdriver
import openai

driver = webdriver.Chrome()  

openai.api_key = "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"  

def main():
    st.title("Cadabra ✨")

    # Sidebar for navigation
    page = st.sidebar.selectbox("Select a page", ["Data Repository", "Search and Chat"])

    if page == "Data Repository":
        display_data_repository()
    elif page == "Search and Chat":
        display_search_and_chat()

def display_data_repository():
    st.header("Data Repository")
    st.write("Here you can access various biomedical research datasets from NASA Open Data Repository")

    st.subheader("Available Datasets")
    datasets = [
        {"name": "Dataset 1", "source": "Source 1"},
        {"name": "Dataset 2", "source": "Source 2"},
        {"name": "Dataset 3", "source": "Source 3"},
        {"name": "Dataset 4", "source": "Source 4"},
        ]

    for dataset in datasets:
        st.write(f"**Name:** {dataset['name']}")
        st.write(f"**Source:** {dataset['source']}")
        st.write("---") 
    
def display_search_and_chat():
    st.header("Search and Chat")
    st.write("Find an required dataset")


    user_prompt = st.text_input("Enter your research field:")

    if st.button("Search and Chat"):
        scraped_data = perform_web_scraping(user_prompt)
        
        chat_response = chat_with_gpt(scraped_data)

        st.subheader("Chat Response:")
        st.write(chat_response)

def perform_web_scraping(prompt):

    driver = webdriver.Chrome() 
    url = 'https://data.nasa.gov/browse?limitTo=datasets'
    driver.get(url)
    scraped_data = driver.find_elements_by_xpath("//*[contains(text(), '" + prompt + "')]")
    driver.quit()

    return scraped_data

def chat_with_gpt(scraped_data):
    chat_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user", "content":f"Answer to the user in the clear way in what purposes this dataser can be used:{scraped_data}"}]
    )
    chat_response = chat_response + '\nLink:https://data.nasa.gov/browse?limitTo=datasets'
    return chat_response

if __name__ == "__main__":
    main()

    
    
