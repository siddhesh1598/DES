import KeyGen
import binascii

# Initial Permutation
def InitPerm(M):

	M = [0] + M

	# matrix for initial permutation
	IP = [58 ,   50,   42,    34,    26,   18,    10,    2,
        60,    52,   44,    36,    28,   20,    12,    4,
        62,    54,   46,    38,    30,   22,    14,    6,
        64,    56,   48,    40,    32,   24,    16,    8,
        57,    49,   41,    33,    25,   17,     9,    1,
        59,    51,   43,    35,    27,   19,    11,    3,
        61,    53,   45,    37,    29,   21,    13,    5,
        63,    55,   47,    39,    31,   23,    15,    7]

	M_IP = []

	for i in IP:
		M_IP.append(M[i])

	return M_IP


# Final Permutation
def FinPerm(M):

	M = [0] + M

	# matrix for final permutation
	FP = [40,     8,   48,    16,    56,   24,    64,   32,
	        39,     7,   47,    15,    55,   23,    63,   31,
	        38,     6,   46,    14,    54,   22,    62,   30,
	        37,     5,   45,    13,    53,   21,    61,   29,
	        36,     4,   44,    12,    52,   20,    60,   28,
	        35,     3,   43,    11,    51,   19,    59,   27,
	        34,     2,   42,    10,    50,   18,    58,   26,
	        33,     1,   41,     9,    49,   17,    57,   25]

	M_FP = []

	for i in FP:
		M_FP.append(M[i])

	return M_FP


# expand 32-bit Right Plain Text into 48-bit
def MessageExpansion(M):

	M = [0] + M

	# expansion matrix
	E = [32,     1,    2,     3,     4,    5,
          4,     5,    6,     7,     8,    9,
          8,     9,   10,    11,    12,   13,
         12,    13,   14,    15,    16,   17,
         16,    17,   18,    19,    20,   21,
         20,    21,   22,    23,    24,   25,
         24,    25,   26,    27,    28,   29,
         28,    29,   30,    31,    32,    1]

	l = []

	for i in E:
		l.append(M[i])

	return l


# bitwise XOR of message and key
def BitwiseXOR(M, K):

	l = []

	for k in range(len(M)):

		if M[k] == int(K[k]):
			l.append(0)
		else:
			l.append(1)

	return l


# S-box substitution
def SBox(M):

	S = [
			[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
			[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
			[4, 1, 14, 8, 13,  6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
			[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
		]

	l = []

	j = 0
	for i in range(8):

		row = 0
		col = 0

		# a,f -> row
		# b,c,d,e -> col
		a = M[j]
		b = M[j+1]
		c = M[j+2]
		d = M[j+3]
		e = M[j+4]
		f = M[j+5]

		if a == 0 and f == 0:
			row = 0
		elif a == 0 and f == 1:
			row = 1
		elif a == 1 and f == 0:
			row = 2
		elif a == 1 and f == 1:
			row = 3

		if b == 0 and c == 0 and d == 0 and f == 0:
			col = 0
		elif b == 0 and c == 0 and d == 0 and f == 1:
			col = 1
		elif b == 0 and c == 0 and d == 1 and f == 0:
			col = 2
		elif b == 0 and c == 0 and d == 1 and f == 1:
			col = 3
		elif b == 0 and c == 1 and d == 0 and f == 0:
			col = 4
		elif b == 0 and c == 1 and d == 0 and f == 1:
			col = 5
		elif b == 0 and c == 1 and d == 1 and f == 0:
			col = 6
		elif b == 0 and c == 1 and d == 1 and f == 1:
			col = 7
		elif b == 1 and c == 0 and d == 0 and f == 0:
			col = 8
		elif b == 1 and c == 0 and d == 0 and f == 1:
			col = 9
		elif b == 1 and c == 0 and d == 1 and f == 0:
			col = 10
		elif b == 1 and c == 0 and d == 1 and f == 1:
			col = 11
		elif b == 1 and c == 1 and d == 0 and f == 0:
			col = 12
		elif b == 1 and c == 1 and d == 0 and f == 1:
			col = 13
		elif b == 1 and c == 1 and d == 1 and f == 0:
			col = 14
		elif b == 1 and c == 1 and d == 1 and f == 1:
			col = 15

		#  bit substitution and conversion to binary till 4 bits
		s = S[row][col]
		s = bin(s)[2:].zfill(4)

		l.append(s)

		j+=6

	# converting 4-bit elemens into a single string and then mapping them to single bit elements
	str = "".join(l)
	l = []
	for i in range(len(str)):
		l.append(str[i])

	return l

# P-Box substitution
def PBox(M):

	M = [0] + M

	P = [16,   7,  20,  21,
         29,  12,  28,  17,
          1,  15,  23,  26,
          5,  18,  31,  10,
          2,   8,  24,  14,
         32,  27,   3,   9,
         19,  13,  30,   6,
         22,  11,   4,  25]

	l = []	

	for i in P:
		l.append(M[i])

	return l

# XOR of lpt and rpt
def XOR(lpt, rpt):

	l = []

	for k in range(len(lpt)):
		if lpt[k] == rpt[k]:
			l.append(0)
		else:
			l.append(1)

	return l

def DESFunction(lpt, rpt, key):

	temp = rpt

	# message expansion
	rpt = MessageExpansion(rpt)
	

	# XOR with key
	rpt = BitwiseXOR(rpt, key)


	# SBox substitution
	rpt = SBox(rpt)


	# PBOx permutation
	rpt = PBox(rpt)

	# XOR with lpt
	rpt = BitwiseXOR(lpt, rpt)

	lpt = temp

	return (lpt, rpt)


def Rounds(L0, R0, K):

	lpt = L0
	rpt = R0

	for i in range(16):

		lpt, rpt = DESFunction(lpt, rpt, K[i])
	
	return (lpt, rpt)

def main():

	# getting message as input and converting it into list
	M = input("Enter 64-bit message: \n")
	
	l = []

	for i in range(len(M)):
		l.append(bin(ord(M[i]))[2:].zfill(8))

	s = ''.join(l)

	l = []
	for i in range(len(s)):
		l.append(s[i])

	message = l


	# getting key as input and converting it into list
	K = input("Enter 64-bit key: \n")
	l = []

	for i in range(len(M)):
		l.append(bin(ord(M[i]))[2:].zfill(8))

	s = ''.join(l)

	l = []
	for i in range(len(s)):
		l.append(s[i])

	K = l

	key = KeyGen.Key()

	# converting 64-bit key to 56-bit
	K = key.subKey(K)

	# generating 16 keys
	K = key.SixteenKeyGen(K)


	message = InitPerm(message)

	L0 = message[:32]
	R0 = message[32:]	

	lpt, rpt = Rounds(L0, R0, K)

	message = lpt + rpt

	message = FinPerm(message)

	for i in range(len(message)):
		message[i] = str(message[i])

	msg = ''.join(message)

	print("Original Message: \n{} \nEncrypted Message: \n{}".format(M, msg))

if __name__ == '__main__':
	main()