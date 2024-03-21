from qrcodes.generator import generate_qr_code

def generate_ticket_qr_code(ticket_id):
    qr_code_value = f"ticket_{ticket_id}"
    qr_code_image = generate_qr_code(qr_code_value)
    # Store the QR code image or value in the database
    return qr_code_image