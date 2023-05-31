# Use a base image with Python installed
FROM python:3.9

# Set the working directory
WORKDIR /etl-app

# Copy my Python code into the container
COPY etl-app.py .

# Install dependencies
RUN pip3 install requests

# Set command to run the Python code
CMD ["python3", "etl-app.py"]
