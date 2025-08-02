# Auto-Certificate-Generator-Email-Sender-using-Excel
🎓 Automated Certificate Generator & Email Sender
This project provides a robust solution for automating the generation and distribution of personalized participation certificates via email. It's ideal for educational institutions, event organizers, or any entity requiring efficient certificate issuance for workshops, webinars, or conferences.

✨ Key Features
Dynamic Certificate Generation: Creates unique PNG certificates for each participant based on a provided template.

Personalized Content: Automatically embeds participant names onto certificates using a specified font and positioning.

Batch Email Distribution: Facilitates the bulk emailing of certificates as attachments to a list of recipients.

Customizable HTML Email Template: Includes a rich HTML email body, allowing for detailed event information and calls to action (e.g., WhatsApp group links).

🚀 Getting Started
Follow these instructions to set up and run the certificate automation script.

Prerequisites
Before you begin, ensure you have the following installed and configured:

Python 3.x: Download and install Python from python.org/downloads. During installation, ensure you check the option "Add Python to PATH".

Gmail Account with 2-Step Verification: This script uses Gmail's SMTP server. For security, you'll need to enable 2-Step Verification on your Google Account and generate an App Password.

Navigate to myaccount.google.com/security.

Under "How you sign in to Google," ensure 2-Step Verification is ON.

Click on App passwords, select "Mail" as the app and "Other (Custom name)" for the device (e.g., "Certificate Sender"), then generate and copy the 16-character password. This is crucial and different from your regular Gmail password.

Installation
Download the Project:

Clone this repository or download the ZIP file and extract its contents to your desired directory.

Install Required Python Libraries:

Open your terminal or command prompt.

Navigate to the project directory using the cd command (e.g., cd path/to/your/project).

Run the following commands to install the necessary libraries:

pip install pandas
pip install Pillow



⚙️ Configuration
Before running the script, you must configure several parameters and prepare your input files.

1. Prepare Your Data (students.xlsx)
Create an Excel file named students.xlsx in the root of your project directory. This file must contain two columns:

Name: Full name of the participant.

Email: Email address of the participant.

Example students.xlsx:

Name

Email

Alice Wonderland

alice@example.com

Bob The Builder

bob@example.com

Charlie Chaplin

charlie@example.com

2. Add Your Certificate Template (participation tedx 25.png)
Place your certificate design as a PNG image file named participation tedx 25.png in the project directory. Ensure this template has a blank space where the participant's name should be inserted.

3. Include Your Font File (GreatVibes-Regular.ttf)
Place your desired TrueType Font (.ttf) file (e.g., GreatVibes-Regular.ttf) in the project directory. This font will be used for rendering names on the certificates. You can find free fonts on Google Fonts.

4. Configure main.py
Open main.py in a text editor and modify the following sections:

a. Configurable Paths & Credentials
Update the your_email and your_password variables with your Gmail address and the 16-character App Password generated in the prerequisites section.

# === Configurable Paths ===
excel_file = 'students.xlsx'
template_path = 'participation tedx 25.png'
output_folder = 'certificates'
font_path = 'GreatVibes-Regular.ttf'
your_email = 'example.email@gmail.com' # <--- UPDATE THIS! (e.g., your actual Gmail address)
your_password = 'abcd1234efgh5678' # <--- UPDATE THIS! (e.g., your 16-character App Password)



b. Font Settings (Crucial for Placement)
Adjust font_size, font_color, and especially text_y to ensure the name is correctly positioned and styled on your certificate template.

# === Font Settings ===
font_size = 160 # Adjust as needed for name size
font_color = (255, 255, 255) # RGB color for the text (e.g., (0, 0, 0) for black, (255, 255, 255) for white)
text_y = 1200 # Vertical position for the name. Adjust this value through trial and error.



Tip for text_y: This value determines the vertical placement of the name.

To move the name down on the certificate, increase the text_y value.

To move the name up on the certificate, decrease the text_y value.
You'll likely need to experiment with different numbers (e.g., 1000, 1100, 1200, 1300) to find the perfect alignment for your specific certificate template. Run the script, check the generated certificates, adjust text_y, and repeat until satisfied.

c. HTML Email Template (Optional Customization)
Modify the generate_html(name) function to customize the content, date, time, venue, and WhatsApp group link within the email body.

def generate_html(name):
    return f"""
    <!DOCTYPE html>
    <html>
    <body style="background: #f5f5f5; font-family: 'Segoe UI', sans-serif;">
        <div style="max-width: 600px; margin: auto; background: #fff; padding: 20px; border-radius: 10px;">
            <h2 style="color: #7928CA;">🎮 Expert Game Development Workshop</h2>
            <p>Hey <strong>{name}</strong>,</p>
            <p>Here’s your certificate for attending the workshop!</p>
            <p><strong>Date:</strong> 2nd August 2025<br>
                <strong>Time:</strong> 9:00 AM<br>
                <strong>Venue:</strong> AJCE, ACM Chapter</p>
            <p>Explore the world of game dev with us! 👾</p>
            <a href="https://chat.whatsapp.com/your-group-link"
                style="display: inline-block; background: #FF0080; color: #fff; padding: 12px 20px; border-radius: 6px; text-decoration: none;">
                👉 Join WhatsApp Group
            </a>
            <p style="font-size: 12px; color: #888; margin-top: 30px;">© 2025 ACM Chapter | AJCE</p>
        </div>
    </body>
    </html>
    """



🏃 Usage
Once all configurations are complete, execute the script from your terminal:

Open your terminal or command prompt.

Navigate to your project directory.

Run the script:

python main.py



The script will:

Read participant data from students.xlsx.

Create an certificates output folder.

Generate and save a personalized .png certificate for each participant in the certificates folder.

Send a customized email with the generated certificate attached to each participant.

Provide real-time progress updates in the console.

🐛 Troubleshooting
IOError: Font not found.: Ensure the font_path variable in main.py correctly points to your .ttf font file, and that the file is present in the specified location.

Failed to send email...:

Verify that your_email and your_password (the 16-character App Password) are correctly entered in main.py.

Confirm that 2-Step Verification is enabled for your Gmail account.

Check for any typos in the email addresses within students.xlsx.

ModuleNotFoundError: No module named 'pandas' or 'PIL': This indicates that the required Python libraries were not installed. Revisit the "Install Required Python Libraries" step in the Installation section.

Incorrect Name Placement/Size on Certificate: Adjust the font_size and text_y variables in the "Font Settings" section of main.py until the name appears correctly on the certificate. This often requires a few iterations.
