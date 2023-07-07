# Traffic Ticket Management System

The Traffic Ticket Management System is a Python application built using the wxPython library. It provides a graphical user interface (GUI) for managing traffic ticket data, allowing users to enter new tickets, view existing tickets, and perform various operations on the ticket data.

## Features

- Ticket Entry Box: Users can enter details of a traffic ticket, including ticket ID, time, posted speed, age, date, actual speed, MPH over the speed limit, and violator's sex.
- Data Table: Displays a table of all entered traffic tickets with columns for ticket ID, stop date, stop time, actual speed, posted speed, MPH over the speed limit, violator's age, and violator's sex.
- Display Button: Retrieves and displays all the ticket data from the underlying SQLite database.
- Insert Citation Button: Opens a dialog box to enter a new traffic ticket and inserts it into the database.
- Cancel Button: Closes the application.

## Prerequisites

- Python 3.x
- wxPython
- SQLite 3

## Installation

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install wxPython sqlite3
   ```
3. Ensure that you have a SQLite database file named "speeding_tickets.db" in the same directory as the script. If not, you can create an empty database file or modify the code to point to an existing database file.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.
2. Run the following command to start the application:
   ```
   python traffic_ticket_management.py
   ```
3. The main application window will open, displaying the ticket data table.
4. Click the "Insert Citation" button to add a new traffic ticket. Enter the ticket details in the dialog box and click "OK" to save the ticket.
5. Click the "Display" button to retrieve and display all the ticket data from the database.
6. The ticket data will be shown in the table, and you can scroll through the data or resize the columns as needed.
7. To exit the application, click the "Cancel" button or close the window.

## Limitations

- The application assumes the existence of a SQLite database file named "speeding_tickets.db" in the same directory as the script. Ensure that the database file is available or modify the code to use a different database file.
- Error handling is minimal in the provided code. You may need to enhance it to handle potential exceptions or errors that could occur during database operations.

## Contributing

Contributions to the Traffic Ticket Management System are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- The Traffic Ticket Management System is based on the wxPython library, which provides the GUI framework.
- The application utilizes SQLite for database management.
