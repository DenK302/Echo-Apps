from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from validation.validateFile import validateFile
from image.transformImage import resizeImage
from upload.uploadImage import uploadImage
from starlette.responses import FileResponse 
import boto3
import os
from dotenv import load_dotenv

app=FastAPI()
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
s3_resource = boto3.client('s3', aws_access_key_id=os.environ.get('aws_access_key'), aws_secret_access_key=os.environ.get('aws_secret_access_key'))# open api to work with amazon aws

@app.get("/")
async def Upload_Image_Form():
    return FileResponse('index.html')

@app.post("/")
async def Upload_Image(file: Annotated[UploadFile, File(description="Select image to upload")],):
    if validateFile(file.filename,file.size): #file has extension and it is jpg/jpeg/png and file size < 10 mb
        image = resizeImage(image=await file.read(),target_width=250) #file data and new image width
        link = uploadImage(s3_resource=s3_resource, image=image, bucket="kormuzhanindenis")
        return {"createdlink": link} 
    return {"error": "Invalid file"}