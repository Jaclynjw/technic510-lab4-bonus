# Weather App with Periodic Data Scraping

This repository hosts a Python-based web scraper integrated into a weather lookup application. The app uses Streamlit to provide a user interface where users can enter a location to fetch and display weather forecasts. Additionally, the project is configured to periodically scrape and update data using GitHub Actions.

## Project Overview

The main components of this project are:
- **Weather App**: A Streamlit application that allows users to input a location name and get the current weather forecast.
- **Automated Scraping**: A scheduled scraper that runs periodically via GitHub Actions to update the app with the latest data.

## Features

- **Streamlit Weather Application**: Easy-to-use web interface for fetching weather.
- **Automated Scraping**: Periodic data collection using GitHub Actions.
- **Robust Error Handling**: Includes error handling for API failures and unexpected data issues.

## How It Works

The Streamlit app provides a frontend where users can enter location names. The backend, powered by Python, uses geocoding to convert locations to coordinates and fetches weather data from these coordinates. The periodic scraping is handled by GitHub Actions, which also automates data updates.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- GitHub account

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
2. **Install the required Python libraries**:
    ```bash
    pip install -r requirements.txt
### Configuration
- Setup Streamlit app: The main application file is app.py, which you can customize for additional functionality.
- Schedule scraper runs: Adjust the cron schedule in .github/workflows/scraper.yml to modify the frequency of data updates.

### Running Locally
To run the Streamlit app locally, execute:
```bash
streamlit run app.py
