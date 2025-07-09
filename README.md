# Payment-accept-by-QR
Payment Acceptance System using QR Code in Python, QR code genrated by UPI I'D.

This project is a simple Python application that generates UPI payment QR codes for different payment apps like PhonePe, Paytm, and Google Pay using a single UPI ID. It allows users to input their UPI ID, and the script will generate QR codes compatible with popular UPI apps, making it easier for customers to scan and pay.

The application leverages the qrcode library to create QR codes and Pillow to display them. These QR codes can be printed or displayed digitally for seamless payment acceptance.

Key Features:
Takes user’s UPI ID as input.

Automatically creates UPI payment URLs for PhonePe, Paytm, and Google Pay.

Generates and saves individual QR code images for each payment platform.

Displays the generated QR codes for easy scanning.

No need for internet or external APIs — works entirely offline.

Technologies Used:
Python 3

qrcode – to generate QR codes

Pillow (PIL) – to display QR images

How It Works:
The user enters their UPI ID.

The script formats the UPI payment URL.

QR codes are generated for:

PhonePe

Paytm

Google Pay

The QR codes are saved as PNG files and displayed on screen.

Use Cases:
Street vendors or shopkeepers who want to offer multiple UPI payment options.

Freelancers or small business owners who need quick offline QR code generation.

Educational demonstration of QR code generation and UPI integration.

Limitations & Notes:
The generated QR codes use a basic UPI format and assume compatibility across apps.

Amount, currency, and transaction message are not included but can be added for dynamic QR codes.

For advanced features like payment verification, API integration would be needed.

