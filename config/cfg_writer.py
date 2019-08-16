import os

import glog as log
import jinja2
from jinja2 import Environment, FileSystemLoader
from globals import general_params, convert_mask_to_str


class CfgWriter:
    instance = None

    def __init__(self):
        log.info('CfgWriter::init')

        # j2_env = Environment(loader=FileSystemLoader(this_dir), trim_blocks=True)
        self.j2_env = Environment(loader=FileSystemLoader('./cfg_templates'))

        self.out_dir = './_output'
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CfgWriter()
        return cls.instance

    def write(self, data, cfg_name):
        log.info(f"cfg::write : write config to file: {cfg_name} - start")
        # 1 read template
        try:
            template = self.j2_env.get_template(general_params.template)
        except jinja2.TemplateNotFound as nf:
            log.error(f"cfg::write : failed to write: Template {general_params.template} not found")
            return
        except Exception as e:
            log.error(f"cfg::write : failed to write: Template {general_params.template} general error: {e}")
            return

        render_data = {
            'hostname': data['hostname'],
            'data_specific_rows': '',
        }
        # 2 add data-specific rows
        ip_address = f"{data['bond0.100-b1']}.{data['bond0.100-b2']}.{data['bond0.100-b3']}.{data['bond0.100-b4']}"
        ip_mask = convert_mask_to_str(data['bond0.100-mask'])
        render_data['data_specific_rows'] += f"inet ifconfig bond0.100 address {ip_address} netmask {ip_mask}\n"

        ip_address = f"{data['bond0.101-b1']}.{data['bond0.101-b2']}.{data['bond0.101-b3']}.{data['bond0.101-b4']}"
        ip_mask = convert_mask_to_str(data['bond0.101-mask'])
        render_data['data_specific_rows'] += f"inet ifconfig bond0.101 address {ip_address} netmask {ip_mask}\n"

        ip_address = f"{data['bond0.102-b1']}.{data['bond0.102-b2']}.{data['bond0.102-b3']}.{data['bond0.102-b4']}"
        ip_mask = convert_mask_to_str(data['bond0.102-mask'])
        render_data['data_specific_rows'] += f"inet ifconfig bond0.102 address {ip_address} netmask {ip_mask}\n"

        ip_address = f"{data['eth3-p3-isp2-c2-b1']}.{data['eth3-p3-isp2-c2-b2']}.{data['eth3-p3-isp2-c2-b3']}.{data['eth3-p3-isp2-c2-b4']}"
        ip_mask = convert_mask_to_str(data['eth3-p3-isp2-c2-mask'])
        render_data['data_specific_rows'] += f"inet ifconfig eth3 address {ip_address} netmask {ip_mask}\n"

        content = template.render(**render_data)
        with open(os.path.join(self.out_dir, cfg_name), 'w', encoding='utf-8') as cfg_file:
            cfg_file.writelines(content)

        log.info(f"cfg::write : successfully")
