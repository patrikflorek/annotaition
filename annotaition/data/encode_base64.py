import base64

with open("/home/pato/Code/patrikflorek/annotaitor/annotaitor/data/seedling.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

with open('/home/pato/Code/patrikflorek/annotaitor/annotaitor/data/seedling_base64.txt', "w") as f:
    f.write(encoded_string.decode('utf-8'))
