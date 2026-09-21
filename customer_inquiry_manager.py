# Customer Inquiry Manager
# Stores customer inquiries, tracks their status,
# records timestamps, and saves data to a JSON file.

from datetime import datetime
import json


# -----------------------------
# LOAD SAVED DATA
# -----------------------------

# Load previously saved customer inquiries
def load_inquiries():

    try:
        # Open the saved JSON file in read mode
        with open("customer_inquiries.json", "r") as file:

            # Convert the JSON data back into a Python list
            loaded_inquiries = json.load(file)

            # Return all saved inquiry records
            return loaded_inquiries

    except FileNotFoundError:

        # If the file does not exist yet,
        # start with an empty list instead of crashing
        print("No saved inquiry file found.")

        return []

    except json.JSONDecodeError:

        # If the file exists but cannot be read as valid JSON,
        # start safely with an empty list
        print("Inquiry file could not be read.")

        return []


# Load saved inquiries when the program starts
inquiries = load_inquiries()

# Show how many records were loaded
print(f"\nLoaded {len(inquiries)} saved inquiries.")


# -----------------------------
# FUNCTIONS
# -----------------------------

# Create a new customer inquiry
def add_inquiry(customer, issue, priority):

    # Create a unique inquiry ID
    inquiry_id = f"INC-{len(inquiries) + 1001}"

    # Create one dictionary containing the inquiry details
    inquiry = {
        "inquiry_id": inquiry_id,
        "customer": customer,
        "issue": issue,
        "priority": priority,
        "status": "Open",

        # Record when the inquiry was created
        "created_at": datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p"
        )
    }

    # Add the inquiry dictionary to the list
    inquiries.append(inquiry)

    # Return the inquiry that was created
    return inquiry


# Update an inquiry using its unique ID
def update_status(inquiry_id, new_status):

    # Loop through every inquiry
    for inquiry in inquiries:

        # Find the matching inquiry ID
        if inquiry["inquiry_id"] == inquiry_id:

            # Update the status
            inquiry["status"] = new_status

            # Record the update time
            inquiry["updated_at"] = datetime.now().strftime(
                "%m/%d/%Y %I:%M:%S %p"
            )

            # Return the updated inquiry
            return inquiry

    # Return None if the ID was not found
    return None


# Save all inquiries to a JSON file
def save_inquiries():

    # Open the JSON file in write mode
    with open("customer_inquiries.json", "w") as file:

        # Save the full inquiries list
        # indent=4 makes the file easier to read
        json.dump(
            inquiries,
            file,
            indent=4
        )

# Display a summary of inquiry activity
def display_summary(open_count, closed_count):

    # Show the total number of inquiries
    print(f"\nTotal inquiries checked: {len(inquiries)}")

    # Show the number of Open inquiries
    print(f"Open inquiries: {open_count}")

    # Show the number of Closed inquiries
    print(f"Closed inquiries: {closed_count}")



# -----------------------------
# CREATE STARTER INQUIRIES
# -----------------------------

# Only create starter records if no saved inquiries exist
if len(inquiries) == 0:

    result = add_inquiry(
        "Jordan Lee",
        "Cannot log into account",
        "high"
    )

    result = add_inquiry(
        "Taylor Smith",
        "Questions about an invoice",
        "high"
    )


# -----------------------------
# UPDATE STATUS
# -----------------------------

# Ask the user which inquiry should be updated
inquiry_id = input(
    "\nEnter inquiry ID: "
).strip().upper()

# Ask the user for the new status
new_status = input(
    "Enter new status (Open or Closed): "
).strip().title()


# Validate the status
if new_status == "Open" or new_status == "Closed":

    # Try to update the inquiry
    result = update_status(
        inquiry_id,
        new_status
    )

    # Check whether the inquiry was found
    if result is None:
        print("\nInquiry not found.")

    else:
        print(
            f"\n{inquiry_id} was updated to {new_status}."
        )

else:
    print(
        "\nInvalid status. "
        "Please enter Open or Closed."
    )


# -----------------------------
# COUNT AND DISPLAY INQUIRIES
# -----------------------------

open_count = 0
closed_count = 0

for inquiry in inquiries:

    # Count Open inquiries
    if inquiry["status"] == "Open":
        open_count += 1

    # Count Closed inquiries
    elif inquiry["status"] == "Closed":
        closed_count += 1

    # Display each inquiry
    print(f"\nInquiry ID: {inquiry['inquiry_id']}")
    print(f"Customer: {inquiry['customer']}")
    print(f"Issue: {inquiry['issue']}")
    print(f"Priority: {inquiry['priority']}")
    print(f"Status: {inquiry['status']}")
    print(f"Created At: {inquiry['created_at']}")

    # Only display Updated At if the inquiry was changed
    if "updated_at" in inquiry:
        print(f"Updated At: {inquiry['updated_at']}")


# -----------------------------
# DISPLAY SUMMARY
# -----------------------------

# Display the final inquiry summary
display_summary(
    open_count,
    closed_count
)

# -----------------------------
# SAVE DATA
# -----------------------------

# Save all inquiry records before the program finishes
save_inquiries()

print("\nInquiry records saved successfully.")