from pydantic import BaseModel

class RiparazioneCompletata(BaseModel):
    id: int
    descrizioneRiparazione: str
    prezzo: float
    statoRiparazione: str

    def statoToInt(self):
        if self.statoRiparazione == "Completata":
            return 3
        elif self.statoRiparazione == "Ritirata ma non Pagata":
            return 4
        elif self.statoRiparazione == "Ritirata e Pagata":
            return 5