import qrcode

upi_id = input("enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CRRENCY&tn=MESSAGE

phonepe_url = f'upi://pay?pa={upi_id}&PN=Recipent%20Name'
paytm_url = f'upi://pay?pa={upi_id}&PN=Recipent%20Name'
google_pay_url = f'upi://pay?pa={upi_id}&PN=Recipent%20Name' 

phone_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(phonepe_url)

phone_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Display the QR codes(you need to install PIL/pillow library)

phone_qr.show()
paytm_qr.show()
google_pay_qr.show()