#Atbash Cipher
 
def atbash_cipher(plaintext):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  atbash_alphabet = [0]*26
  start, end = 0, 25
  while start != end and end>start:
    atbash_alphabet[start] = alphabet[end]
    atbash_alphabet[end] = alphabet[start]
    start += 1
    end -= 1
  ciphertext = ''
  for i in plaintext:
    if i in alphabet:
      position = alphabet.index(i)
      ciphertext += atbash_alphabet[position]
    else:
      ciphertext += i
  return print('Ciphertext: ',ciphertext)

plaintext = input('Plaintext: ').lower()
atbash_cipher(plaintext)
