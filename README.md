# eksi-api

`eksi-api` is a FastAPI-based RESTful API that allows users to interact with Ekşi Sözlük, a popular Turkish collaborative dictionary and discussion platform. This API enables users to search for topics, retrieve entries, and explore trending content from Ekşi Sözlük.

## Features

- **Search Topics**: Search for topics on Ekşi Sözlük by query.
- **Search Topics with Entries**: Search for topics and retrieve their associated entries.
- **Trending Topics**: Get the list of trending topics.
- **Trending Topics with Details**: Get trending topics along with detailed information.
- **Trending Entries**: Retrieve the entries from trending topics.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/beratcmn/eksi-api.git
   cd eksi-api
   ```

2. Install the dependencies:

   Use `uv` please.

   ```bash
   uv init && uv sync
   ```

3. Run the FastAPI application:

   ```bash
   python mainsrc/eksi-api/app.py
   ```

4. Access the API documentation at `http://localhost:8000/docs`.

## Usage

### Search Topics

Search for topics based on a query:

```http
GET /topic/search/{query}?page={page}
```

- **query**: The search query (e.g., "Python").
- **page**: The page number (default is 1).

### Search Topics with Entries

Search for topics and retrieve their entries:

```http
GET /entries/search/{query}?page={page}
```

- **query**: The search query (e.g., "Python").
- **page**: The page number (default is 1).

### Get Trending Topics

Retrieve a list of trending topics:

```http
GET /topic/trending
```

### Get Trending Topic Details

Retrieve trending topics with detailed information:

```http
GET /topic/trending/details
```

### Get Trending Entries

Retrieve the entries from trending topics:

```http
GET /entry/trending
```

---

#### Project Structure

- `main.py`: The main entry point for the FastAPI application.
- `parser.py`: Contains the `EksiParser` class responsible for scraping and parsing Ekşi Sözlük data.
- Project uses `uv` for managing dependencies and running the application.

#### API Routes

1. **Root Route**

   - **URL**: `/`
   - **Method**: `GET`
   - **Description**: Provides basic information about the API.

2. **Search Topics**

   - **URL**: `/topic/search/{query}`
   - **Method**: `GET`
   - **Parameters**:
     - `query` (str): The search term.
     - `page` (int): The page number for pagination (default is 1).
   - **Description**: Returns a list of topics matching the search query.

3. **Search Topics with Entries**

   - **URL**: `/entries/search/{query}`
   - **Method**: `GET`
   - **Parameters**:
     - `query` (str): The search term.
     - `page` (int): The page number for pagination (default is 1).
   - **Description**: Returns a topic matching the search query along with its entries.

4. **Get Trending Topics**

   - **URL**: `/topic/trending`
   - **Method**: `GET`
   - **Description**: Returns a list of trending topics.

5. **Get Trending Topic Details**

   - **URL**: `/topic/trending/details`
   - **Method**: `GET`
   - **Description**: Returns trending topics with detailed information.

6. **Get Trending Entries**
   - **URL**: `/entry/trending`
   - **Method**: `GET`
   - **Description**: Returns entries from trending topics.

#### Parser Class (`EksiParser`)

- **Methods**:
  - `search_topic(query, page)`: Searches for topics based on the query.
  - `get_entries_from_url(url)`: Retrieves entries from a given topic URL.
  - `get_trending_topics()`: Fetches trending topics.
  - `get_topic(url)`: Retrieves detailed information for a topic based on its URL.

#### Development Workflow

1. **Fork the Repository**: Create your own fork of the `eksi-api` repository.

2. **Create a Feature Branch**: Develop your feature in a new branch.

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Run Tests**: Ensure your changes don't break existing functionality.

4. **Submit a Pull Request**: When your feature is ready, submit a PR to the main repository.

#### Testing

Add unit tests for any new features or modifications. Ensure that the tests cover edge cases and are robust.

#### Code Style

Follow PEP 8 guidelines for Python code. Use descriptive variable names and include comments where necessary to explain complex logic.

#### Future Enhancements

- Add user authentication for API access.
- Implement caching to improve performance.
- Add more granular search options (e.g., search within a specific time frame).

By following this documentation, developers can contribute effectively to the `eksi-api` project and ensure the continued improvement of the codebase.
