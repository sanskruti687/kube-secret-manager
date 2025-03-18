# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
