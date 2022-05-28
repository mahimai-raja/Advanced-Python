from stegano import lsb

image = '____.jpg'     # file path

output = 'output.jpg'

msg = input('Enter the secret messsage')

lsb.hide(image, message=msg).save(output)



