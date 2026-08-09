from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

if __name__ == "__main__":
    raw_pass = "MySecretPassword123!"

    hashed = hash_password(raw_pass)
    print("Stored Hash in DB:", hashed)

    is_valid = verify_password("MySecretPassword123!", hashed)
    print("Valid Password Test:", is_valid)

    is_invalid = verify_password("WrongPassword!", hashed)
    print("Wrong Password Test:", is_invalid)






