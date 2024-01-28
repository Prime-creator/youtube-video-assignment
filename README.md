# FamPay Backend Assignment

This Django project is designed to fetch and store the latest YouTube videos based on a predefined search query. Additionally, it provides APIs for retrieving stored video data and searching for videos by title and description.

## Project Setup

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Google API Python Client

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Prime-creator/fampay-backend-assignment.git
    cd fampay-backend-assignment
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

   - Create a `.env` file in the project root.
   - Add your YouTube Data API key to the `.env` file:

        ```env
        YOUTUBE_API_KEY=your_youtube_api_key
        ```

4. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The API should be accessible at `http://localhost:8000/`.

## Usage

- Use the `/api/videos/` endpoint to retrieve stored video data.
- Use the `/api/search/` endpoint to search for videos.

For more details, refer to the API documentation.

## Bonus Features

- [Optional] Add support for multiple API keys.
- [Optional] Create a dashboard to view stored videos with filters and sorting options.

## Reference

- [YouTube Data API Documentation](https://developers.google.com/youtube/v3/getting-started)
- [YouTube Search API Reference](https://developers.google.com/youtube/v3/docs/search/list)

Feel free to reach out if you have any questions or need further assistance!