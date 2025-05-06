import facebook

# Bước 1: Đọc Access Token
with open('access_token.txt', 'r') as file:
    access_token = file.read().strip()

# Bước 2: Đọc nội dung bài viết
with open('post_content.txt', 'r') as file:
    post_content = file.read().strip()

# Bước 3: Đăng bài lên Facebook
try:
    graph = facebook.GraphAPI(access_token=access_token)
    graph.put_object(parent_object='me', connection_name='feed', message=post_content)
    print("✅ Đã đăng bài thành công lên Facebook!")
except facebook.GraphAPIError as e:
    print(f"❌ Lỗi khi đăng bài: {e}")
