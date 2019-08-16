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

    def __generate_specific1(self, data):
        log.info(f"cfg::write : __generate_specific1")
        res = ''
        ip_address = f"{data['bond0.100-b1']}.{data['bond0.100-b2']}.{data['bond0.100-b3']}.{data['bond0.100-b4']}"
        ip_mask = convert_mask_to_str(data['bond0.100-mask'])
        res += f"inet ifconfig bond0.100 address {ip_address} netmask {ip_mask}\n"

        ip_address = f"{data['bond0.101-b1']}.{data['bond0.101-b2']}.{data['bond0.101-b3']}.{data['bond0.101-b4']}"
        ip_mask = convert_mask_to_str(data['bond0.101-mask'])
        res += f"inet ifconfig bond0.101 address {ip_address} netmask {ip_mask}\n"

        ip_address = f"{data['bond0.102-b1']}.{data['bond0.102-b2']}.{data['bond0.102-b3']}.{data['bond0.102-b4']}"
        ip_mask = convert_mask_to_str(data['bond0.102-mask'])
        res += f"inet ifconfig bond0.102 address {ip_address} netmask {ip_mask}\n"

        ip_address = f"{data['eth3-p3-isp2-c2-b1']}.{data['eth3-p3-isp2-c2-b2']}.{data['eth3-p3-isp2-c2-b3']}.{data['eth3-p3-isp2-c2-b4']}"
        ip_mask = convert_mask_to_str(data['eth3-p3-isp2-c2-mask'])
        res += f"inet ifconfig eth3 address {ip_address} netmask {ip_mask}"

        return res

    def __generate_specific2(self, data):
        log.info(f"cfg::write : __generate_specific2")
        res = ''
        ip_address = f"{data['failover-isp1-b1']}.{data['failover-isp1-b2']}.{data['failover-isp1-b3']}.{data['failover-isp1-b4']-1}"
        res += f"inet route add default next-hop {ip_address} table 1024 name ISP1\n"

        ip_address = f"{data['failover-isp2-b1']}.{data['failover-isp2-b2']}.{data['failover-isp2-b3']}.{data['failover-isp2-b4']-1}"
        res += f"inet route add default next-hop {ip_address} table 1025 name ISP2"

        return res

    def __generate_specific3(self, data):
        log.info(f"cfg::write : __generate_specific3")
        res = ''
        ip_address = f"{data['failover-isp1-b1']}.{data['failover-isp1-b2']}.{data['failover-isp1-b3']}.{data['failover-isp1-b4']-1}"
        res += f"inet dgd next-hop add GW-1-hop address {ip_address} check icmp\n"

        ip_address = f"{data['failover-isp2-b1']}.{data['failover-isp2-b2']}.{data['failover-isp2-b3']}.{data['failover-isp2-b4']-1}"
        res += f"inet dgd next-hop add GW-2-hop address {ip_address} check icmp\n"

        ip_address = f"{data['failover-bond0.100-b1']}.{data['failover-bond0.100-b2']}.{data['failover-bond0.100-b3']}.{data['failover-bond0.100-b4']-1}"
        id_mask = '26' if  data['tunnel-nets-b4'] == '1-62' else '27'
        res += f"inet policy rule add isp-both 1025 match address from {ip_address}/{id_mask}"

        return res

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

        # 2 add data-specific rows
        render_data = {
            'hostname': data['hostname'],
            'data_specific_part1': self.__generate_specific1(data),
            'data_specific_part2': self.__generate_specific2(data),
            'data_specific_part3': self.__generate_specific3(data),
        }

        content = template.render(**render_data)
        with open(os.path.join(self.out_dir, cfg_name), 'w', encoding='utf-8') as cfg_file:
            cfg_file.writelines(content)

        log.info(f"cfg::write : successfully")
