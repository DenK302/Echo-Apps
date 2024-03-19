import random
import string
import io

def uploadImage(s3_resource, image, bucket):
    filename=f"{createFileName()}.jpg"
    s3_resource.upload_fileobj(io.BytesIO(image),bucket, filename, ExtraArgs={'ACL': 'public-read'}) #send file
    return f"https://{bucket}.s3.eu-central-1.amazonaws.com/{filename}"


def createFileName():
    return ''.join(random.choices(string.ascii_letters, k=10)) #random string with 10 letters