# Customer Inquiry Manager

A Python application that creates, tracks, updates, and stores customer inquiries using unique inquiry IDs, timestamps, status validation, exception handling, and JSON persistence.

## Features

- Creates customer inquiries
- Assigns unique inquiry IDs
- Tracks Open and Closed status
- Records created and updated timestamps
- Validates user-entered status values
- Handles missing inquiry IDs
- Saves inquiry records to JSON
- Loads saved records when the program starts
- Produces summary counts

## Python Concepts Used

- Functions
- Lists
- Dictionaries
- Loops
- Conditional logic
- f-strings
- datetime
- try/except
- JSON
- File handling
- User input

## Example Output

```text
Inquiry ID: INC-1002
Customer: Taylor Smith
Issue: Questions about an invoice
Priority: high
Status: Closed

Total inquiries checked: 2
Open inquiries: 1
Closed inquiries: 1