# cryptocurrency-price-tracker
This repository contains a Python script named take_data_coins.py, designed to track and store real-time prices of popular cryptocurrencies such as Ethereum (ETH), Bitcoin (BTC), and Ripple (XRP). It leverages the Bybit API for fetching prices and stores the data in local SQLite databases, thus allowing for easy data access and persistence.




Cryptocurrency Price Tracker

  This Python script is designed to track and store the latest trading prices of Ethereum (ETH), Bitcoin (BTC), and Ripple (XRP) using the Bybit API. The prices are        stored in SQLite databases for each cryptocurrency, allowing for easy data persistence and access.
  


Features: 

  Fetches the latest trading prices for ETH, BTC, and XRP.
  Stores prices in individual SQLite databases for each cryptocurrency.
  Utilizes Bybit's Unified Trading API for price data.
  Easy configuration with environment variables for API keys.

  
Prerequisites:

  Before you begin, ensure you have met the following requirements:
  
    Python 3.x installed
    SQLite3 installed
    Bybit account with API keys generated
    pybit and python-decouple libraries installed
    You can install the required Python libraries using pip:
  
  
      pip install pybit python-decouple

  
Setup:

  Clone the repository or download the script to your local machine.
  
  Create a .env file in the root directory of the project.
  
  Add your Bybit API key and secret to the .env file as follows:
  
  
    BYBIT_API_KEY=your_api_key_here
    BYBIT_API_PASS=your_api_secret_here
  
  Ensure you have SQLite3 installed on your system to create and manage the databases.

How It Works:
  
  The script performs the following actions:
  
  Database Initialization: On startup, it attempts to connect to SQLite databases for ETH, BTC, and XRP. If the databases do not exist, they are created with a single table to store the price values.
  
  Fetching Prices: Utilizing the Bybit API, the script retrieves the latest trading prices for ETH, BTC, and XRP at regular intervals (every 120 seconds).
  
  Storing Prices: The retrieved prices are then stored in their respective databases.
  
  Repeating: This process repeats every 120 seconds, continuously updating the databases with the latest prices.


Code Explanation:

  Database Connection and Table Creation: The script starts by connecting to SQLite databases for each cryptocurrency. It tries to create a table to store the prices if    it doesn't already exist. This operation is enclosed in a try-except block to handle the case where the table already exists.
  
  Data Insertion Functions: There are separate functions defined for inserting the latest price data into each cryptocurrency's database. These functions connect to the    respective database, insert the price, commit the transaction, and then close the connection.
  
  API Key Configuration: The script uses python-decouple to securely fetch API keys stored in the .env file.
  
  Bybit API Session Initialization: An instance of the HTTP class from pybit.unified_trading is created with the Bybit API keys for fetching the cryptocurrency prices.
  
  Main Loop: In an infinite loop, the script fetches the latest prices for ETH, BTC, and XRP using the Bybit API, converts the price data to floats, and calls the          respective data insertion functions. It then sleeps for 120 seconds before repeating.


Running the Script:

  To run the script, navigate to the script's directory in your terminal and run:
  
  
    take_data_coins.py.py



Important Notes:

  The script uses a hard-coded interval of 120 seconds for fetching price updates. Modify this value as needed based on your requirements.
  Ensure your Bybit API keys have the necessary permissions to access trading data.
