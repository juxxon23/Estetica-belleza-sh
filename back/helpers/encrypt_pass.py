import bcrypt

class EncrypyPass():
    
    def do(self, password):
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return hash_password