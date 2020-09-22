# This question is from codechef link: https://www.codechef.com/problems/TSHIRTS#
# A top down approach with memoization


def main():

	# Constraints 0 < Test cases < 10
	testCases = int(input())
	n, v, nPersonSetBit = None, None, None

	# Maximum Tshirts ID can be 100
	# Maximum set of people from 10 people is 2^10
	dp = [[-1 for i in range(101)] for _ in range(1025)]

	def calc(personBitSet, tshirtId):
			
			if personBitSet == nPersonSetBit:
				return 1

			if tshirtId == 101:
				return 0

			ans = 0
			if dp[personBitSet][tshirtId] != -1:
				return dp[personBitSet][tshirtId]

			ans = calc(personBitSet, tshirtId + 1)

			for person in v[tshirtId]:
				if ((personBitSet & (1<<person)) == 0):
					ans += calc(personBitSet | (1<<person), tshirtId + 1)

			ans = ans%1000000007
			dp[personBitSet][tshirtId] = ans
			return ans

	for _ in range(testCases):

		# Constraints 0 < Elephants < 10
		n = int(input())
		v = [list() for _ in range(101)]

		# Used bits for representing the person who have their tshirts
		# Can use other DS but sometimes you can never detach from your mother language C
		nPersonSetBit = (1<<n) - 1

		# For each n person store the list of tshirt IDs in 
		# 2d list
		# Need a reverse map from tshirt IDs to persons
		for i in range(0,n):

			# Constraint tshirts id in range (1,100)
			tshirtsList = list(map(int,input().split()))
			# print(x)
			for tid in tshirtsList:
				v[tid].append(i)


		print(calc(0,1))

main()