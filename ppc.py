from itertools import combinations 
s = []
d = []
print "Enter a few space separated strings"
s = raw_input().split()
d =list(combinations(s,3))
for i in d:
	p = ''
	for j in i:
		p+=j
	if p == p[::-1]:
		print "This combination is a palindrome."
		print i  
