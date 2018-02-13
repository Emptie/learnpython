class Restaurant():
    """模拟餐厅"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化描述餐厅的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """返回餐厅的描述信息"""
        restaurant_description = self.restaurant_name + ' ' + self.cuisine_type
        print(restaurant_description)
    
    def open_restaurant(self):
        """返回餐厅营业状态"""
        print(self.restaurant_name + " is opening!")

    def set_number_served(self,number_served):
        """设置餐厅就餐人数"""
        self.number_served = number_served
        print(str(self.number_served) + " people ate pizza in " + self.restaurant_name)

    def increment_number_served(self,new_number_served):
        """设置新增的就餐人数"""
        self.number_served += new_number_served
        print(str(self.number_served) + " people ate pizza in " + self.restaurant_name)
    
restaurant = Restaurant('Pizza Hut','pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(1000)
restaurant.increment_number_served(100)