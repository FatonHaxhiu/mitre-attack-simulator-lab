# Use an official Python base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy the code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command
CMD ["python3", "lab_manager.py"]