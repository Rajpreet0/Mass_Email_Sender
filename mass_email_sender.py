import tkinter as tk
from tkinter import filedialog, Text, Label, Entry, Button, Scrollbar, Frame, messagebox, ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication  
import csv

def select_csv():
    global csv_file_path
    csv_file_path = filedialog.askopenfilename(title='Select CSV File', filetypes=[('CSV Files', '*.csv')])
    csv_label.config(text="Selected: " + csv_file_path.split("/")[-1])

def select_attachment():
    global attachment_file_paths
    attachment_file_paths = filedialog.askopenfilenames(title='Select Attachments')  # Note the 's' in 'askopenfilenames'
    # Create a readable list of selected files for the label
    selected_files = ", ".join([path.split("/")[-1] for path in attachment_file_paths])
    attachment_label.config(text=f"Selected: {selected_files}")

def send_emails():
    email_address = email_entry.get()
    email_password = password_entry.get()
    
    # Determine SMTP settings based on the selected email provider
    if provider_var.get() == 'Gmail':
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
    elif provider_var.get() == 'Outlook':
        smtp_server = 'smtp.office365.com'
        smtp_port = 587
    elif provider_var.get() == 'Yahoo':
        smtp_server = 'smtp.mail.yahoo.com'
        smtp_port = 587
    elif provider_var.get() == 'Web.de':
        smtp_server='smtp.web.de'
        smtp_port = 587
    elif provider_var.get() == 'Gmx':
        smtp_server = 'mail.gmx.com'
        smtp_port = 587
    else:
        messagebox.showerror("Error", "Please select a valid email provider.")
        return

    # Initialize the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    try:
        server.login(email_address, email_password)
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Authentication failed. Check your credentials.")
        return

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            msg = MIMEMultipart()
            msg['From'] = email_address
            msg['To'] = row['Email']
            msg['Subject'] = subject_entry.get()

            msg.attach(MIMEText(body_text.get("1.0", "end-1c"), 'plain'))

            for attachment_path in attachment_file_paths:  # Iterate over each selected attachment
                with open(attachment_path, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), Name=attachment_path.split('/')[-1])
                part['Content-Disposition'] = f'attachment; filename="{attachment_path.split("/")[-1]}"'
                msg.attach(part)

            server.send_message(msg)

    server.quit()
    messagebox.showinfo("Success", "Emails have been sent successfully.")


# Initialize Tkinter root
root = tk.Tk()
root.title("Email Sender")

csv_file_path = ""
attachment_file_path = ""

# Email Provider Selection
provider_label = Label(root, text="Select your email provider:")
provider_label.pack()
provider_var = tk.StringVar()
provider_dropdown = ttk.Combobox(root, textvariable=provider_var, state="readonly")
provider_dropdown['values'] = ('Gmail', 'Outlook', 'Yahoo', 'Web.de', 'Gmx')
provider_dropdown.pack()


# Email and Password Entry
email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

# CSV Selection
csv_button = Button(root, text="Select CSV File", command=select_csv)
csv_button.pack()
csv_label = Label(root, text="No CSV file selected")
csv_label.pack()

# Subject
subject_label = Label(root, text="Subject:")
subject_label.pack()
subject_entry = Entry(root)
subject_entry.pack()

# Body
body_label = Label(root, text="Body:")
body_label.pack()
body_frame = Frame(root)
body_frame.pack(fill="both", expand=True)
body_text = Text(body_frame, wrap="word", height=10)
body_scrollbar = Scrollbar(body_frame, command=body_text.yview)
body_text.configure(yscrollcommand=body_scrollbar.set)
body_text.pack(side="left", fill="both", expand=True)
body_scrollbar.pack(side="right", fill="y")

# Attachment
attachment_button = Button(root, text="Select Attachment", command=select_attachment)
attachment_button.pack()
attachment_label = Label(root, text="No file attached")
attachment_label.pack()

# Send Button
send_button = Button(root, text="Send Emails", command=send_emails)
send_button.pack()

root.mainloop()