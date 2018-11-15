from des import core


message = "FEDCBA0123456017"
key = "133457799BBCDFE9"
print "Message : {}".format(message)
print "Key : {}".format(key)
print "Encrypted message: {}".format(core.encrypt(message , key))
