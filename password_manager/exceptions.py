# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        pass
# Moved outside the loop to print total_likes only once after processing all posts
print(total_likes)
