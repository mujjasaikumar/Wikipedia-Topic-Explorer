

# Wikipedia Topic Explorer

The **Wikipedia Topic Explorer** is a web application built with Flask that allows users to explore Wikipedia topics, view their sections, and generate summaries or paraphrases of specific sections using OpenAI's GPT-3 model.

## Features

### 1. Explore Wikipedia Topics
- Users can enter a Wikipedia topic URL in the homepage.
- The application retrieves the sections of the Wikipedia page and displays them to the user.

### 2. View Section Content
- Users can click on the section links to view the content of specific sections of the Wikipedia page.

### 3. Summarize Sections
- Users have the option to generate summaries of specific sections using GPT-3.
- Summarized text is displayed to the user, providing a concise overview of the section content.

### 4. Paraphrase Sections
- Users can generate paraphrases of specific sections of the Wikipedia page using GPT-3.
- Paraphrased text is displayed, offering a rephrased version of the section content.

## Installation

Follow these steps to install and run the application locally:

1. Clone the repository:

   ```bash
   gh repo clone mujjasaikumar/Wikipedia-Topic-Explorer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   
   add api key in .env file

   ```
   api_key = '<actual API key 🗝 >'
   ```

## Usage

1. Run the Flask application:

   ```bash
   python main.py
   ```

2. Open the application in a web browser:

   ```
   http://localhost:5000
   ```

3. Enter a Wikipedia topic URL and explore its sections.

## Endpoints

- **GET /**: Homepage route to enter a Wikipedia topic URL.
- **POST /<topic_name>**: Process the submitted Wikipedia topic URL and display its sections.
- **GET /redirect**: Redirect to a specific section of the Wikipedia page.
- **GET /section/<section_index>**: Display the content of a specific section of the Wikipedia page.
- **GET /summarize_section/<section_index>**: Summarize a specific section of the Wikipedia page using GPT-3 Turbo.
- **GET /paraphrase_section/<section_index>**: Paraphrase a specific section of the Wikipedia page using GPT-3 Turbo.

## Deployment

This code is hosted on [Render](https://wiki-summarisation-paraphrasing.onrender.com).

## Technologies Used

- Python
- Flask
- Wikipedia API
- OpenAI's GPT-3

## Contributors

- Saikumar Mujja
