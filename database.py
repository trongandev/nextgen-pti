from data_json import load_json_data, write_json_data

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class UserDatabase:
    def __init__(self):
        self.user_list = list() # khởi tạo danh sách user rỗng
        self.user_dict = load_json_data("user.json") # đọc dữ liệu từ file json
        self.user_title = self.load_title()
        
    def load_title(self):
        return [item["username"] for item in self.user_dict]

    def load_data(self):
        for model_dict in self.user_dict:
            model = User(username = model_dict["username"],
                        password = model_dict["password"])
            self.user_list.append(model)
            
    def save_data(self,new_dict):
        new_data = User(username = new_dict["username"],
                        password = new_dict["password"])
        self.user_list.append(new_data)
        self.user_dict.append(new_dict) # thêm dữ liệu vào danh sách
        write_json_data("user.json",self.user_dict)
    

class Product:
    def __init__(self,id,name,desc,type,price,quantity,image,discount=0,brand=None):
        self.id = id
        self.name = name
        self.desc = desc
        self.type = type
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.brand = brand
        self.image = image
        
    
    # cập nhập, truyền gì vào thì cập nhập cái đó
    def update(self,new_data):
        for k, v in new_data.items():
            if v:
                setattr(self,k ,v)

class GymProductDatabase:
    def __init__(self):
        self.product_list = list() # khởi tạo danh sách product rỗng
        self.product_dict = load_json_data("product.json") # đọc dữ liệu từ file json
        self.product_title = self.load_title()
        
    def load_title(self):
        return [item["name"] for item in self.product_dict]
  
    def load_data(self):
        for model_dict in self.product_dict:
            model = Product(id = model_dict["id"],
                        name = model_dict["name"],
                        desc = model_dict["desc"],
                        type = model_dict["type"],
                        price = model_dict["price"],
                        quantity = model_dict["quantity"],
                        image = model_dict["image"],
                        discount = model_dict["discount"],
                        brand = model_dict["brand"])
            self.product_list.append(model)
    
    def save_data(self,new_dict):
        new_dict["id"] = len(self.product_list)
        new_data = Product(id = new_dict["id"],
                        name = new_dict["name"],
                        desc = new_dict["desc"],
                        type = new_dict["type"],
                        price = new_dict["price"],
                        quantity = new_dict["quantity"],
                        image = new_dict["image"],
                        discount = new_dict["discount"],
                        brand = new_dict["brand"])
        self.product_list.append(new_data)
        self.product_dict.append(new_dict) # thêm dữ liệu vào danh sách
        write_json_data("product.json",self.product_dict)
    
    def delete_item(self, delete_title):
        obj_delete = self.get_item_by_title(delete_title) # tìm ra thằng anime bằng cách truyền title vào
        self.product_list.remove(obj_delete) # sử dụng hàm mà list hỗ trợ (remove) để xóa
        self.product_dict = self.item_to_data()
        write_json_data("product.json",self.product_dict)
        
    # tìm kiếm item theo tên
    def get_item_by_title(self, obj_name) -> Product:
        for item in self.product_list:
            if item.name == obj_name:
                return item
    
    # từ item tìm được hoặc cập nhật sẽ biến về lại thành dạng dict để có thể lưu xuống file json
    def item_to_data(self):
        json_data = list()
        for anime in self.product_list:
            json_data.append(anime.__dict__)
        return json_data 
    
    # chuyển đổi danh sách product thành dict để lưu vào file json        
    def edit_item_from_dict(self, edit_title, product_dict: Product):
        obj_edit = self.get_item_by_title(edit_title)
        obj_edit.update(product_dict)
        self.product_dict = self.item_to_data()
        write_json_data("product.json",self.product_dict)