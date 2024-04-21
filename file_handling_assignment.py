class FileHandling:

  def write(self):
    try:
      file = open('my_file.txt', 'w')
      file.write('This is my first file\n')
      file.write('The file contains three lines:'+str(123)+'\n')
      file.write('And this is the final line\n')
    except FileNotFoundError:
      print("Error: File not found") 
    except PermissionError:
      print("Error: Permission denied")
    finally:
      file.close()

  def read(self):
    try:
      file = open('my_file.txt', 'r')
      content = file.read()
      print(content)
    except FileNotFoundError:
      print("Error: File not found")
    except PermissionError:
      print("Error: Permission denied")
    finally:
      file.close()
  
  def append(self):
    try:
      file = open('my_file.txt', 'a')
      file.write('This is the appended line\n')
      file.write('it includes two lines\n')
    except FileNotFoundError:
      print("Error: File not found")
    except PermissionError:
      print("Error: Permission denied")
    finally:
      file.close()

file = FileHandling()
file.write()
file.read()
file.append() 
file.read()
