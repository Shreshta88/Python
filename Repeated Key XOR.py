key = 'ICE'
text = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
xor = ''
k = 3
t = len(text)
x = key*(t/k)+key[:t%k]
for i in range(len(text)):
	xor+=chr(ord(text[i])^ord(x[i]))
print xor.encode("hex")
	
