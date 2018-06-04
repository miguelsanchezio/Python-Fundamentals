nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]

z = zip(nums1, nums2)
list(z) # [(1,6),(2,7),(3,8),(4,9),(5,10)]

midterms = [80,91,78]
finals = [98, 89, 54]
students = ['dan', 'ang', 'kate']

# final_grades = [max(pair) for pair in zip(midterms, finals)]

# final_grades ={t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}

final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# print(final_grades)