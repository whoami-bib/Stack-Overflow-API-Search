
# Stack Overflow Search API


This is a web application built with Django and the Stack Overflow API that allows users to search for questions and answers on Stack Overflow.

## Features

•Search all available fields/parameters of the Stack Overflow API

•Caching of search results to reduce API calls and improve 

performance

•Rate limiting to prevent excessive API usage

•API key protection using environment variables


## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/whoami-bib/Stack-Overflow-API-Search.git
```
    
Install the project dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file in the project root directory and add the following line, replacing YOUR_API_KEY with your actual API key:


```bash
API_KEY=YOUR_API_KEY
```
Run the server:

```bash
python manage.py runserver
```

Access the application at:
```bash
http://localhost:8000//api/search/?q=django&page=1
```
## Usage

•Enter your search query in the search box and click "Search".

•The application will display a list of results from the Stack Overflow API.

•Click on a result to view the details of the question.



