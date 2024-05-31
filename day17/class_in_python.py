class Profile:

  def __init__(self, user_id , user_name , user_email) -> None:
    self.user_id = user_id
    self.user_name = user_name
    self.user_email = user_email
    self.follower = 0
    self.following = 0
  
  def follow(self , user):
    user.follower += 1
    self.following += 1



obj1 = Profile(1 , "Aman" , "aman@gamil.com")
obj2 = Profile(2 , "Bob" , "bob@gamil.com")
    

print(obj1.user_id , obj1.user_name , obj1.user_email)
# 1 Aman aman@gamil.com

print(obj2.user_id , obj2.user_name , obj2.user_email)
# 2 Bob bob@gamil.com

obj1.follow(obj2)

print('---------------------------------')
print(obj1.follower)  #0
print(obj1.following) #1
print('---------------------------------')
print(obj2.follower)  #1
print(obj2.following) #0
print('---------------------------------')