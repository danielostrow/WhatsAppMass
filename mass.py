import csv
import pywhatkit
import time
import pyautogui
import os

# Define the message to be sent
message = "Enter message here."

# Function to send message
def send_message(phone_number, message):
    try:
        # Send the message
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        time.sleep(10)  # Wait for the WhatsApp Web to load

        # Save a screenshot of the message input area
        screenshot_path = f'message_input_{phone_number}.png'
        pyautogui.screenshot(screenshot_path)

        # Locate the message input area
        input_location = pyautogui.locateOnScreen(screenshot_path)
        if input_location:
            pyautogui.click(input_location)  # Click on the message input area
            pyautogui.press('enter')  # Simulate pressing "Enter" to send the message
            os.remove(screenshot_path)  # Delete the screenshot after sending the message
            return True
        else:
            print(f"Message input area not found for {phone_number}")
            os.remove(screenshot_path)  # Cleanup the screenshot even if not found
            return False
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")
        return False

# Load CSV and send messages
csv_file = 'phone_numbers.csv'  # Replace with the path to your .csv file

with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        phone_number = row['phone_number']
        if send_message(phone_number, message):
            print(f"Message sent to {phone_number}")
        else:
            print(f"Failed to send message to {phone_number}")

print("All messages have been sent.")
# let the script run without clicking off the pop-up browser.
