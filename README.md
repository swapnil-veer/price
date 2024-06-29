# Price Comparison API Project

This project is a RESTful API for a price comparison service that aggregates product prices from various online stores. The API is built using Django and Django REST Framework, and it incorporates JWT Token Authentication, a custom user model, pagination, throttling, caching, and AWS services (S3 bucket and Lambda).

## Features

- **JWT Token Authentication**: Secure user authentication using JSON Web Tokens.
- **Custom User Model**: Extended user model to include additional fields and functionalities.
- **Pagination**: Efficiently handle large datasets with pagination.
- **Throttling**: Limit the number of requests a user can make to prevent abuse.
- **Django Caching**: Improve performance with caching mechanisms.
- **AWS Integration**: Use AWS S3 for file storage and AWS Lambda for serverless functions.

## Getting Started

### Prerequisites

- Python 3.7+
- Django 3.2+
- Django REST Framework
- Docker (for optional containerization)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/price-comparison-api.git
    cd price-comparison-api
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

    Create a `.env` file in the project root and add the necessary environment variables.

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=your_database_url
    AWS_ACCESS_KEY_ID=your_aws_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret_key
    AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
    ```

5. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

### Endpoints

- **Search Products**: `GET /api/products?name=<product_name>`
- **Add Product**: `POST /api/products`
- **Get All Products**: `GET /api/products`


## Deployment

### Docker

1. **Build the Docker Image**

    ```bash
    docker build -t price-comparison-api .
    ```

2. **Run the Docker Container**

    ```bash
    docker run -p 8000:8000 price-comparison-api
    ```

### AWS

To deploy the API on AWS, you can use services like Elastic Beanstalk or EC2. Ensure you configure your environment variables and AWS credentials correctly.

## Tests

Run the tests with the following command:

```bash
python manage.py test
```

## Documentation

API documentation is available at /api/docs once the server is running.

## Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or feedback, please contact swapnil.veer095@gmail.com

```css
This README includes headings, lists, and code blocks to make it more readable and organized
```
