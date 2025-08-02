import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
import smtplib
from email.message import EmailMessage


excel_file = 'students.xlsx' #create a excel file with Column 1 with Name list And Column 2 with Email ID
template_path = 'Certificate_template.png' #template certificate
output_folder = 'certificates' 
font_path = 'GreatVibes-Regular.ttf' #font need to be downloaded fist to use ,otherwise use arial.ttf 
your_email = 'examplemail0@gmail.com' #provide your sender mail
your_password = 'abcdefghijklmn'  #replace the 16 digit password.Refer the README to know how to generate it.

font_size = 160
font_color = (255, 255, 255)
text_y = 1200 #Adjust y value for better alignment of the name.refer README


os.makedirs(output_folder, exist_ok=True)

try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print("❌ Font not found. Check the path.")
    exit()

template_img = Image.open(template_path).convert("RGB")
img_width, img_height = template_img.size

def generate_html(name):  #you can place another html content in this field or use the same and edit it as per your use
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


def send_email(to_email, name, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = "🎮 Game Development Workshop - Your Certificate"
    msg['From'] = your_email
    msg['To'] = to_email
    msg.set_content(f"Hi {name},\n\nPlease view this email in HTML. Your certificate is attached.")
    msg.add_alternative(generate_html(name), subtype='html')

   
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(your_email, your_password)
        smtp.send_message(msg)
        print(f"✅ Email sent to {name} ({to_email})")


df = pd.read_excel(excel_file)

for _, row in df.iterrows():
    name = str(row['Name']).strip()
    email = str(row['Email']).strip()


    cert_img = template_img.copy()
    draw = ImageDraw.Draw(cert_img)
    text_width = draw.textlength(name, font=font)
    text_x = (img_width - text_width) / 2
    draw.text((text_x, text_y), name, font=font, fill=font_color)

    cert_path = os.path.join(output_folder, f"{name}.png")
    cert_img.save(cert_path)
    print(f"✅ Certificate generated for: {name}")


    try:
        send_email(email, name, cert_path)
    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")

print("🎉 All certificates processed and emails sent!")

