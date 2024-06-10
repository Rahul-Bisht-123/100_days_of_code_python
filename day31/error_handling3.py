Insta_Posts = [
  {"likes" : 20 , "comments" : 2 , "shares" : 1},
  {"likes" : 20 , "comments" : 2 , "shares" : 1},
  {"likes" : 20 , "comments" : 2},
  {"likes" : 20 , "comments" : 2 , "shares" : 10},
  {"likes" : 20 , "comments" : 2 },
]

total_shares_count = 0

for post in Insta_Posts:
  try:
    total_shares_count += post["shares"]
  except KeyError:
    pass

print(total_shares_count)
#12