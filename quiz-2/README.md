# OpenWeatherMap API Automation Test

This repository contains API automation tests for OpenWeatherMap.

## How to run the tests

1.  **Install dependencies:**
    ```bash
    pip install requests
    ```
2.  **Replace `YOUR_API_KEY`:** In the `test_openweathermap.py` file, replace `YOUR_API_KEY` with your actual OpenWeatherMap API key.
3.  **Run the tests:**
    ```bash
    python test_openweathermap.py
    ```

## Test Scenarios

- Get current weather data for Terban, Sleman, Yogyakarta
- Get current air pollution data for Terban, Sleman, Yogyakarta

## Assertions

- Response code (200 OK)
- Basic JSON schema validation
