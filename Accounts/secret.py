
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import secrets
import string


def secert_code_genarator():
    alphabet = string.ascii_letters + string.digits
    secert_code = ''.join(secrets.choice(alphabet) for i in range(10))
    return secert_code


def encode_int_urlsafe(my_integer):
    encoded_bytes = my_integer.to_bytes((my_integer.bit_length() + 7) // 8, byteorder='big')

    # Encode the bytes using urlsafe_base64_encode
    encoded_urlsafe = urlsafe_base64_encode(encoded_bytes)
    return encoded_urlsafe


def decode_int_urlsafe(encoded_urlsafe):
    decoded_bytes = urlsafe_base64_decode(encoded_urlsafe)

    # Convert the bytes back to an integer
    decoded_integer = int.from_bytes(decoded_bytes, byteorder='big')

    return decoded_integer
