import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import cover
from esphome.const import CONF_ID
from . import IdasenDeskControllerComponent, CONF_IDASEN_DESK_CONTROLLER_ID

DEPENDENCIES = ['esp32', 'idasen_desk_controller']

CONFIG_SCHEMA = cover.COVER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(cover.Cover),
    cv.GenerateID(CONF_IDASEN_DESK_CONTROLLER_ID): cv.use_id(IdasenDeskControllerComponent),
})


async def to_code(config):
    hub = await cg.get_variable(config[CONF_IDASEN_DESK_CONTROLLER_ID])
    var = await cover.new_cover(config)
    await cg.register_parented(var, config[CONF_IDASEN_DESK_CONTROLLER_ID])
    cg.add(hub.set_cover(var))
