from django.shortcuts import render

# Create your views here.

import qrcode
import base64
from io import BytesIO


def qr_code_view(request):

    data = "https://github.com/Nazirov-02"


    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)


    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)


    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'qrcode/qrcode.html', {'qrcode_img': f"data:image/png;base64,{img_base64}"})
