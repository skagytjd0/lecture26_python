from win.win import Winning

class WinningDAO:
    def __init__(self):
        self.__winningDB = {}

    def insert_winning(self, winning):
        self.__winningDB[winning.get_win_id()] = winning
        return True

    def select_all_winnings(self):
        if self.__winningDB: return list(self.__winningDB.values())
        return None

    def select_winning(self, win_id):
        if win_id in self.__winningDB: return self.__winningDB[win_id]
        return None

    def delete_winning(self, win_id):
        if win_id in self.__winningDB:
            self.__winningDB.pop(win_id)
            return True
        return False
