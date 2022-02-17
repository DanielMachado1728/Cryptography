#Affine Cipher

def gcd(p, q):
  while(q != 0):
    remainder = p % q
    p = q
    q = remainder
  return int(p)

def affinecipher(plaintext, a, b):
  alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 
              'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 
              'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 
              's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23,
              'y':24, 'z':25, 'complete_alphabet': 'abcdefghijklmnopqrstuvwxyz'}

  ciphertext = ''
  for p in plaintext:
    try:
      number = alphabet[p]
      ciphertext += alphabet['complete_alphabet'][((number*a)+b)%26]
    except:
      continue
  return print(ciphertext)


plaintext = input('Plaintext: ').lower().replace(' ', '')

while 1:
  key_a = int(input('Key a: '))
  if gcd(key_a, 26) != 1:
    print('The variable "Key a" needs that the Greatest Common Divisor between it and 26 to be equal to 1.')
  else:
    break
key_b = int(input('Key b: '))
affinecipher(plaintext, key_a, key_b)
