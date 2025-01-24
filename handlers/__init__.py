from aiogram import Router

from handlers.help import router as help_router
from handlers.imei import router as imei_router


router = Router()
router.include_router(help_router)
router.include_router(imei_router)
