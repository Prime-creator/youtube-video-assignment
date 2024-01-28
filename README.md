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
    git clone https://github.com/Prime-creator/youtube-video-assignment.git
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
