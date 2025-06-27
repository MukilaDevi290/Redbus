Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

Project Overview

This project focuses on building a complete pipeline for extracting, storing, and analyzing bus travel data from the Redbus website. 
It leverages Selenium for web scraping, SQL for data storage, and Streamlit to develop an interactive dashboard for dynamic filtering and analysis.


Objectives

- Automate the extraction of real-time bus travel data from Redbus.
- Store structured data in a SQL database.
- Build a user-friendly Streamlit web application to visualize and filter the data.
- Enable insights that improve decision-making in the transportation domain.

Skills & Technologies Used

- Python
- Selenium (for Web Scraping)
- Streamlit (for Web Application UI)
- SQL (for Data Storage and Filtering)
- Pandas, Regex, Time, etc. (for data manipulation and cleaning)

Domain

Transportation— Focused on improving accessibility and decision-making using real-time bus travel data.

Problem Statement

The "Redbus Data Scraping and Filtering with Streamlit Application" aims to provide a scalable solution for:
- Collecting detailed data about bus services (routes, prices, seat availability, etc.)
- Empowering travel companies and users to filter and interact with this data efficiently
- Enhancing transportation analytics and operations through real-time insights

Business Use Cases

- Travel Aggregators: Display real-time schedules, prices, and seat availability.
- Market Research: Identify travel patterns, demand trends, and pricing strategies.
- Customer Experience: Recommend buses based on comfort, rating, and availability.
- Competitor Analysis: Compare services, pricing, and performance of different operators.


Project Workflow

1. Data Scraping with Selenium
- Extract data such as bus routes, names, departure/arrival times, ratings, prices, and seat availability.
- Target at least 10 state-owned and private bus routes.

2. Data Storage (SQL)
- Store the extracted data into a structured SQL database.
- Use appropriate schema design for efficient querying and normalization.

3. Streamlit Application
- Build an interactive UI for users to:
  - Filter by route, bus type, rating, price range, and availability
  - Search and explore route-specific bus data
- Run dynamic SQL queries based on user input

 Screenshots
<img width="1512" alt="Screenshot 2025-06-27 at 10 10 14 PM" src="https://github.com/user-attachments/assets/25e7302a-b6f2-4ad5-b190-37520d0a2889" />

How to Run the Project

1.cloning the repository
git clone https://github.com/yourusername/redbus-project.git
cd redbus-project

2.Run the script
python testing.ipynb

3.Run the streamlit app
streamlit run stream.py












