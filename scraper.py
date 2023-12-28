from selenium import webdriver  
from selenium.webdriver.common.by import By  
import json #the first few of lines import different selenium libraries

# Function to configure and return a WebDriver instance
def configure_driver():
    # Configure the driver (e.g., using Chrome)
    driver = webdriver.Chrome()
    return driver

# Function to scrape blockquote texts from a given character page
def scrape_character_page(driver, url):
    # Navigate to the character page
    driver.get(url)

    # Find all blockquote elements and print their text
    blockquotes = driver.find_elements(By.TAG_NAME, "blockquote")
    # Return a list of texts from each blockquote element
    return [blockquote.text for blockquote in blockquotes]

def main():
    # List of character page URLs to be scraped
    character_urls = [
        'https://www.khdatabase.com/Ansem',
        'https://www.khdatabase.com/Ariel',
        'https://www.khdatabase.com/Cloud',
        'https://www.khdatabase.com/Daisy_Duck',
        'https://www.khdatabase.com/Donald_Duck',
        'https://www.khdatabase.com/Goofy',
        'https://www.khdatabase.com/Hades',
        'https://www.khdatabase.com/Hercules',
        'https://www.khdatabase.com/Ice_Titan',
        'https://www.khdatabase.com/Jiminy_Cricket',
        'https://www.khdatabase.com/Kairi',
        'https://www.khdatabase.com/King_Mickey_Mouse',
        'https://www.khdatabase.com/Lava_Titan',
        'https://www.khdatabase.com/Leon',
        'https://www.khdatabase.com/Maleficent',
        'https://www.khdatabase.com/Merlin',
        'https://www.khdatabase.com/Moogle',
        'https://www.khdatabase.com/Philoctetes',
        'https://www.khdatabase.com/Queen_Minnie_Mouse',
        'https://www.khdatabase.com/Riku',
        'https://www.khdatabase.com/Rock_Titan',
        'https://www.khdatabase.com/Simba',
        'https://www.khdatabase.com/Sora',
        'https://www.khdatabase.com/Tornado_Titan',
        'https://www.khdatabase.com/Ursula',
    ]

    # Configure the WebDriver
    driver = configure_driver()
    
    # Initialize an empty list to store all scraped quotes
    all_quotes = [] 
    try:
        # Iterate over each URL in the character_urls list
        for url in character_urls:
            # Scrape blockquote texts from the current URL
            quotes = scrape_character_page(driver, url)
            # Add the scraped quotes to the all_quotes list
            all_quotes.extend(quotes)
    finally:
        # Close the WebDriver once scraping is done or if an error occurs
        driver.quit()

    # Write the collected quotes to a JSON file
    with open('quotes.json', 'w') as file:
        # Convert the list of quotes to JSON format and save i
        json.dump(all_quotes, file)


# Python's way to check if this script is being run as the main program
if __name__ == "__main__":
    main()



























































































# def configure_driver():
#     driver = webdriver.Chrome()
#     return driver


# def get_character_urls(driver, url):
#     driver.get(url)
#     character_links = driver.find_elements(By.CSS_SELECTOR, "div.mw-category-group ul li a")
#     urls = [link.get_attribute('href') for link in character_links]

#     return urls

# def main():
#     characters_list_page = "https://www.khdatabase.com/Category:Kingdom_Hearts_characters"

#     driver = configure_driver()

#     try:
#         character_urls = get_character_urls(driver, characters_list_page)
#         for url in character_urls:
#             print(url)
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()

# #elements = driver.find_elements(By.TAG_NAME, "blockquote")  

# #for element in elements:
# #    print(element.text)

# #driver.quit()
