from stegano import lsb

image = '___.jpg'     # file path

message = lsb.reveal(image)

print('Hidden message : ',message)