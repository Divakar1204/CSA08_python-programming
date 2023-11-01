index = int(input("Index: "))
s1 = 'welcome'
s2 = 'Homely'
s3 = s1[:index] + s2 + s1[index:]
s3 = ''.join([c.upper() if c.islower() else c.lower() for c in s3])
vowel_count = sum(1 for c in s3 if c in 'aeiouAEIOU')

print(s3)
print("Vowel count in S3:", vowel_count)
