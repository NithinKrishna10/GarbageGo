# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client library
RUN apt-get update && apt-get install -y libpq-dev

# Copy the Django project code into the container
COPY . .

# Expose the port on which your Django application will run
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=myproject.settings.prod
ENV DATABASE_URL=postgres://postgres:postgres@db:5432/postgres

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
