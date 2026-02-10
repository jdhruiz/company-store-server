# Company Store Backend Server

This project implements a deployable backend server for a small company store. It provides a database-backed service that can be accessed by client machines over a network. The system is designed to be lightweight, portable, and reproducible, and is intended for deployment on a Raspberry Pi.

The backend is containerized using Docker so it can be developed and tested locally before being deployed to hardware.

---

## Project Overview

The system consists of two main components:

- **PostgreSQL Database**
  - Stores cadets, items, orders, and order items
  - Initialized automatically from a SQL schema
- **Flask API Server**
  - Provides an HTTP interface for client interaction
  - Acts as an intermediary between clients and the database

Both components are managed using **Docker Compose**, allowing the entire system to be started with a single command.

---

## Database Schema

The database schema is defined in `db/schema.sql` and includes the following tables:

- **cadets** – stores cadet information
- **items** – stores inventory and pricing
- **orders** – represents orders placed by cadets
- **order_items** – associates items with orders and quantities

The schema is automatically applied when the database container is created.


## Running the Server Locally

### Prerequisites
- Docker
- Docker Compose

### Start the system

From the project root directory:

```bash
docker compose up --build
