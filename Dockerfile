# Stage 1: Build stage
FROM python:3.10.12-alpine as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies will with C files like nummpy etc 
RUN apk --no-cache add build-base

# Create a new user
RUN adduser -D django-user

WORKDIR /app

COPY ./requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

#Remove build dependencies that are not needed 
RUN apk del build-base

COPY . /app

# Set ownership to the user
RUN chown -R django-user /app

# Set the user
USER django-user

# Run collectstatic
RUN python manage.py collectstatic --no-input

# Stage 2: Runtime stage
FROM python:3.10.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a new user
RUN adduser -D django-user

WORKDIR /app

# Copy all the complied & installed dependencies
COPY --from=builder --chown=django-user:django-user /usr/local /usr/local

# Copy the built project from the builder stage
COPY --from=builder --chown=django-user:django-user /app .

# Set the user
USER django-user

EXPOSE 8000

#use gunicorn to serve the project
CMD python manage.py runserver
