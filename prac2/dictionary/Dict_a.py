
#20CS039 vraj nagarsheth
#  a. Write a Python script to check whether a given key already exists in a dictionary.


#sample dictionary
Cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1800,
}
#key to find if it exists
key = 'brand'
#if key is present in dictionary
if key in Cars:
    print("Present")
else:
    print("Not present")
#key to find if exists
key = 'Company'
if key in Cars:
    print("Exists")
else:
    print("Not present")


