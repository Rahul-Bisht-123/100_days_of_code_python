PLACE_HOLDER = "[name]"

with open(file="./input/names/invited_names.txt") as names:
  names_list = names.readlines()

with open(file="./input/letter/starting_letter.docx") as letter_file:
  letter_contents = letter_file.read()
  for name in names_list:
    new_letter = letter_contents.replace(PLACE_HOLDER , name.strip())
    # print(new_letter)
    with open(file=f"./output/ready_to_send/letter_for_{name.strip()}.docx", mode="w") as new_file:
      new_file.write(new_letter)