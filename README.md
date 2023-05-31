# Amazing-Python-Projects
Here, you will find a collection of five wonderful Python projects that you can explore and learn from. Each project is designed to showcase different aspects of Python programming and demonstrate its versatility and power.

# 1. PyPDF2 PDF Merger
This code is an example of using the PyPDF2 library to merge multiple PDF files into a single document. The code takes a list of PDF files to be merged and uses the PdfMerger class of the PyPDF2 library to append each PDF file to the merger object. Finally, the merged document is saved to the file 'merged.pdf' using the write() method. There are two sample pdf files attached with this folder.

To use this code, ensure that the PyPDF2 library is installed in your Python environment. You can install it using pip with the command

```bash
  pip install PyPDF2
```
Replace the file names in the pdfiles list with the names of the PDF files that you want to merge, and then run the code.

This code can be useful for merging multiple PDF files into a single document, which can be useful for creating reports, presentations, or other types of documents that require combining multiple PDF files.

# 2. Plagiarism Detection in Python
This code utilizes the difflib library in Python to detect the similarity between two text files and determine the percentage of plagiarism. It compares the content of two files, 1.txt and 2.txt, and calculates the similarity ratio using the SequenceMatcher class from the difflib module.

# 3. URL Shortener
This is a Python program that uses the pyshorteners library to create a short URL from a long URL entered by the user. The program generates a unique, shortened URL using the TinyURL service that redirects to the original URL.

## Installation
Before running this program, you must first install the pyshorteners library using pip:
```bash
  pip install pyshorteners
```
## Usage
To use this program, simply run the Python script UrlShortener.py. The program will prompt you to enter a long URL that you want to shorten. Once you enter the long URL, the program will generate a short URL using the TinyURL service and display it on the screen.

# 4. Weather App
This code fetches the current temperature of a given city using the Weather API. It prompts the user to enter the name of the city and then sends a request to the API with the city name as a parameter. The API returns a JSON response which is then parsed to extract the current temperature of the city in degrees Celsius. Finally, the temperature is printed to the console.

## Libraries used
● requests

● json

## API key
The API key used in this code is a free key provided by Weather API. The key has a limited number of requests and might not work if  [Weather API Website](https://www.weatherapi.com/). If you have your own API key, you can replace the key parameter in the URL with your own key.

# 5. Pytube Youtube Downloader
This Python script allows you to download YouTube videos using the pytube library. It prompts the user to enter a YouTube video link, displays the available video streams, and lets the user choose the desired stream to download. The script then downloads the selected video and saves it to the current directory.

To use this code, ensure that the Pytube library is installed in your Python environment. You can install it using pip with the command:

```bash
  pip install pytube
```
## Notes:
- Some YouTube videos may have restrictions or be unavailable for download due to YouTube's policies or the uploader's settings. In such cases, the script may not be able to download the video.
- The pytube library may not work for certain videos if there are changes in YouTube's backend or if YouTube updates its algorithms. If you encounter any issues, make sure you have the latest version of the pytube library and check for updates.
- Ensure you have a stable internet connection during the video download process to avoid interruptions or incomplete downloads.


