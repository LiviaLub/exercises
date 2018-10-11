def is_power2(num):



	return num != 0 and ((num & (num - 1)) == 0)

print(is_power2(4))
print(is_power2(3))
print(is_power2(8))
