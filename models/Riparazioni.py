from datetime import date

from pydantic import BaseModel, Field

from database import Database


class Riparazione(BaseModel):
    id: int
    dataIngresso: date
    dataCompletata: date = Field(default=date.min)
    dataUscita: date = Field(default=date.min)
    descrizioneGuasto: str
    descrizioneRiparazione: str
    prezzo: float = Field(default=0.0, ge=0)
    fk_cliente: int
    fk_stato_riparazione: int = Field(default=0)
    def clienteDaIdRip(self):
        if self.fk_cliente == -1:
            return "Nessun Cliente"
        nome = Database.getNomeCognomeClienteByRiparazioneId(self.id)
        return nome

    def clienteTelefono(self):
        if self.fk_cliente == -1:
            return None

        telefono: str = Database.getClienteById(self.fk_cliente).telefono
        return telefono

    def stato(self):
        if self.fk_stato_riparazione == 1:
            return "In Attesa"
        elif self.fk_stato_riparazione == 3:
            return "Completata"
        elif self.fk_stato_riparazione == 4:
            return "Ritirata ma non Pagata"
        elif self.fk_stato_riparazione == 5:
            return "Ritirata e Pagata"
        elif self.fk_stato_riparazione == 6:
            return "Non Riparabile"

    def getNomeOggetto(self):
        return Database.getNameObject(self.id)

    def getModelloOggetto(self):
        return Database.getModelloObject(self.id)

    def getMatricolaOggetto(self):
        return Database.getMatricolaObject(self.id)

    def getMarcaOggetto(self):
        return Database.getMarcaObject(self.id)

    def getAccessorioOggetto(self):
        return Database.getAccessorioObject(self.id)


