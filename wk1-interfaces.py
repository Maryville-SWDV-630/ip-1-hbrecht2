class Teams:
    def __init__(self, members):
        self.__myTeam = members
    
    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, item):
        if item in self.__myTeam:
            return True
        else:
            return False
    
def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print (len(classmates))
  print('Tim' in classmates)
  print('Sam' in classmates)

main()