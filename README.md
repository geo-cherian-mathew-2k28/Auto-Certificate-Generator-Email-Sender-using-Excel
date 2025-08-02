🎓 Automated Certificate Generator & Email Sender
This project provides a straightforward and automated way to create personalized participation certificates and send them to attendees via email. It's designed for anyone needing to efficiently distribute certificates for events like workshops, webinars, or courses.

✨ Key Features
Generate Personalized Certificates: Creates a unique PNG certificate for each person from a single template.

Custom Name Placement: Adds attendee names to certificates using your chosen font and precise positioning.

Automated Email Delivery: Sends certificates as attachments to all recipients listed in your data.

Customizable Email Content: Includes a flexible HTML email template for event details and links.

🚀 Getting Started
Follow these steps to set up and run the script.

Prerequisites
You'll need:

Python 3.x: Download from python.org/downloads. Remember to check "Add Python to PATH" during installation.

Gmail Account with App Password:

Enable 2-Step Verification on your Google Account: myaccount.google.com/security.

Generate an "App password" under "App passwords" in the security settings. Select "Mail" and "Other (Custom name)", then copy the 16-character password. This is what the script will use, not your regular Gmail password.

Installation
Download Project Files: Get the project files by cloning the repository or downloading the ZIP and extracting it.

Install Libraries: Open your terminal/command prompt, navigate to the project folder, and run:

pip install pandas Pillow

⚙️ Configuration
Prepare your files and adjust the script settings.

1. Prepare Your Data (students.xlsx)
Create an Excel file named students.xlsx in your project folder. It must have two columns: Name and Email.

Example students.xlsx:

| Name | Email |
| Alice Wonderland | alice@example.com |
| Bob The Builder | bob@example.com |

2. Add Your Certificate Template (participation tedx 25.png)
Place your certificate design (a PNG image) named participation tedx 25.png in the project folder. Ensure it has a blank area for the name.

3. Include Your Font File (GreatVibes-Regular.ttf)
Place your chosen font file (a .ttf file) in the project folder. You can find free fonts on Google Fonts.

4. Configure main.py
Open main.py in a text editor and update the following lines:

a. Your Email & App Password
your_email = 'example.email@gmail.com' # <--- Your Gmail address
your_password = 'abcd1234efgh5678' # <--- Your 16-character App Password

b. Font Settings (Name Placement)
Adjust these values to position and style the name on your certificate.

font_size = 160 # Size of the name text
font_color = (255, 255, 255) # RGB color (e.g., (0, 0, 0) for black, (255, 255, 255) for white)
text_y = 1200 # Vertical position of the name.

Tip for text_y: This number controls how high or low the name appears.

To move the name down, increase text_y.

To move the name up, decrease text_y.
You'll likely need to try different numbers and re-run the script until the name is perfectly aligned.

c. HTML Email Content
Customize the text and links in the email that will be sent to attendees.

def generate_html(name):
    return f"""
    <!DOCTYPE html>
    <html>
    <body>
        <!-- Your custom HTML content for the email -->
        <p>Hey <strong>{name}</strong>, here's your certificate!</p>
        <p>Join our WhatsApp Group: <a href="https://chat.whatsapp.com/your-group-link">Link</a></p>
    </body>
    </html>
    """

🏃 Running the Script
Open your terminal or command prompt.

Navigate to your project folder.

Run the script:

python main.py

The script will then generate certificates and send emails, showing progress in the console.

🐛 Troubleshooting
"Font not found.": Ensure your font file is in the project folder and font_path in main.py is correct.

"Failed to send email...": Double-check your your_email and your_password in main.py, and confirm 2-Step Verification is on for your Gmail.

"No module named 'pandas'" or "'PIL'": You missed installing the libraries. Run pip install pandas Pillow again.

Name is misplaced/wrong size: Adjust font_size and text_y in main.py as described in the "Font Settings" section.

🤝 Contributing
Feel free to contribute to this project by opening issues or submitting pull requests!
