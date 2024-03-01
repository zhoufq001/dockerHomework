#
#https://github.com/mmulqueen/pyStrich/tree/master/pystrich/datamatrix
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('this is a data matrix')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())
