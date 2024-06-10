Insta_Posts = [
  {"likes" : 20 , "comments" : 2 , "shares" : 1},
  {"likes" : 20 , "comments" : 2 , "shares" : 1},
  {"likes" : 20 , "comments" : 2 , "shares" : 1},
  {"comments" : 2 , "shares" : 1},
  {"comments" : 2 , "shares" : 1},
]

total_likes_count = 0

for post in Insta_Posts:
  try:
    total_likes_count += post["likes"]
  except KeyError:
    pass

print(total_likes_count)
#60