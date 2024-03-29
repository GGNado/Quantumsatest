from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from database.Database import *

router = APIRouter(
	tags=['Riparazioni'],
	prefix='/api/v1.0/riparazioni'
)

templates = Jinja2Templates(
	directory='templates',
	autoescape=False,
	auto_reload=True
)


@router.get('/')
async def getPagina(req: Request):
	return templates.TemplateResponse(
		'riparazioni.html', {
			'request': req,
			'riparazioni': getRiparazioni(),
			'cliente': None
		}
	)

@router.get('/{id}')
async def getPagina(req: Request, id: int):
	return templates.TemplateResponse(
		'riparazioni.html', {
			'request': req,
			'riparazioni': getRiparazioniByFK_Cliente(id),
			'cliente': getClienteById(id)
		}
	)

@router.get("/{id}/add")
async def getPagina(id: int, req: Request):
	return templates.TemplateResponse(
		'riparazioniAdd.html', {
			'request': req,
			'cliente': getClienteById(id)
		}
	)

@router.post("/add")
async def aggiungiRiparazione(rip: RiparazioneInput):
	addRiparazioni(rip)

@router.delete("/{id}")
async def eliminaRiparazione(id: int):
	deleteRiparazione(id)

@router.put("/edit")
async def modificaRiparazione(rip: RiparazioneInput):
	updateRiparazioni(rip)

@router.get("/{id}/edit")
async def cambiaPag(req: Request, id: int):
	return templates.TemplateResponse(
		'RiparazioniEdit.html', {
			'request': req,
			'rip': getRiparazioniById(id)
		}
	)

@router.get("/{id}/completa")
async def cambiaPag(req: Request, id: int):
	return templates.TemplateResponse(
		'riparazioniCompleta.html', {
			'request': req,
			'rip': getRiparazioniById(id)
		}
	)

@router.put("/completa")
async def completaRiparazione(rip: RiparazioneCompletata):
	completeRiparazione(rip)

@router.get("/filtro/{fk_Cliente}/{stato}/{marca}/{modello}/{descrizioneRiparazione}/{id}")
async def filtraRiparazioni(req: Request, fk_Cliente: int = -1, stato: int = -1, marca: str = "", modello: str = "", descrizioneRiparazione: str = "", id: int = -1):
	return templates.TemplateResponse(
		'riparazioni.html', {
			'request': req,
			'cliente': getClienteById(fk_Cliente),
			'riparazioni': getRiparazioniFiltro(fk_Cliente, stato, marca, modello, descrizioneRiparazione, id),
		}
	)
