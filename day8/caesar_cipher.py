def caesar(start_text, shift_num ,mode):
  start_text_list = [char for char in start_text]

  end_text = ""
  if(mode == "decrypt"):
      shift_num *= -1
  for letter in start_text_list:
    if letter.isalpha():
      letter_ascii_value = ord(letter)
      shifted_letter_ascii_value = ord("a") + (letter_ascii_value - ord("a") + shift_num) % 26
      shifted_letter = chr(shifted_letter_ascii_value)
      letter = shifted_letter
    
    end_text += letter
  print(f"{mode}ed text = {end_text} \n")

print("****** Welcome to the  Caesar cipher ****** \n")
while True:
  
  print("------------------------------------------------------")
  choice = input("Type 'encrypt' or 'decrypt' or 'exit' : ")
  print("------------------------------------------------------")
  if(choice == "exit"):
    break

  elif(choice == "encrypt"):
    plain_message = input("Enter Your Plain message : ")
    shift = int(input("Enter the shift : "))
    caesar(plain_message , shift , choice)

  elif(choice == "decrypt"):
    cipher_message = input("Enter Your cipher message : ")
    shift = int(input("Enter the shift : "))
    caesar(cipher_message , shift , choice)

  else:
    print("Wrong input")