import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to create 'images' folder if it doesn't exist
def create_folder(folder_name="images"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to download an image from a given URL
def download_image(image_url, folder_name="images", count=0):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            # Create file path
            image_path = os.path.join(folder_name, f"image_{count}.jpg")
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded image_{count}.jpg")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

# Function to search and download images from a fantasy manhwa website
def search_and_download_images(query="fantasy manhwa", num_images=30, folder_name="images"):
    url = "https://www.google.com/search?tbm=isch&q=" + query
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    # Send a request to the URL
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all("img")
        
        create_folder(folder_name)
        
        count = 0
        for img in images:
            if count >= num_images:
                break
            img_url = img.get("src")
            if img_url and img_url.startswith('http'):
                download_image(img_url, folder_name, count)
                count += 1
    else:
        print(f"Failed to retrieve content from {url}")

# Main function to execute the search and download
if __name__ == "__main__":
    search_and_download_images(query="fantasy manhwa", num_images=30)
