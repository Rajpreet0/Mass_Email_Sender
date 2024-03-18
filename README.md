# Email Sender Application

This is a simple Python application built with Tkinter that allows users to send emails to multiple recipients using a CSV file as a source for email addresses. Users can also attach files to their emails.

## Features

- Select your email provider from a dropdown list.
- Enter your email address and password.
- Select a CSV file containing the list of recipient email addresses.
- Enter the subject and body of the email.
- Attach files to the email.
- Send emails to all recipients listed in the CSV file.

## Requirements

- Python 3.12.2
- Tkinter (usually included with Python installation)
- Libraries:
  - `smtplib`: For sending emails using the SMTP protocol.
  - `email.mime`: For creating email messages with attachments.
  - `csv`: For reading CSV files.
  - `tkinter`: For building the graphical user interface.
  - `tkinter.filedialog`: For opening file dialogs.
  - `tkinter.messagebox`: For displaying message boxes.
  - `tkinter.ttk`: For themed Tkinter widgets.

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the files.
3. Run the script `email_sender.py`.
4. Fill in the required fields:
   - Select your email provider.
   - Enter your email address and password.
   - Select a CSV file containing recipient email addresses.
   - Enter the subject and body of the email.
   - Optionally, attach files to the email.
5. Click the "Send Emails" button to send the emails.

## Notes

- Ensure that you have allowed access to less secure apps in your email account settings if you encounter authentication issues.
- The application currently supports Gmail, Outlook, Yahoo, Web.de, and Gmx email providers.
- For security reasons, it's recommended to use an app-specific password for email authentication instead of your main account password.

## Contributors

- [Rajpreet Singh](https://github.com/Rajpreet0)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
