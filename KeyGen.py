class Key:

	# creating subkey of 56-bit long
	def subKey(self, K):

		K = [0] + K

		# permutation matrix for KeyGen
		PC_1 = [ 57,  49,    41,   33,    25,    17,    9,
	           1,   58,    50,   42,    34,    26,   18,
	          10,    2,    59,   51,    43,    35,   27,
	          19,   11,     3,   60,    52,    44,   36,
	          63,   55,    47,   39,    31,    23,   15,
	           7,   62,    54,   46,    38,    30,   22,
	          14,    6,    61,   53,    45,    37,   29,
	          21,   13,     5,   28,    20,    12,    4]

		K_56 = []

		for i in PC_1:
			K_56.append(K[i])

		return K_56

	# generating keys for 16 rounds
	def SixteenKeyGen(self, K):

		# rotating list by n bits
		def rotate(l, n):
			return l[n:] + l[:n]

		# divide the key into left-half and right-half
		C0 = K[:28]
		D0 = K[28:]
		K0 = [0] + C0 + D0

		C1 = rotate(C0, 1)
		D1 = rotate(D0, 1)
		K1 = [0] + C1 + D1

		C2 = rotate(C1, 1)
		D2 = rotate(D1, 1)
		K2 = [0] + C2 + D2

		C3 = rotate(C2, 2)
		D3 = rotate(D2, 2)
		K3 = [0] + C3 + D3

		C4 = rotate(C3, 2)
		D4 = rotate(D3, 2)
		K4 = [0] + C4 + D4

		C5 = rotate(C4, 2)
		D5 = rotate(D4, 2)
		K5 = [0] + C5 + D5

		C6 = rotate(C5, 2)
		D6 = rotate(D5, 2)
		K6 = [0] + C6 + D6

		C7 = rotate(C6, 2)
		D7 = rotate(D6, 2)
		K7 = [0] + C7 + D7

		C8 = rotate(C7, 2)
		D8 = rotate(D7, 2)
		K8 = [0] + C8 + D8

		C9 = rotate(C8, 1)
		D9 = rotate(D8, 1)
		K9 = [0] + C9 + D9

		C10 = rotate(C9, 2)
		D10 = rotate(D9, 2)
		K10 = [0] + C10 + D10

		C11 = rotate(C10, 2)
		D11 = rotate(D10, 2)
		K11 = [0] + C11 + D11

		C12 = rotate(C11, 2)
		D12 = rotate(D11, 2)
		K12 = [0] + C12 + D12

		C13 = rotate(C12, 2)
		D13 = rotate(D12, 2)
		K13 = [0] + C13 + D13

		C14 = rotate(C13, 2)
		D14 = rotate(D13, 2)
		K14 = [0] + C14 + D14

		C15 = rotate(C14, 2)
		D15 = rotate(D14, 2)
		K15 = [0] + C15 + D15

		C16 = rotate(C15, 1)
		D16 = rotate(D15, 1)
		K16 = [0] + C16 + D16

		def KeyConv48Bit(K):

			# permutation matrix for 16 keys to convert them into 48-bit keys
			PC_2 = [14,    17,   11,    24,     1,    5,
		              3,    28,   15,     6,    21,   10,
		             23,    19,   12,     4,    26,    8,
		             16,     7,   27,    20,    13,    2,
		             41,    52,   31,    37,    47,   55,
		             30,    40,   51,    45,    33,   48,
		             44,    49,   39,    56,    34,   53,
		             46,    42,   50,   36,    29,   32]

			l = []

			for i in PC_2:
				l.append(K[i])

			return l

		K1 = KeyConv48Bit(K1)
		K2 = KeyConv48Bit(K2)
		K3 = KeyConv48Bit(K3)
		K4 = KeyConv48Bit(K4)
		K5 = KeyConv48Bit(K5)
		K6 = KeyConv48Bit(K6)
		K7 = KeyConv48Bit(K7)
		K8 = KeyConv48Bit(K8)
		K9 = KeyConv48Bit(K9)
		K10 = KeyConv48Bit(K10)
		K11 = KeyConv48Bit(K11)
		K12 = KeyConv48Bit(K12)
		K13 = KeyConv48Bit(K13)
		K14 = KeyConv48Bit(K14)
		K15 = KeyConv48Bit(K15)
		K16 = KeyConv48Bit(K16)

		keys_48 = [K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, K13, K14, K15, K16]

		return keys_48
