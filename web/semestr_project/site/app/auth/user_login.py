from base.models import User


class UserLogin:
    def from_db(self, name, password):
        self.__user = User.query.filter_by(id=user_id).first()
        return self


    def create(self, user):
        self.__user = user
        return self


    def is_authenticated(self):
        return True

    
    def is_active(self):
        return True

    
    def is_anonymous(self):
        return False

    
    def get_id(self):
        return str(self.__user.id)