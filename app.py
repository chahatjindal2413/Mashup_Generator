from flask import Flask, request, render_template_string
import subprocess
import zipfile
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

HTML_FORM = """
<h2>Mashup Generator</h2>
<form method="POST">
Singer Name: <input type="text" name="singer" required><br><br>
Number of Videos: <input type="number" name="videos" required><br><br>
Duration (seconds): <input type="number" name="duration" required><br><br>
Email: <input type="email" name="email" required><br><br>
<input type="submit" value="Generate Mashup">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = request.form["videos"]
        duration = request.form["duration"]
        email = request.form["email"]

        output_file = "web_output.mp3"

        # Run Program 1
        subprocess.run([
            "python", "102303831.py",
            singer,
            videos,
            duration,
            output_file
        ])

        # Zip the file
        zip_filename = "mashup_result.zip"
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            zipf.write(output_file)

        # Send Email
        send_email(email, zip_filename)

        return "<h3>Mashup created and sent to your email!</h3>"

    return render_template_string(HTML_FORM)


def send_email(receiver, zip_file):
    sender_email = "ccjindal1312@gmail.com"
    app_password = "wsdinsrraofsptgp"

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender_email
    msg["To"] = receiver
    msg.set_content("Your mashup is attached.")

    with open(zip_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename=zip_file
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)


if __name__ == "__main__":
    app.run(debug=True)
