thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["year"]
print(thisdict)

thisdict.clear()
print(thisdict)