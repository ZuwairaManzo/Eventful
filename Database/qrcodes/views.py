from flask import jsonify, request

from . import qrcodes_blueprint
from .models import db, QRCode
from .generator import generate_qr_code

@qrcodes_blueprint.route('/generate', methods=['POST'])
def generate_qrcode():
    data = request.get_json()
    ticket_id = data.get('ticket_id')

    # Implement QR code generation logic
    qr_code_value = f"ticket_{ticket_id}"
    qr_code_image = generate_qr_code(qr_code_value)

    # Store the QR code in the database
    qrcode_record = QRCode(code=qr_code_value, ticket_id=ticket_id)
    db.session.add(qrcode_record)
    db.session.commit()

    return jsonify({'qrcode': qr_code_image})