# smartquote_backend
Automate the pricing process with a scalable solution designed for production, leveraging microservices, containerized with FastAPI, and integrated with generative AI services.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Build and Run the Services

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd aipricing_backend
    ```
2. Create .env file to storage enviroment variable such as:

    ```sh
    OPENAI_API_KEY=EXAMPLEOFAPIKEY
    ```

3. Build and start the services using Docker Compose:

    ```sh
    docker-compose up --build
    ```

4. The services will be available at the following URLs:
    - AI Service: `http://localhost:8001`
    - Quotation Service: `http://localhost:8000`

### Endpoints

#### AI Service

- `GET /`: Check if the AI service is running.
- `POST /chat/`: Send a message to the AI model and receive a response.

#### Quotation Service

- `GET /`: Check if the Quotation service is running.
- `POST /generate_quote`: Generate a quotation.

## Example of curl for Lanchaing chat response

curl -X POST http://localhost:8001/chat/ -H "Content-Type: application/json" -d "{\"message\": \"Qué es una plan premium en odoo?\"}"

## Dependencies

### AI Service (`ms_ai`)

- fastapi
- uvicorn
- python-dotenv
- langchain-openai
- langchain-core

### Quotation Service (`ms_pricing`)

- fastapi
- uvicorn
- pandas
- openpyxl

## License

This project is licensed under the MIT License.
