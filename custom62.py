from random import choice


class CustomBase62:
    """
    Encode and decode int values from a custom base64 signature
    Use [0-9] [a-z] [A-Z] only
    Must only use 1 of each character
    """
    
    def __init__(self, signature):
        """
        Initiate object.
        Takes 1 parameter; signature.
        """
        if signature:
            self._signature = self.test_signature(signature)
        else:
            raise ValueError('62 character signature has not been provided')
        
        self._sig_dict = self._build_dict(self._signature)
        
    
    def cur_sig(self):
        """
        return current signature for object
        """
        return self._signature
    
    
    def encode(self, integer):
        """
        Encode integer to base62 using the current object signature
        """
        
        # test input parameter
        if not type(int()) == type(integer):
            raise ValueError('\'{prov}\' is not an integer')
        
        
        # ns is split of float value from division
        # ns[0] is whole number left of division
        # ns[1] is remainder of division
        ns = str(integer/62).split('.')

        # the whole number of divisions left to calculate (if any) next hex from
        div = int(ns[0])

        # the remainder - calculate current hex value
        integer = round(float('0.' + str(ns[1]))*62)

        # recurse next hex from div (if any)
        if div:
            next = self.encode(div)
        else:
            next = ''

        return next + self._signature[integer]
    
    
    def decode(self, base62_str):
        """
        Decode int value from base62 string.
        """

        # length of string - determine power values
        hex_len = len(base62_str) - 1
        
        # return int value
        rtn_int = 0
        
        # loop through hex string
        for h in base62_str:
            
            # calculate value of hex
            rtn_int += int(self._sig_dict[h] * pow(62, hex_len))
            
            # deduct 1 from length (for pow calculation)
            hex_len -= 1
            
        return  rtn_int
        
            
    @staticmethod
    def _build_dict(signature):
        """
        return dictionary of signature characters.
        Value of each character is the corresponding int value
        """
        
        # define dictionary to return
        rtn_dict = dict()
        
        # loop through signature and append dictionary
        for i in range(62):
            rtn_dict[signature[i]] = i
        
        return rtn_dict
        
    
    @staticmethod
    def test_signature(signature):
        """
        test signature for:
        uniqueness
        correct values
        correct amount of values
        """
        
        # string containing one of each valid characters available
        skel = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # set to validate uniqueness of signauture value
        signature_set = set()
        
        if not len(signature) == 62:
            raise ValueError('Signature is not 62 characters long')
        
        for s in signature:
            
            # add letter to set for verification
            signature_set.add(s)
            
            # check for valid signature character 
            if not s in skel:
                raise ValueError(
                    '\'{a}\' is not a valid signature character'.format(a=s)
                    )
            
        if not len(signature_set) == 62:
            raise ValueError('Signature values are not unique')
        return signature
        
        
    @staticmethod
    def sig_gen():
        """
        Generate a random "signature" from a complete character list
        """
        # standard collection of values
        skel = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        rtn_sig = ''
        
        while bool(skel) == True:
            ch = choice(skel)
            skel = skel.replace(ch, '')
            rtn_sig = rtn_sig + ch
        
        return rtn_sig
    
            
