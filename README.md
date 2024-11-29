# Keyword Ranking Dashboard

This project is an interactive, data-driven dashboard built using Python, Dash, and Google Sheets API. It enables users to analyze keyword ranking trends dynamically, providing real-time visualizations and insights into data. Designed for ease of use and scalability, the dashboard integrates Google Cloud services for secure and seamless data management.

---

## Features

- **Secure Authentication**: Uses a Google Cloud service account for JSON-based authentication, eliminating manual logins.
- **Data Fetching**: Retrieves data from Google Sheets via the Google Sheets API.
- **Data Filtering**: Prepares and filters data for relevance and performance.
- **Interactive Dashboard**: Features dropdowns, search functionality, and real-time graph updates.
- **Dynamic Visualizations**: Supports bar, line, and scatter plot types.
- **Data Export**: Allows users to export filtered data to a CSV file.
- **Responsive Design**: Styled with Bootstrap for optimal user experience across devices.

---

## Technologies Used

- **Languages**: Python
- **Libraries**: 
  - `gspread` and `oauth2client` for Google Sheets API access
  - `Pandas` for data manipulation
  - `Dash` for dashboard creation
  - `Bootstrap` for responsive design
- **Google Cloud Platform**: Service accounts for secure API access

---

## Installation

1. **Clone the Repository**:
   ```bash
   https://github.com/Samrat1507/Keyword-Dashboard.git
   cd keyword-ranking-dashboard
   ```

2. **Set Up Google Cloud Service Account**:
   - Create a service account on [Google Cloud Console](https://console.cloud.google.com/).
   - Assign necessary permissions for Google Sheets and Drive APIs.
   - Download the service account JSON key file.

3. **Install Dependencies**:
   Use the following command to install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**:
   - Place the JSON key file in the project directory.
   - Set the path to the JSON file in an environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

   The app will run locally and can be accessed at [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

---

## Usage

1. **Data Input**:
   - Provide the URL of the Google Sheet containing your keyword data.
   - Ensure the columns include `KEYWORD`, `Belongs to`, and date-based ranking data.

2. **Dashboard Interaction**:
   - Use the dropdowns to filter data by category or graph type.
   - Search for specific keywords using the search bar.
   - View keyword ranking trends over time through interactive graphs.
   - Export the filtered data to CSV for offline analysis.

---

## Project Structure

```
keyword-ranking-dashboard/
│
├── app.py                  # Main application script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── service-account.json    # Service account credentials (not included, user-specific)
```

---

## Future Enhancements

- Integrate additional data sources like Google BigQuery.
- Add support for multi-language visualizations.
- Deploy the application on cloud platforms for broader access.
- Introduce user authentication for personalized dashboards.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---


Feel free to contribute to this project by opening issues or submitting pull requests! 😊
