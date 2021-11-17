class hamming:
    def distance(self, str1, str2):
        if len(str1)>len(str2):
            raise ValueError("pierwszy str jest dłuższy")
        elif len(str1)<len(str2):
            raise ValueError("drugi str jest dłuższy")
        elif str1=="" and str2=="":
            return 0

        elif len(str1)==1 and len(str2)==1:
            if str1==str2:
                return 0
            else:
                return 1

        else:
            suma=0
            for i in range(len(str1)):
                if str1[i]!=str2[i]:
                    suma+=1
            return suma