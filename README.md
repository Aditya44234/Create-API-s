# Flask API Project

A comprehensive RESTful API built with Flask that demonstrates various web API concepts and patterns. This project serves as a learning resource for understanding Flask web development and API design.

## 🚀 Features

- **Basic Calculator API** - Perform arithmetic operations (add, subtract, multiply, divide)
- **User Data Management** - Submit and retrieve user information
- **Calculation History** - Track and manage calculation history
- **Data Export** - Export user data to CSV format
- **Error Handling** - Proper error responses for invalid operations
- **Multiple Parameter Types** - Support for both URL path parameters and query parameters

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd FLASK
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     env\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install flask
   ```

## 🚀 Running the Application

1. **Start the Flask server**
   ```bash
   python api.py
   ```

2. **Access the API**
   - The server will run on `http://localhost:5000`
   - API documentation and examples are provided below

## 📚 API Documentation

### Basic Information
- **GET** `/` - Get basic information about the API
  ```json
  {
    "name": "Aditya Joshi",
    "role": "Software Engineer",
    "message": "Welcome to your first flask API!",
    "id": 4561
  }
  ```

### Calculator Endpoints

#### 1. Simple Addition
- **GET** `/add/<a>/<b>` - Add two numbers
  ```
  Example: GET /add/5/3
  Response: {"num1": 5, "num2": 3, "result": 8}
  ```

#### 2. Arithmetic Operations (Path Parameters)
- **GET** `/calculate/<operation>/<a>/<b>` - Perform arithmetic operations
  - Operations: `add`, `sub`, `mul`, `div`
  ```
  Examples:
  GET /calculate/add/10/5    → {"operation": "add", "num1": 10, "num2": 5, "result": 15}
  GET /calculate/mul/4/6     → {"operation": "mul", "num1": 4, "num2": 6, "result": 24}
  GET /calculate/div/20/4    → {"operation": "div", "num1": 20, "num2": 4, "result": 5.0}
  ```

#### 3. Arithmetic Operations (Query Parameters)
- **GET** `/api/calculate?op=<operation>&a=<num1>&b=<num2>` - Same operations using query parameters
  ```
  Examples:
  GET /api/calculate?op=add&a=15&b=25
  GET /api/calculate?op=sub&a=50&b=20
  GET /api/calculate?op=mul&a=8&b=9
  GET /api/calculate?op=div&a=100&b=5
  ```

### Calculation History

#### 1. View History
- **GET** `/history` - Get the last 10 calculations performed
  ```json
  {
    "history": [
      {
        "operation": "add",
        "num1": 5,
        "num2": 3,
        "result": 8
      }
    ]
  }
  ```

#### 2. Clear History
- **GET** `/history/clear` - Clear all calculation history
  ```json
  {
    "message": "Calculation history cleared."
  }
  ```

### User Data Management

#### 1. Submit User Data
- **GET** `/submit?name=<name>&role=<role>&message=<message>&id=<id>` - Submit user information
  ```
  Example: GET /submit?name=John&role=Developer&message=Hello&id=123
  Response: {
    "message": "Data submitted successfully",
    "data": {
      "id": "123",
      "name": "John",
      "role": "Developer",
      "message": "Hello",
      "timestamp": "2024-01-15 10:30:45"
    }
  }
  ```

#### 2. View User History
- **GET** `/user_history` - Get all submitted user data
  ```json
  {
    "user_data": [
      {
        "id": "123",
        "name": "John",
        "role": "Developer",
        "message": "Hello",
        "timestamp": "2024-01-15 10:30:45"
      }
    ]
  }
  ```

#### 3. Export User Data
- **GET** `/export` - Download user data as CSV file

### Utility Endpoints

#### 1. API Information
- **GET** `/api` - Get information about APIs
  ```json
  {
    "API": "Application Programming Interface",
    "Description": "Basically an API is a way to communicate between different sites where different sites can communicate using some http methods such as GET,POST,DELETE,PUT etc."
  }
  ```

#### 2. Greeting
- **GET** `/greet/<name>` - Get a personalized greeting
  ```
  Example: GET /greet/Alice
  Response: {"greeting": "Hello, Alice!"}
  ```

## 🔧 Error Handling

The API includes proper error handling for:
- **Division by zero** - Returns 400 status with error message
- **Invalid operations** - Returns 400 status for unsupported operations
- **Missing parameters** - Returns 400 status when required parameters are missing
- **Empty data** - Returns 404 status when no data is available

## 📁 Project Structure

```
FLASK/
├── api.py              # Main Flask application
├── env/                # Virtual environment
├── static/
│   └── style.css       # CSS styles
├── templates/
│   └── index.html      # HTML templates
├── todo_api.py         # Additional API file
└── README.md           # This file
```

## 🧪 Testing the API

You can test the API using:
- **Web browser** - For GET requests
- **Postman** - For comprehensive API testing
- **cURL** - For command-line testing

### Example cURL commands:
```bash
# Test basic endpoint
curl http://localhost:5000/

# Test calculator
curl http://localhost:5000/calculate/add/10/5

# Test user submission
curl "http://localhost:5000/submit?name=Test&role=Developer&message=Hello&id=1"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Aditya Joshi**
- Role: Software Engineer
- GitHub: [Your GitHub Profile]

## 🙏 Acknowledgments

- Flask framework and its contributors
- Python community for excellent documentation
- All contributors and learners who use this project

---

⭐ If you find this project helpful, please give it a star!