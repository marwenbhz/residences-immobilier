# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:2
 
# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
 
# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
 
# Install Scrapy specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .
 
# Run the crawler when the container launches.
CMD [ "python", "./crawl_residences-immobilier.py" ] 
