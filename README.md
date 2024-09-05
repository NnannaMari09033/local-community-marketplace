# Local Community Marketplace API

This project is an API for a local community marketplace where users can buy, sell, and trade items. The API consists of three main apps: `account`, `listings`, and `messaging`. Each app serves a specific purpose in managing users, their listings, and their communication within the platform.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
  - [Account Management](#account-management)
  - [Listings](#listings)
  - [Messaging](#messaging)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Project Overview

The Local Community Marketplace API is designed to facilitate the buying, selling, and trading of items within a local community. Users can create accounts, post listings, and communicate with each other regarding specific products. This API serves as the backend for a marketplace platform, providing all the necessary functionalities through a RESTful interface.

## Features

### Account Management

- User Registration: Allows users to register with an email and password.
- Authentication: JWT-based authentication system.
- Profile Management: Users can update their profile information including their bio and profile picture.
- User Roles: Supports both admin and regular user roles.

### Listings

- CRUD Operations: Users can create, read, update, and delete their listings.
- Search Functionality: Users can search for listings by title, description, or category.
- Filtering: Listings can be filtered by price range, category, and date posted.

### Messaging

- Direct Communication: Allows users to send messages to each other regarding specific listings.
- CRUD Operations: Users can create, read, update, and delete their messages.

## Dependencies

The following Python packages are required to run this project:

```plaintext
asgiref==3.8.1
Django==5.1
django-filter==24.3
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
pillow==10.4.0
PyJWT==2.9.0
sqlparse==0.5.1
typing_extensions==4.12.2
Installation
Follow these steps to get the project up and running:

Clone the repository:

bash
git clone https://github.com/NnannaMari09033/local-community-marketplace.git
cd local-community-marketplace
Create and activate a virtual environment:

bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
Install the dependencies:

bash
pip install -r requirements.txt
Apply migrations:

bash
python manage.py migrate
Create a superuser (optional but recommended):

bash
python manage.py createsuperuser
Run the development server:

bash
python manage.py runserver
Usage
Once the server is running, you can interact with the API using tools like Postman or Curl. The following endpoints are available:

Account
Register: POST /account/register/
Login: POST /account/login/
Update Profile: PUT /account/profile/
Delete Account: DELETE /account/delete/
Listings
Create Listing: POST /listings/create/
View Listings: GET /listings/
Update Listing: PUT /listings/update/<id>/
Delete Listing: DELETE /listings/delete/<id>/
Search Listings: GET /listings/search/?query=<search_term>
Filter Listings: GET /listings/filter/?price_min=&price_max=&category=&date_posted=
Messaging
Send Message: POST /messaging/send/
View Messages: GET /messaging/
Update Message: PUT /messaging/update/<id>/
Delete Message: DELETE /messaging/delete/<id>/
Contact
For any inquiries or support, please contact:
Email: nnannamari@gmail.com

Note: This project is developed as a backend API and does not include frontend components. It is designed to be used with tools like Postman for API testing and integration with other frontend frameworks or applications.

