# custom_base62
A python object for using the base62 number system, allowing for custom character orders 

# usage

```python3
# import object
from custom62 import CustomBase62

# generate a new unique base62 signature
sig = CustomBase62.sig_gen()

# output : 'Fsj50wIB91VkEAlrzH6PxybX2c73tSThZnGCqKmJfNUgpYQvLMauRdeWDoi48O'

# Retrieve standard base62 characters
CustomBase62.base62_std()

# output : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# create new CustomBase62 object and initiate with our signature
cb = CustomBase62(sig)

# encode an int from our unique signature
cb.encode(200)

# output : '5l'

# decode an int from our unique signature
cb.decode('5l')

# output : 200

# retreive signature from current object
cb.cur_sig()

# output : 'Fsj50wIB91VkEAlrzH6PxybX2c73tSThZnGCqKmJfNUgpYQvLMauRdeWDoi48O'
```

# known limitations
With very large ints ( > 1,000,000,000,000,000,000), float will run into issues and some tweaking of the object may be required. You can use float128 from nmpy, however it is probably unlikely that such numbers will be acheived
