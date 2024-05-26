phone_book = {
  "Aman" : 998877,
  "Bob" : 12345,
  "Chaman" : 443322,
  "Dany" : 332211
}

print(phone_book)

phone_book["Dany"] = 929292
print(phone_book)

print(phone_book["Aman"])  #998877

for key in phone_book:
  print(f"key = {key} | value = {phone_book[key]}")