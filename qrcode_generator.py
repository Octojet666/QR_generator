import qrcode

# Get input from user
text = input("Enter text or URL to convert to QR code: ")

# Generate QR code
qr = qrcode.make(text)

# Save the QR code
filename = input("Enter filename to save (default: qrcode.png): ") or "qrcode.png"
qr.save(filename)

print(f"QR code saved as {filename}")
