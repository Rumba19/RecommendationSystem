class UserPreferences:
    def __init__(self):
        self.user_profile_list = {} #Hash table to store user profile and preferences

    def add_preferences(self, user, item, rating):
        if user not in self.user_profile_list:
            self.user_profile_list[user] = {}
        self.user_profile_list[user][item] = rating

    def get_preferences(self, user):
        return self.user_profile_list.get(user, {})

# Example to create item and ratings
user_preferences = UserPreferences()
user_preferences.add_preferences("user1", "item1", 5)
user_preferences.add_preferences("user1", "item2", 7)
print(user_preferences.get_preferences("user1")) 
