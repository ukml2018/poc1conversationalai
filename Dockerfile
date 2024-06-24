# Use a base image with Python installed
#FROM python:3.9-slim-buster
FROM python:3
RUN  pip3 install --upgrade pip
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit Python application to the working directory
#COPY your_app.py .
COPY . /app

# Expose the default Streamlit port (8501)
EXPOSE 8501

# Set the command to run when the container starts
#CMD ["streamlit", "run", "--server.port", "8501", "your_app.py"]
CMD ["streamlit", "run", "--server.port", "8501", "application.py"]
