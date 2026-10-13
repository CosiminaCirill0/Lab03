from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile

        #self.strumenti e self.prestiti sono delle liste vuote che serviranno per andare a
        #contenere gli oggetti
        self.strumenti = []
        self.prestiti = []

        #contatore che serve per generare codici univoci per i prestiti
        self._numeroPrestiti = 1

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        #si può omettere il try-except perchè nel caso in cui il file non ci dovesse
        # essere, l'opzione è già risolta nel main
        lista_strumenti = []
        with open(file_path, "r", encoding = 'utf-8') as csvfile:
            for row in csvfile:
                r = row.strip().split(',') #row.strip() toglie gli spazi e gli "a capo" a fine riga .split(',') divide la riga in una lista di stringhe usando la virgola come separatore
                strumento = Strumento(r[0], r[1], r[2], int(r[3]), float(r[4]))
                lista_strumenti.append(strumento)
        self.strumenti = lista_strumenti
        return lista_strumenti


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        idNuovoStrumento = f"S{len(self.strumenti)+1}"

        #si crea l'oggetto in memoria e lo si aggiunge alla lista
        nuovoStrumento = Strumento(idNuovoStrumento, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovoStrumento)
        return nuovoStrumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        #ordina gli strumenti per marca
        strumentiOrdinati = sorted(self.strumenti, key = lambda strumento: strumento.marca.lower())
        return strumentiOrdinati


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        strumentoEsistente = False
        for s in self.strumenti: #controlla se lo strumento esiste oppure no
            if s.id_strumento == id_strumento:
                strumentoEsistente = True
                break
        if not strumentoEsistente:
            raise Exception(f"errore, lo strumento richiesto non è presente nel sistema")

        for p in self.prestiti: #controlla se lo strumento è già in prestito
            if p.id_strumento == id_strumento:
                raise Exception(f"lo strumento è già in prestito")

        idNuovoPrestito = f"P{self._numeroPrestiti}" #stringa formattata perchè è richiesto un codice del tipo P5
        self._numeroPrestiti += 1  # serve a incrementare il contatore
        nuovoPrestito = Prestito(idNuovoPrestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(nuovoPrestito)
        return nuovoPrestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        for p in self.prestiti:
            if p.id_prestito == id_prestito:
                self.prestiti.remove(p)
                return True
        raise Exception(f"non è stato trovato nessun prestito con questo codice:{id_prestito} ")