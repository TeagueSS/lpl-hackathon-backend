# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./

# Uninstall any conflicting bson package and install pymongo
RUN pip uninstall -y bson pymongo && \
    pip install --no-cache-dir -r requirements.txt

# Uninstall conflicting bson package (if any)
RUN pip uninstall -y bson pymongo && \
    pip install --no-cache-dir pymongo==4.10.1
# Copy the project files
COPY . .

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
