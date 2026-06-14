# DeskGuard
# DeskGuard Library

DeskGuard Library is a smart library desk management system that helps monitor desk occupancy in real time. The system allows students to check in to a desk, tracks desk usage, and automatically frees desks when the allotted time expires.

## Features

- Real-time desk availability tracking
- Occupied, Free, and Away desk status indicators
- Automatic desk timeout management
- Library occupancy visualization
- Responsive web interface
- SQLite database integration
- Flask backend
- Server-side occupancy management

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

## Project Structure

```
DeskGuard/
│
├── static/
│   ├── assets/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── desk.html
│   └── dashboard.html
│
├── app.py
├── database.py
├── database.db
├── requirements.txt
└── README.md
```

## How It Works

1. Users select a desk.
2. A desk can be marked as:
   - Free
   - Occupied
   - Away
3. Occupied desks store check-in information.
4. A server-side timer periodically checks for expired desk sessions.
5. Expired desks are automatically released and marked as available.

## Installation

### Clone Repository

```bash
git clone https://github.com/anjali-pandey1641/DeskGuard-Library.git
cd DeskGuard-Library
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Future Improvements

- User authentication
- QR-based desk check-in
- PostgreSQL support
- Analytics dashboard
- Notification system
- Multi-library support
- Cloud deployment

## Use Cases

- College libraries
- Reading halls
- Study centers
- Co-working spaces
- Computer laboratories

## Team

Developed for a Hackathon Project.

## License

This project is developed for educational and hackathon purposes.