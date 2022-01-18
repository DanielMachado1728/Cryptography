#Caesar Cipher
def caesarcipher(plaintext, key):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  ciphertext = ''
  for i in plaintext:
    try:
      position = alphabet.index(i)
      ciphertext += alphabet[(position+key)%26]
    except:
      ciphertext += i 
  return print('Ciphertext: ',ciphertext)

plaintext = input('Plaintext: ').lower()
key = int(input('Key: ')) 
caesarcipher(plaintext, key)
