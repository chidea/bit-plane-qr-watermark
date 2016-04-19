# bit-plane-qr-watermark
Insert/extract invisible watermark on 1bit plane of images, powered by PILlow.
This is also be called as LSB steganography.

### Required libraries
  - PILlow
  - qrcode

#### How to get required libraries
`pip install pillow qrcode`

### How to use
  - Insert
    - `python embed.py hello_world image.jpg`
    - `image_watermark.jpg` which contains invisible watermark will be created.
  - Extract
    - `python extract.py image_watermark.jpg`
    - `image_watermark_1bit.jpg` which has original QR code will be created.

#### Note
  - Saving to JPG/JPEG file will loose its LSB.
