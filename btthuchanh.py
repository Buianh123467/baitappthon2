import facebook

# Đọc token từ file
with open('facebook_token.txt', 'r') as f:
    access_token = f.read().strip()

# Đọc nội dung bài đăng từ file
with open('post_content.txt', 'r', encoding='utf-8') as f:
    message = f.read()

# Tạo đối tượng Graph API
graph = facebook.GraphAPI(access_token)

# Đăng bài lên Trang
graph.put_object(parent_object='me', connection_name='feed', message=message)
