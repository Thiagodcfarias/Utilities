from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
from string import Template
from email.mime.text import MIMEText

MY_ADDRESS = 'email'
PASSWORD = 'senha'

def get_contacts(template):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(template, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            data = a_contact.split(',')
            names.append(data[0])
            emails.append(data[1])
    return names, emails

def read_template(template):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(template, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('path/emails.csv') # read contacts 
    print(names, emails)
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=25)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        
        html = """
                <html>
                </html>
                """
        partHtml = MIMEText(html, 'html')
        msg = MIMEMultipart()       # create a message
        

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']= "email's title"
        
        # add in the message body
        msg.attach(partHtml)
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
    
if __name__ == '__main__':
    main()