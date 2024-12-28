# E-Commerce Web Application

## Project Overview
This project is a comprehensive **E-Commerce Web Application** designed to provide users with a seamless shopping experience. It features user authentication, product management, a shopping cart system, secure password reset capabilities, and Paytm payment integration.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **User Authentication**: Secure user sign-up and login processes, including email verification and account activation.
- **Product Management**: A comprehensive product catalog with categories, subcategories, and detailed product information.
- **Shopping Cart**: Users can add, remove, and update products in their cart, with real-time updates and local storage functionality.
- **Password Reset**: A secure password reset system that sends reset links via email, ensuring user data protection.
- **Payment Integration**: Seamlessly integrated Paytm payment gateway with checksum generation and verification for secure transactions.
- **Responsive Design**: Fully responsive and optimized for various devices, providing a smooth user experience on desktops, tablets, and smartphones.

## Technologies Used
- **Backend**: Django, Express.js
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: MongoDB
- **Email Service**: SMTP
- **Payment Gateway**: Paytm

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ecommerce-web-app.git
    cd ecommerce-web-app
    ```

2. **Backend Setup**:
    - **Install dependencies**:
      ```bash
      pip install -r requirements.txt
      ```
    - **Set up MongoDB**:
      - Ensure MongoDB is running and accessible.
    - **Run the server**:
      ```bash
      python manage.py runserver
      ```

3. **Frontend Setup**:
    - **Navigate to the frontend directory**:
      ```bash
      cd frontend
      ```
    - **Install dependencies**:
      ```bash
      npm install
      ```
    - **Run the frontend server**:
      ```bash
      npm start
      ```

## Configuration
### Paytm Integration
Create a `paytmConfig.js` file to store your Paytm credentials:
```javascript
module.exports = {
    mid: 'YOUR_MID_HERE',
    key: 'YOUR_MERCHANT_KEY_HERE',
    website: 'YOUR_WEBSITE_NAME',
    callbackUrl: 'YOUR_CALLBACK_URL'
};
