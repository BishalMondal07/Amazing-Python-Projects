# Amazing-Python-Projects
Here, you will find a collection of twelve wonderful Python projects that you can explore and learn from. Each project is designed to showcase different aspects of Python programming and demonstrate its versatility and power.

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

# 3. QR Code Generator
The "QR Code Generator" is a Python script that generates a QR code from a user-provided link and saves it as an image file. It uses the qrcode library and the PIL (Python Imaging Library) module to create and save the QR code.

## Prerequisites
To run the script, you need to have Python installed on your system. Additionally, make sure that the qrcode and PIL modules are installed. You can install them using pip:

  ```bash
  pip install qrcode pillow
```
## Limitations
● The script relies on the user-provided link for generating the QR code. Make sure the link is valid and correctly entered to ensure accurate QR code generation.

● The generated QR code image is saved in the current directory where the script is run. Ensure that the script has write permissions in that directory.

# 4. URL Shortener
This is a Python program that uses the pyshorteners library to create a short URL from a long URL entered by the user. The program generates a unique, shortened URL using the TinyURL service that redirects to the original URL.

## Installation
Before running this program, you must first install the pyshorteners library using pip:
```bash
  pip install pyshorteners
```
## Usage
To use this program, simply run the Python script UrlShortener.py. The program will prompt you to enter a long URL that you want to shorten. Once you enter the long URL, the program will generate a short URL using the TinyURL service and display it on the screen.

# 5. Weather App
This code fetches the current temperature of a given city using the Weather API. It prompts the user to enter the name of the city and then sends a request to the API with the city name as a parameter. The API returns a JSON response which is then parsed to extract the current temperature of the city in degrees Celsius. Finally, the temperature is printed to the console.

## Libraries used
● requests

● json

## API key
The API key used in this code is a free key provided by Weather API. The key has a limited number of requests and might not work if  [Weather API Website](https://www.weatherapi.com/). If you have your own API key, you can replace the key parameter in the URL with your own key.

# 6. Pytube Youtube Downloader
This Python script allows you to download YouTube videos using the pytube library. It prompts the user to enter a YouTube video link, displays the available video streams, and lets the user choose the desired stream to download. The script then downloads the selected video and saves it to the current directory.

To use this code, ensure that the Pytube library is installed in your Python environment. You can install it using pip with the command:

```bash
  pip install pytube
```
## Notes:
- Some YouTube videos may have restrictions or be unavailable for download due to YouTube's policies or the uploader's settings. In such cases, the script may not be able to download the video.
- The pytube library may not work for certain videos if there are changes in YouTube's backend or if YouTube updates its algorithms. If you encounter any issues, make sure you have the latest version of the pytube library and check for updates.
- Ensure you have a stable internet connection during the video download process to avoid interruptions or incomplete downloads.

# 7. Armstrong Number Checker
This is a simple Python program to check whether a given number is an Armstrong number or not. An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
## Example
Suppose you want to check whether 153 is an Armstrong number or not. You can run the program and enter 153 as the input. The program will calculate the power of each digit: 1^3 + 5^3 + 3^3 = 153. Since 153 is equal to the sum of the power of each digit, the program will print that 153 is an Armstrong number.

# 8. Store-Reciept-Generator
This program helps to calculate the total bill of items purchased at a store. The user has to provide the name of the store and the number of items purchased. Then for each item, the user has to enter the price and the name of the item. Finally, the program calculates the total bill and displays a detailed bill receipt.

# 9. Password Generator
This code generates a strong password using a combination of numbers, uppercase and lowercase letters, and special characters.

## How it works
The code creates three lists, a, b, and c, each containing characters to be used in generating the password. Then, it randomly selects a character from each list and concatenates them to form a six-character password.

The password consists of two random numbers, two random uppercase or lowercase letters, and two random special characters.

# 10. Python LCM and HCF Calculator
This is a simple Python program that calculates the LCM (Least Common Multiple) and HCF (Highest Common Factor or GCD) of two numbers entered by the user.

## How it works
The program uses simple arithmetic operations to calculate the LCM and HCF of two numbers.

For LCM, it first finds the maximum number between the two input numbers. It then iteratively checks if the maximum number is divisible by both input numbers. If it is, the program breaks the loop and returns the LCM of the two numbers.

For HCF, it first finds the minimum number between the two input numbers. It then iteratively checks for factors of both numbers up to the minimum number. If a common factor is found, the program stores the factor and continues checking. The program then returns the HCF of the two numbers.

# 11. Password Securement using Substitution Cipher
This program is a password security tool that replaces some characters in the password with some other characters, making it more secure. It replaces some commonly used characters with more complex characters, making it harder for hackers to crack the password.

## How it Works
The program defines a SECURE tuple containing pairs of characters to be replaced. It then prompts the user to enter a password. The program then iterates over each character in the password and replaces the characters in SECURE if found. The modified password is then returned and printed to the console.

# 12. Dice Rolling Simulator
This is a simple Python program that simulates rolling a dice. It generates a random number between 1 and 6, and prints out a representation of a dice with the number of dots corresponding to the number that was rolled.

## Code Explanation
The random module is imported to generate a random number between 1 and 6, representing the number that was rolled on the dice.
The if statements check the value of the result variable, and print out the corresponding representation of a dice using ASCII art.
