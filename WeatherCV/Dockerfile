# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE projectname.settings

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt 

# Expose the port the app runs on
EXPOSE 8000

# Run the command to start the Django app
CMD ["python3", "manage.py", "runserver"]