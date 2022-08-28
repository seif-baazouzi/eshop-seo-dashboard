import bcrypt

def hash(password):
  return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify(password, hash):
  hashBytes = hash.encode("utf-8")
  passwordBytes = password.encode("utf-8")

  return bcrypt.checkpw(passwordBytes, hashBytes)
