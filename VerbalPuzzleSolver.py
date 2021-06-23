#К О Р О В А		5	4	0	4	9	8
#  Т Р А В А			6	0	8	9	8
#Д О Я Р К А		1	4	2	0	5	8
#- - - - - -
#М О Л О К О		7	4	3	4	5	4

for K in range(0,9):
	for O in range(0,9):
		for T in range(0,9):
			for B in range(0,9):
				for A in range(0,9):
					for P in range(0,9):
						for L in range(0,9):
							for M in range(0,9):
								for J in range(0,9):
									for D in range(0,9):
										z1 = A + 10*B+100*O+1000*P+10000*O+100000*K
										z2 = A + 10*B+100*A+1000*P+10000*T
										z3 = A + 10*K+100*P+1000*J+10000*O+100000*D

										result = O + 10*K + 100*O + 1000*L+10000*O+100000*M

										if ((z1+z2+z3)==result and len({K,O,P,B,A,T,D,J,M,L})==10):
											print("SUCCESS")
											print("K=",K)
											print("O=",O)
											print("P=",P)
											print("B=",B)
											print("A=",A)
											print("T=",T)
											print("D=",D)
											print("J=",J)
											print("M=",M)
											print("L=",L)
											exit()