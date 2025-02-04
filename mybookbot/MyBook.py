from pyrogram import Client, filters
import fitz  
from PIL import Image
import os

API_ID = 111234555 
API_HASH = "dssdfghjjjjkoooofda8fd606d2c"  
BOT_TOKEN = "mjnhbgvvvfvrd9dDw1eRVa3I4YD-Zx7yB7ev9waA"  

app = Client("my_admin_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
def take_photo(my_pdf, my_image="cover.jpg"):
    book = fitz.open(my_pdf)  
    first_page = book[0] 
    change_to_photo = first_page.get_pixmap()  
    img = Image.frombytes("RGB", [change_to_photo.width, change_to_photo.height], change_to_photo.samples)
    img.save(my_image, "JPEG")  
    return my_image
@app.on_message(filters.document)
async def pdf_handler(client, message): 
    if message.document.mime_type == "application/pdf":  
        my_pdf = await message.download() 
        my_image = take_photo(my_pdf)  
        if my_image:
            photo_msg = await message.reply_photo(my_image)
            sent_pdf = await photo_msg.reply_document(my_pdf)
    else:
        await message.reply_text("Only pdf files are supported")
print("The bot is running")
app.run()