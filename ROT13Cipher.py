#ROT13 Cipher
def rot13(plaintext):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  ciphertext = ''
  for i in plaintext:
    if i in alphabet:
      position = alphabet.index(i)
      ciphertext += alphabet[(position+13)%26]
    else:
      ciphertext += i
  return print('Ciphertext: ',ciphertext)

plaintext = input('Plaintext: ').lower()
rot13(plaintext)
