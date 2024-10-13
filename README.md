# System Information API

This Django REST API provides endpoints to retrieve system information including CPU usage, memory statistics, network statistics, and temperature readings of the machine the application is running on. It leverages the `psutil` library to access system-level metrics.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Get CPU usage percentage.
- Retrieve memory usage statistics (total, used, available).
- Access network I/O statistics (bytes sent and received).
- Retrieve temperature readings (if supported by the system).

## Requirements

- Python 3.9 or higher
- Django 5.1 or higher
- Django REST Framework
- psutil

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AKRASH-Nadeem/System-Info-RESTAPI.git
   cd system-info-api
