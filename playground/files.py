def write_to_file(filename):
    try:
        file1 = open(filename, "w")
        file1.write("Preved ")
        file1.write("Medved")
    except Exception:
        pass
    finally:
        file1.close()


def read_from_file(filename):
    try:
        file1 = open(filename, "r")
        read1 = file1.read(3)
        print(read1)
      #  file1.seek(3)
      #  read2 = file1.read(7)
       # print(read2)
     #   print(file1.tell())
        file1.seek(0, 2)
        print(file1.tell())
    except Exception:
        pass
    finally:
        file1.close()


#write_to_file("text1")
read_from_file("text1")











