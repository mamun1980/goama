# Use a slim version of the Python image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app


# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the Django app code into the container
COPY . /app/

# RUN bash scripts/load_fixture_data.sh
# Configure Nginx
# COPY nginx.default /etc/nginx/sites-available/default

# Copy the entrypoint script
# COPY entrypoint.sh /app/

# Grant execute permissions to the entrypoint script
# RUN chmod +x /app/entrypoint.sh

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Set the entrypoint script as the container entrypoint
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]