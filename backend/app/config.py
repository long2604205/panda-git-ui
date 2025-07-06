import os

class Config:
    # Chế độ debug
    DEBUG = True

    # Thư mục workspace nơi các repo sẽ được clone về
    WORKSPACE_PATH = os.path.expanduser("~/git-workspace")

    # Cho phép clone repo công khai (https), hoặc ssh nếu sau này cần
    ALLOWED_PROTOCOLS = ['https', 'git', 'ssh']

    # Số commit tối đa sẽ trả về (ví dụ limit khi load git graph)
    MAX_COMMITS = 500

    # Danh sách nhánh mặc định ưu tiên nếu không có main/master
    DEFAULT_BRANCHES = ['main', 'master', 'dev']

    # Encoding mặc định cho commit message (nếu cần xử lý)
    DEFAULT_ENCODING = 'utf-8'


# Hàm để load config vào Flask app nếu cần
def init_app(app, config_class=Config):
    app.config.from_object(config_class)
