# Admit Bot - College Admissions Assistant

Admit Bot is an AI-powered assistant designed to guide students and parents through college admissions, fee structures, placement statistics, and personalized career counseling.

## Features

- **College Search**: Find colleges based on your preferences
- **Fee Calculator**: Estimate college expenses
- **Placement Statistics**: View placement trends and opportunities
- **Career Counseling**: Get personalized career guidance

## Setup Instructions

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## Usage

1. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)
2. Use the sidebar navigation to explore different sections
3. Input your preferences and requirements in each section
4. Get personalized recommendations and insights

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Plotly

## Note

This is a prototype version of Admit Bot. The data used in the application is sample data and should be replaced with real data from a database in a production environment.
