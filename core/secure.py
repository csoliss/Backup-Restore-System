# -*- coding: utf-8 -*-
import sys
import hashlib


class HashFile():

    def __init__(self, verbose=False):
        self.verbose = verbose

    def hashForFile(self, filename):
        """This function returns the SHA-512 hash of the file passed into it"""
        # make a hash object
        if self.verbose:
            print(('Creating hash (sha-512) for %s' % (filename)))
        h = hashlib.sha512()
        # open file for reading in binary mode
        with open(filename, 'rb') as _file:
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = _file.read(1024)
                h.update(chunk)
        # return the hex representation of digest
        return h.hexdigest()

    def hashFiles(self, filename, filehash='hash.txt'):
        """This function create a file with a list of filename and hash's"""
        # Creating the hash for the file
        _hash = self.hashForFile(filename)
        if self.verbose:
            print(('Appending the hash for "%s" in "%s"' %
                    (filename, filehash)))
        # append the line in the file
        with open(filehash, 'a') as _file:
            # writing the file
            _file.write('%s \t %s\n' % (filename, _hash))


if __name__ == '__main__':
    try:
        #print(sys.argv[1])
        hf = HashFile(True)
        hf.hashFiles(sys.argv[1])
    except KeyboardInterrupt:
        print('\nExit by the user by pressing "Ctrl + c"...\n')
        #core.del_file(lock_file)