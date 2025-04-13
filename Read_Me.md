# Natural Language to SQL Query Provider

A Streamlit-based application that converts natural language queries to SQL and executes them against a Redshift database.

## Features

- Natural language to SQL query conversion using OpenAI GPT
- Redshift database integration
- Pre-defined table relationships management
- Interactive Streamlit UI
- Real-time query execution and results display

## Prerequisites

- Python 3.8+
- Redshift database access
- OpenAI API key
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt

#Project Structure
├── README.md
├── requirements.txt
├── config.py          # Configuration and table relationships
├── database.py        # Database connection handler
├── schema_manager.py  # Table relationship management
├── nl_to_sql.py      # Natural language to SQL converter
└── app.py            # Streamlit application

## Example Queries
- "Show me all orders from customers in New York"
- "List the top 10 products by sales volume"
- "Find customers who made purchases last month"
## Contributing
Feel free to submit issues and enhancement requests.

## License
MIT License

## Acknowledgments
- OpenAI for GPT API
- Streamlit for the UI framework