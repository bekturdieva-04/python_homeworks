'''Homework 2. Simple Blog System

Define Post Class:
Create a Post class with attributes like title, content, and author.
Define Blog Class:
Create a Blog class that manages a list of posts.
Include methods to add a post, list all posts, and display posts by a specific author.
Create Main Program:
Develop a CLI to interact with the Blog system.
Include options to add posts, list all posts, and display posts by a specific author.
Enhance Blog System:
Add functionality to delete a post, edit a post, and display the latest posts.
Test the Application:
Create instances of posts and test the functionality of your Blog system.'''

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully!")
    
    def list_posts(self):
        return "\n".join(str(post) for post in self.posts) if self.posts else "No posts available."
    
    def posts_by_author(self, author):
        filtered_posts = [post for post in self.posts if post.author == author]
        return "\n".join(str(post) for post in filtered_posts) if filtered_posts else "No posts by this author."
    
    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                return "Post deleted successfully!"
        return "Post not found."
    
    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                return "Post updated successfully!"
        return "Post not found."
    
    def latest_posts(self, count=3):
        return "\n".join(str(post) for post in self.posts[-count:]) if self.posts else "No posts available."

def main():
    blog = Blog()
    
    while True:
        print("\nSimple Blog System")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
        
        elif choice == "2":
            print("\nAll Posts:")
            print(blog.list_posts())
        
        elif choice == "3":
            author = input("Enter author name: ")
            print(blog.posts_by_author(author))
        
        elif choice == "4":
            title = input("Enter post title to delete: ")
            print(blog.delete_post(title))
        
        elif choice == "5":
            title = input("Enter post title to edit: ")
            new_content = input("Enter new content: ")
            print(blog.edit_post(title, new_content))
        
        elif choice == "6":
            print("\nLatest Posts:")
            print(blog.latest_posts())
        
        elif choice == "7":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
