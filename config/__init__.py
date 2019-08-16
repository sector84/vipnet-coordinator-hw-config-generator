from .cfg_writer import CfgWriter

cfg_writer = CfgWriter.get_instance()

__all__ = [
    'cfg_writer',
]