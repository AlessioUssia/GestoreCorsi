from database.corso_dao import CorsoDao
from model import corso


class Model:

    def __init__(self):
        self.corsi = CorsoDao.get_all_corsi()

    def get_corsi_periodo(self, pd):
        # Soluzione programmatica
        result = []
        for corso in self.corsi:
            if corso.pd == int(pd):
                result.append(corso)
        # Soluzione da DAO
        #return CorsoDao.get_corsi_periodo(self, pd)

    def get_studenti_periodo(self, pd):

        # Soluzione con join da SQL
        # matricole = CorsoDao.get_studenti_periodo(self, pd)
        # return len(matricole)

        # Soluzione con map relazione
        matricole = set()
        for corso in self.corsi:
            if corso.pd == int(pd):
                # chiedo al corso i suoi iscritti
                matricole_corso = corso.get_studenti()
                # se il corso non sa i suoi iscritti, li chiedo al DAO e li inserisco nel corso
                if matricole_corso is None:
                    CorsoDao.get_studenti_singolo_corso(corso.codins)
                    matricole_corso = corso.studenti
                # calcolo la union di matricole
                matricole = matricole.union(matricole_corso)
        return len(matricole)


